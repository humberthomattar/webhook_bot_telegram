#!/usr/bin/python
# encoding: iso-8859-1

""" Filename:     __init__.py
    Purpose:      Este arquivo e necesserio para estruturar o servico da web
                  como um pacote,
                  para poder definir rotas em varios modulos e definir
                  variaveis globais.
    Requirements: Flask
    Author:       humbertho mattar
"""

from flask import Flask

app = Flask(__name__)

# configuracoees externalizadas - classes de conf/config.py
app.config.from_object('webapp.config.DevelopmentConfig')

# A importacaoo de m�dulos de visualiza��es DEVE SER no final do arquivo para
# evitar problemas  relacionados a importa��es circulares.


import webapp.controllers  # noqa
