# encoding: iso-8859-1
""" Filename:     config.py
    Purpose:      Este arquivo  externaliza as configurações da aplicação. Separando os ambientes por classes
                  BaseConfig = PRODUCAO - as demais classes herdam e sobreescrem os atributos de produção..
    Requirements:
    Author:       humbertho mattar
"""
import os

class BaseConfig(object):
    DEBUG = False
    TESTING = False
    APP_NAME = 'dtp_webhooks'
    VERSION = '0.0.1'
    PROXY_HABILITADO = bool(os.environ['PROXY_HABILITADO'])
    LOG_FILENAME = 'webapp/log/log_%s.log' % APP_NAME
    LOG_LEVEL = 'INFO'  # DEBUG OU INFO


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    TESTING = False
    HOST = '0.0.0.0'
    PORT = int(os.environ.get("PORT", 5000))
    TELEGRAM_TOKEN = os.environ['TELEGRAM_TOKEN']
    UPTIMEROBOT_TOKEN = os.environ['UPTIMEROBOT_TOKEN']
    PROXY_ADRESS = os.environ['PROXY_ADRESS']
    PROXY_HABILITADO = bool(os.environ['PROXY_HABILITADO'])
    LOG_LEVEL = 'DEBUG'  # DEBUG OU INFO


class TestingConfig(BaseConfig):
    DEBUG = False
    TESTING = False
    HOST = '0.0.0.0'
    PORT = 88
    TELEGRAM_TOKEN = os.environ['TELEGRAM_TOKEN']
    UPTIMEROBOT_TOKEN = os.environ['UPTIMEROBOT_TOKEN']
    PROXY_ADRESS = os.environ['PROXY_ADRESS']
    PROXY_HABILITADO = bool(os.environ['PROXY_HABILITADO'])
    LOG_LEVEL = 'DEBUG'  # DEBUG OU INFO
