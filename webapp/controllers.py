#!/usr/bin/python
# encoding: iso-8859-1
""" Filename:        controllers.py
    Purpose:         Este arquivo � uma das possiveis views, que podem conter
                     rotas da aplicacao.
    Requirements:    Nao se aplica
    Author:          Humbertho Mattar
"""
import json
import cerberus
from flask import request
from flask import abort
from webapp import app
from webapp import schemas
from webapp import utils
from webapp import database
import datetime


@app.route('/info/', methods=['GET', 'HEAD'])
def info():

    mensagem = {'nome da aplicacao': app.config['APP_NAME'],
                'versao': app.config['VERSION']}
    return json.dumps(mensagem)


# TODO: Definir mensagem de alerta
@app.route('/uptimeRobotAlerts/', methods=['GET', 'POST'])
def uptime_robot_alerts():
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    try:
        v = cerberus.Validator(schemas.uptime_robot_alerts)
        if not v.validate(request.args):
            app.logger.error('schema erro: ' + str(v.errors))
            abort(400)
        else:
            url = 'https://api.telegram.org/bot%s/sendMessage' % (app.config['TELEGRAM_TOKEN'])
            text = 'DTP_MONITOR :: Informa\n\n'
            text += 'Sistema: %s\n' % request.args['monitorFriendlyName']
            text += 'URL: %s\n' % request.args['monitorURL']
            if request.args['alertType'] == '1':
                text += 'Status atual: OFFLINE\n'
            else:
                text += 'Status atual: ONLINE\n'
            text += 'Desde de: %s\n' % datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')
            text += 'Detalhes: %s' % request.args['alertDetails'].upper()

            rows = database.search_chats()
            if rows:
                for row in rows:
                    req = utils.post_with_query_string(url=url, params={'chat_id': row, 'text': text}, headers=headers)
                    app.logger.info(req.text)
                return 'OK', 200
            else:
                return 'OK', 204
    except Exception as e:
        app.logger.error('uptimeRobotAlerts - N�o foi possivel enviar a mensagem.')
        app.logger.error(str(e))
        abort(400)


@app.errorhandler(400)
def bad_request():
    mensagem = {'status code': 400,
                'message': 'bad request'
                }
    return json.dumps(mensagem), 400


@app.errorhandler(500)
def internal_server_error():
    mensagem = {'status code': 500,
                'message': 'internal server error'
                }
    return json.dumps(mensagem), 500


@app.errorhandler(404)
def page_not_found():
    mensagem = {'status code': 404,
                'message': 'page not found'
                }
    return json.dumps(mensagem), 404
