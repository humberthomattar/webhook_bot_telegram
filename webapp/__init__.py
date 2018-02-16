#!/usr/bin/python
# encoding: iso-8859-1
""" Filename:     __init__.py
    Purpose:      Este arquivo é necessário para estruturar o serviço da web como um pacote,
                  para poder definir rotas em vários módulos e definir variáveis globais.
    Requirements: Flask
    Author:       humbertho mattar
"""

from flask import Flask

app = Flask(__name__)


# configurações externalizadas - classes de conf/config.py
app.config.from_object('webapp.config.DevelopmentConfig')



# A importação de módulos de visualizações DEVE SER no final do arquivo para evitar problemas
# relacionados a importações circulares.
import webapp.controllers
import webapp.telegram_bot
