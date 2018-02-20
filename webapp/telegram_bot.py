import telegram
from webapp import utils
from webapp import message_handler
from webapp import app
from telegram.ext import Updater, MessageHandler, Filters
from telegram.ext import CommandHandler
from webapp import uptime_connect
import json

global monitors

def start(bot, update):
    msg = message_handler.BOT_MSG_START
    bot.send_message(chat_id=update.message.chat_id, text=msg)
    menu_principal(bot, update)

def inscrever(bot, update):
    try:
        chats = utils.load_json('webapp/chats.json')
        if update.message.chat_id not in chats['chat_id']:
            chats['chat_id'].append(update.message.chat_id)
            utils.write_json('webapp/chats.json', chats)
            bot.send_message(chat_id=update.message.chat_id, text=message_handler.BOT_MSG_JSON_INSC_OK)
        else:
            bot.send_message(chat_id=update.message.chat_id, text=message_handler.BOT_MSG_JSON_INSC_NOK)
    except Exception as e:
        print(str(e))


def desinscrever(bot, update):
    chats = utils.load_json('webapp/chats.json')
    if update.message.chat_id not in chats['chat_id']:
        bot.send_message(chat_id=update.message.chat_id, text=message_handler.BOT_MSG_JSON_DESINSC_OK)
    else:
        chats['chat_id'].remove(update.message.chat_id)
        utils.write_json('webapp/chats.json', chats)
        bot.send_message(chat_id=update.message.chat_id, text=message_handler.BOT_MSG_JSON_DESINSC_NOK)


def menu_principal(bot, update):
    msg = message_handler.BOT_MSG_MENU
    #global monitors
    #monitors = getListaMonitores()
    #for m in monitors['monitors']:
    #    msg+= "/%s \n" % m['friendly_name']

    main_menu_keyboard = [[telegram.KeyboardButton('/menu')],
                          [telegram.KeyboardButton('/inscrever')],
                          [telegram.KeyboardButton('/desinscrever')]]

    reply_kb_markup = telegram.ReplyKeyboardMarkup(main_menu_keyboard,
                                                   resize_keyboard=True,
                                                   one_time_keyboard=True)
    bot.send_message(chat_id=update.message.chat_id,
                     text=msg,
                     reply_markup=reply_kb_markup)

def menu_sistemas(bot, update):
    msg = message_handler.BOT_MSG_MENU_SISTEMAS

    global monitors
    monitors = getListaMonitores()

    for m in monitors['monitors']:
        msg+= "/%s \n" % m['friendly_name']

    bot.send_message(chat_id=update.message.chat_id,
                     text=msg)


def unknown(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text=message_handler.BOT_MSG_UNKNOWN)

def getListaMonitores(**kwargs):
    try:
        res = utils.post_with_query_string(url=uptime_connect.URL_CONNECT, params=uptime_connect.PAYLOAD, headers=uptime_connect.HEADERS)
        if (res.status_code == 200):
            parsed_json = json.loads(res.text)
            return parsed_json
            #return parsed_json.get('monitors')
        else:
            print(res.text)

    except Exception as ex:
        print(ex)

# Criacao do objeto updater #
if app.config['PROXY_HABILITADO']:
    updater = Updater(token=app.config['TELEGRAM_TOKEN'], request_kwargs={'proxy_url': app.config['PROXY_ADRESS']})
else:
    updater = Updater(token=app.config['TELEGRAM_TOKEN'])
dispatcher = updater.dispatcher


# Criacao dos objetos de comando #
start_handler = CommandHandler('start', start)
menu_principal_handler = CommandHandler('menu', menu_principal)
menu_sistemas_handler = CommandHandler('sistemas', menu_sistemas)
inscrever_handler = CommandHandler('inscrever', inscrever)
desinscrever_handler = CommandHandler('desinscrever', desinscrever)
unknown_handler = MessageHandler(Filters.command, unknown)


# ADD Comandos ao dispatcher #
dispatcher.add_handler(start_handler)
dispatcher.add_handler(menu_principal_handler)
dispatcher.add_handler(menu_sistemas_handler)
dispatcher.add_handler(inscrever_handler)
dispatcher.add_handler(desinscrever_handler)
dispatcher.add_handler(unknown_handler)

updater.start_polling()

