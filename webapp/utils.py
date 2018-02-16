#!/usr/bin/python
# encoding: iso-8859-1

import json
import requests
from webapp import app


def write_json(file, data):
    try:
        with open(file, 'w') as outfile:
            json.dump(data, outfile)
    except Exception as e:
        app.logger.error('Não foi possível gravar no arquivos json as informações desejadas.')
        app.logger.error(str(e))


def load_json(file):
    """
    :objetivo: Funcao especializada na leitura do arquivo json especificado.
    :param file: Path do arquivo json que sera lido pela aplicacao.
    :return: Dicionario com as chaves e valores do arquivo json.
    """
    try:
        with open(file) as data:
            return json.load(data)
    except Exception as e:
        print('>> Erro no parser das configurações!! - Detalhamento: ' + str(e))


def post_with_query_string(**kwargs):
    """ Realizar a chamada REST - POST via módulo requests utilizando query string.

    :usage:
            t = utils.post_with_query_string(url=url, params={'key1': int1, 'key2': value2})
            OR
            params = {
                        'key_1': value_1,
                        'key_2': 'value_2'
                    }

            t = utils.post_with_query_string(url=url, params=params)

    :param kwargs['url']: Endereço da API/ metodo POST que será consumido.
    :param kwargs['params']: params é um dicionário com chave e valor, utilizada na query string.
    :return: Retorna o objeto request com seus atributos.
    """
    try:
        if app.config['PROXY_HABILITADO']:

            proxies = {
                'http': app.config['PROXY_ADRESS'],
                'https': app.config['PROXY_ADRESS']
            }

            return requests.post(kwargs['url'],
                                 proxies=proxies,
                                 params=kwargs['params'],
                                 headers={'Content-Type': 'application/x-www-form-urlencoded'},
                                 timeout=30)
        else:
            return requests.post(kwargs['url'],
                                 params=kwargs['params'],
                                 headers={'Content-Type': 'application/x-www-form-urlencoded'},
                                 timeout=30)
    except Exception as e:
        return '[FATAL ERROR]: ' + str(e)