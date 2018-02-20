#!/usr/bin/python
# encoding: iso-8859-1
""" Filename:        controllers.py
    Purpose:         Este arquivo é uma das possiveis views, que podem conter
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
import datetime


@app.route('/info/', methods=['GET'])
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
            text = 'DTP_MONITOR :: Informa\n'
            text += 'Sistema: %s\n' % request.args['monitorFriendlyName']
            text += 'URL: %s\n' % request.args['monitorURL']
            text += 'Status atual: %s\n' % request.args['alertTypeFriendlyName'].upper()
            text += 'Desde de: %s\n' % datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')

            chats = utils.load_json('webapp/chats.json')
            for chat_id in chats['chat_id']:
                req = utils.post_with_query_string(url=url, params={'chat_id': chat_id, 'text': text}, headers=headers)
                app.logger.info(req.text)
            return 'OK', 200
    except Exception as e:
        app.logger.error('uptimeRobotAlerts - Não foi possivel enviar a mensagem.')
        app.logger.error(str(e))
        abort(400)


@app.errorhandler(400)
def bad_request(e):
    mensagem = {'status code': 400,
                'message': 'bad request'
                }
    return json.dumps(mensagem), 400


@app.errorhandler(500)
def internal_server_error(e):
    mensagem = {'status code': 500,
                'message': 'internal server error'
                }
    return json.dumps(mensagem), 500


@app.errorhandler(404)
def page_not_found(e):
    mensagem = {'status code': 404,
                'message': 'page not found'
                }
    return json.dumps(mensagem), 404
