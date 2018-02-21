#!/usr/bin/python
# encoding: iso-8859-1
""" Filename:     run.py
    Purpose:      Esse arquivo tem o unico objetivo de executar corretamente a aplicacao
    Requirements: Flask
    Author:       Humbertho Mattar
"""
from webapp import app
import webapp.telegram_bot
import sys


if __name__ == '__main__':
    sys.exit(app.run(debug=app.config['DEBUG'],
                     host=app.config['HOST'],
                     port=app.config['PORT']))


