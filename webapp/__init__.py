#!/usr/bin/python
# encoding: iso-8859-1
""" Filename:     __init__.py
    Purpose:      Este arquivo � necess�rio para estruturar o servi�o da web como um pacote,
                  para poder definir rotas em v�rios m�dulos e definir vari�veis globais.
    Requirements: Flask
    Author:       humbertho mattar
"""

from flask import Flask

app = Flask(__name__)


# configura��es externalizadas - classes de conf/config.py
app.config.from_object('webapp.config.DevelopmentConfig')



# A importa��o de m�dulos de visualiza��es DEVE SER no final do arquivo para evitar problemas
# relacionados a importa��es circulares.
import webapp.controllers
import webapp.telegram_bot
