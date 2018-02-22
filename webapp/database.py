#!/usr/bin/python
# encoding: iso-8859-1

from urllib import parse
import psycopg2
from webapp import app


def connect_bd():
    parse.uses_netloc.append('postgres')
    url = parse.urlparse(app.config['DATABASE_URL'])

    conn = psycopg2.connect(
        database=url.path[1:],
        user=url.username,
        password=url.password,
        host=url.hostname,
        port=url.port
    )
    return conn


def search_chats():
    try:
        conn = connect_bd()
        cursor = conn.cursor()
        cursor.execute("SELECT id FROM chat")
        rows = cursor.fetchall()

        if cursor.rowcount != 0:
            cursor.close()
            conn.close()
            return rows
        else:
            cursor.close()
            conn.close()
            return False

    except Exception as e:
        app.logger.error(
            'DatabaseAlerts - Não foi possivel realizar consulta ao BD'
        )
        app.logger.error(str(e))


def search_chat_id(**kwargs):
    try:
        conn = connect_bd()
        cursor = conn.cursor()
        cursor.execute("SELECT id FROM chat WHERE id = %s" % kwargs['chat_id'])

        if cursor.rowcount != 0:
            cursor.close()
            conn.close()
            return True
        else:
            cursor.close()
            conn.close()
            return False

    except Exception as e:
        app.logger.error(
            'DatabaseAlerts - Não foi possivel realizar consulta ao BD'
        )
        app.logger.error(str(e))


def insert_chat(**kwargs):
    try:
        conn = connect_bd()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO chat (id, type, username, first_name, last_name) "
            "VALUES (%s,'%s','%s','%s','%s')" % (
                kwargs['chat_id'], kwargs['type'], kwargs['username'],
                kwargs['first_name'], kwargs['last_name']
            )
        )

        if cursor.rowcount != 0:
            conn.commit()
            cursor.close()
            conn.close()
            return True
        else:
            cursor.close()
            conn.close()
            return False

    except Exception as e:
        app.logger.error(
            'DatabaseAlerts - Não foi possivel incluir registro no BD'
        )
        app.logger.error(str(e))


def remove_chat(**kwargs):
    try:
        conn = connect_bd()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM chat WHERE id = %s" % kwargs['chat_id'])

        if cursor.rowcount != 0:
            conn.commit()
            cursor.close()
            return True
        else:
            cursor.close()
            return False

    except Exception as e:
        app.logger.error(
            'DatabaseAlerts - Não foi possivel remover registro no BD'
        )
        app.logger.error(str(e))
