import telegram
from webapp import utils
from webapp import message_handler
from webapp import app
from webapp import database
from telegram.ext import Updater, MessageHandler, Filters
from telegram.ext import CommandHandler
from webapp import uptime_connect
import json
import datetime
import time
import os


def start(bot, update):
    msg = message_handler.BOT_MSG_START
    bot.send_message(chat_id=update.message.chat_id, text=msg)
    menu_principal(bot, update)


def inscrever(bot, update):
    try:
        if not database.search_chat_id(chat_id=update.message.chat_id):
            chats = bot.getChat(update.message.chat_id)
            if database.insert_chat(
                chat_id=chats['id'], type=chats['type'],
                username=chats['username'], first_name=chats['first_name'],
                last_name=chats['last_name']
            ):
                bot.send_message(
                    chat_id=update.message.chat_id,
                    text=message_handler.BOT_MSG_INSC_OK
                )
            else:
                app.logger.error("DatabaseAlerts - NÃ£o foi possivel realizar inscrição no BD. ChatId: %s"
                                 % update.message.chat_id)
                bot.send_message(
                    chat_id=update.message.chat_id,
                    text=message_handler.BOT_MSG_INSC_ERRO
                )

        else:
            bot.send_message(
                chat_id=update.message.chat_id,
                text=message_handler.BOT_MSG_INSC_NOK
            )

        # chats = utils.load_json('webapp/chats.json')
        # if update.message.chat_id not in chats['chat_id']:
        #     chats['chat_id'].append(update.message.chat_id)
        #     utils.write_json('webapp/chats.json', chats)
        #     bot.send_message(chat_id=update.message.chat_id,
        #       text=message_handler.BOT_MSG_JSON_INSC_OK)
        # else:
        #     bot.send_message(chat_id=update.message.chat_id,
        #       text=message_handler.BOT_MSG_JSON_INSC_NOK)

    except Exception as e:
        print(str(e))


def desinscrever(bot, update):
    try:
        if database.search_chat_id(chat_id=update.message.chat_id):
            if database.remove_chat(chat_id=update.message.chat_id):
                bot.send_message(
                    chat_id=update.message.chat_id,
                    text=message_handler.BOT_MSG_DESINSC_OK
                )
            else:
                bot.send_message(
                    chat_id=update.message.chat_id,
                    text=message_handler.BOT_MSG_DESINSC_ERRO
                )
        else:
            bot.send_message(
                chat_id=update.message.chat_id,
                text=message_handler.BOT_MSG_DESINSC_NOK
            )

        # chats = utils.load_json('webapp/chats.json')
        # if update.message.chat_id not in chats['chat_id']:
        #     chats['chat_id'].append(update.message.chat_id)
        #     utils.write_json('webapp/chats.json', chats)
        #     bot.send_message(chat_id=update.message.chat_id,
        #       text=message_handler.BOT_MSG_JSON_INSC_OK)
        # else:
        #     bot.send_message(chat_id=update.message.chat_id,
        #       text=message_handler.BOT_MSG_JSON_INSC_NOK)

    except Exception as e:
        print(str(e))

    # chats = utils.load_json('webapp/chats.json')
    # if update.message.chat_id not in chats['chat_id']:
    #     bot.send_message(chat_id=update.message.chat_id,
    #       text=message_handler.BOT_MSG_DESINSC_OK)
    # else:
    #     chats['chat_id'].remove(update.message.chat_id)
    #     utils.write_json('webapp/chats.json', chats)
    #     bot.send_message(chat_id=update.message.chat_id,
    #       text=message_handler.BOT_MSG_DESINSC_NOK)


def menu_principal(bot, update):
    msg = message_handler.BOT_MSG_MENU

    main_menu_keyboard = [[telegram.KeyboardButton('/menu')],
                          [telegram.KeyboardButton('/inscrever')],
                          [telegram.KeyboardButton('/desinscrever')],
                          [telegram.KeyboardButton('/sistemas')]]

    reply_kb_markup = telegram.ReplyKeyboardMarkup(main_menu_keyboard,
                                                   resize_keyboard=True,
                                                   one_time_keyboard=True)
    bot.send_message(chat_id=update.message.chat_id,
                     text=msg,
                     reply_markup=reply_kb_markup)


def menu_sistemas(bot, update):
    msg = message_handler.BOT_MSG_MENU_SISTEMAS

    monitors = get_lista_monitores()
    utils.write_json('webapp/sistemas.json', monitors)

    for m in monitors['monitors']:
        msg += "/%s \n" % m['friendly_name']

    bot.send_message(chat_id=update.message.chat_id,
                     text=msg)


def unknown(bot, update):
    try:
        found = False
        msg = update.message.text.lstrip('/')
        file = utils.load_json('webapp/sistemas.json')

        for monitors in file['monitors']:
            if msg == monitors['friendly_name']:
                found = True
                bot.send_message(
                    chat_id=update.message.chat_id,
                    text=get_info_monitor(id=monitors['id'])
                )

        if not found:
            bot.send_message(
                chat_id=update.message.chat_id,
                text=message_handler.BOT_MSG_UNKNOWN
            )

    except Exception as e:
        print(e)


def get_lista_monitores():
    try:
        payload = uptime_connect.PAYLOAD + '&logs_limit=1'
        res = utils.post_with_query_string(
            url=uptime_connect.URL_CONNECT,
            params=payload,
            headers=uptime_connect.HEADERS
        )
        if res.status_code == 200:
            parsed_json = json.loads(res.text)
            return parsed_json
        else:
            print(res.text)

    except Exception as ex:
        print(ex)


def get_info_monitor(**kwargs):
    try:
        msg = ""
        payload = uptime_connect.PAYLOAD + '&logs_limit=1&monitors=%s' % kwargs['id']
        res = utils.post_with_query_string(
            url=uptime_connect.URL_CONNECT,
            params=payload,
            headers=uptime_connect.HEADERS
        )
        if res.status_code == 200:
            parsed_json = json.loads(res.text)

            for m in parsed_json['monitors']:
                msg += 'DTP MONITOR :: INFORMA\n\n'
                msg += 'Sistema: %s \n' % (m['friendly_name'])
                msg += 'URL: %s \n' % (m['url'])
                if m.get('logs')[0].get('type') == 2:
                    msg += 'Status: ONLINE \n'
                else:
                    msg += 'Status: OFFLINE \n'
                msg += 'Desde: %s \n' % (datetime.datetime.fromtimestamp(
                    int(m.get('logs')[0].get('datetime'))
                ).strftime('%d-%m-%Y %H:%M:%S'))

            return msg
        else:
            print(
                'Retorno indevido do UptimeRobot. Detalhamento: %s' % res.text
            )

    except Exception as ex:
        print(
            'Problema na conexão com o UptimeRobot para busca de Informações \
             do Monitor. Detalhamento: %s ' % ex)


def get_status_monitor(**kwargs):
    try:
        payload = uptime_connect.PAYLOAD + '&logs_limit=1&monitors=%s' % kwargs['id']
        res = utils.post_with_query_string(
            url=uptime_connect.URL_CONNECT,
            params=payload,
            headers=uptime_connect.HEADERS
        )
        if res.status_code == 200:
            parsed_json = json.loads(res.text)
            for m in parsed_json['monitors']:
                return m.get('logs')[0].get('type')
        else:
            print(
                'Retorno indevido do UptimeRobot. Detalhamento: %s' % res.text
            )

    except Exception as ex:
        print(
            'Problema na conexão com o UptimeRobot para busca de Informações \
             do Monitor. Detalhamento: %s ' % ex)


def retry_status_monitor(**kwargs):
    count = 1
    while count < app.config['RETRY_TIMES']:
        time.sleep(app.config['RETRY_SECONDS'])
        if int(get_status_monitor(id=kwargs['monitorID'])) == 2:
            return 2
        else:
            count += 1
    return get_status_monitor(id=kwargs['monitorID'])


def verify_downtime(**kwargs):
    try:
        payload = uptime_connect.PAYLOAD + '&logs_limit=1&monitors=%s' % kwargs['monitorID']
        res = utils.post_with_query_string(
            url=uptime_connect.URL_CONNECT,
            params=payload,
            headers=uptime_connect.HEADERS
        )
        print(res)
        if res.status_code == 200:
            retrys = int(os.environ['RETRY_TIMES']) * int(os.environ['RETRY_SECONDS'])
            parsed_json = json.loads(res.text)
            for m in parsed_json['monitors']:
                if int(m.get('logs')[0].get('duration')) > retrys:
                    return 0
                else:
                    return 1
        else:
            print(
                'Retorno indevido do UptimeRobot. Detalhamento: %s' % res.text
            )

    except Exception as ex:
        print(
            'Problema na conexão com o UptimeRobot para busca de Informações \
             do Monitor. Detalhamento: %s ' % ex)





# Criacao do objeto updater
if app.config['PROXY_HABILITADO']:
    updater = Updater(
        token=app.config['TELEGRAM_TOKEN'],
        request_kwargs={'proxy_url': app.config['PROXY_ADRESS']}
    )
else:
    updater = Updater(token=app.config['TELEGRAM_TOKEN'])

dispatcher = updater.dispatcher


# Criacao dos objetos de comando
start_handler = CommandHandler('start', start)
menu_principal_handler = CommandHandler('menu', menu_principal)
inscrever_handler = CommandHandler('inscrever', inscrever)
desinscrever_handler = CommandHandler('desinscrever', desinscrever)
menu_sistemas_handler = CommandHandler('sistemas', menu_sistemas)
unknown_handler = MessageHandler(Filters.command, unknown)


# ADD Comandos ao dispatcher
dispatcher.add_handler(start_handler)
dispatcher.add_handler(menu_principal_handler)
dispatcher.add_handler(menu_sistemas_handler)
dispatcher.add_handler(inscrever_handler)
dispatcher.add_handler(desinscrever_handler)
dispatcher.add_handler(unknown_handler)

updater.start_polling()
