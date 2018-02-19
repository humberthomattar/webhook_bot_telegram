import telegram
from webapp import utils
from webapp import message_handler
from webapp import app
from telegram.ext import Updater, MessageHandler, Filters
from telegram.ext import CommandHandler


def start(bot, update):
    msg = message_handler.BOT_MSG_START
    bot.send_message(chat_id=update.message.chat_id, text=msg)
    menu(bot, update)

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


def menu(bot, update):
    msg = message_handler.BOT_MSG_MENU

    main_menu_keyboard = [[telegram.KeyboardButton('/menu')],
                          [telegram.KeyboardButton('/inscrever')],
                          [telegram.KeyboardButton('/desinscrever')]]

    reply_kb_markup = telegram.ReplyKeyboardMarkup(main_menu_keyboard,
                                                   resize_keyboard=True,
                                                   one_time_keyboard=True)
    bot.send_message(chat_id=update.message.chat_id,
                     text=msg,
                     reply_markup=reply_kb_markup)


def unknown(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text=message_handler.BOT_MSG_UNKNOWN)


# Criacao do objeto updater #
if app.config['PROXY_HABILITADO']:
    updater = Updater(token=app.config['TELEGRAM_TOKEN'], request_kwargs={'proxy_url': app.config['PROXY_ADRESS']})
else:
    updater = Updater(token=app.config['TELEGRAM_TOKEN'])
dispatcher = updater.dispatcher


# Criacao dos objetos de comando #
start_handler = CommandHandler('start', start)
menu_handler = CommandHandler('menu', menu)
inscrever_handler = CommandHandler('inscrever', inscrever)
desinscrever_handler = CommandHandler('desinscrever', desinscrever)
unknown_handler = MessageHandler(Filters.command, unknown)


# ADD Comandos ao dispatcher #
dispatcher.add_handler(start_handler)
dispatcher.add_handler(menu_handler)
dispatcher.add_handler(inscrever_handler)
dispatcher.add_handler(desinscrever_handler)
dispatcher.add_handler(unknown_handler)

updater.start_polling()

