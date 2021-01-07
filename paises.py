import json
import sys

import requests as rq


URL_ALL = 'https://restcountries.eu/rest/v2/all'
URL_NAME = 'https://restcountries.eu/rest/v2/name'


def requisicao(url):
    try:
        resposta = rq.get(url)
        if resposta.status_code == 200:
            return resposta.text
    except:
        print('Erro ao fazer requisção em:', url)


def parsing(resposta):
    try:
        return json.loads(resposta)
    except:
        print('Erro ao fazer parsing')


def contagem_de_paises():
    resposta = requisicao(URL_ALL)

    if resposta:
        lista_de_paises = parsing(resposta)
        if lista_de_paises:
            return len(lista_de_paises)


def listar_paises(paises):
    for pais in paises:
        print(pais['name'])


def mostar_populucao(nome_do_pais):
    resposta = requisicao('{}/{}'.format(URL_NAME, nome_do_pais))

    if resposta:
        lista_de_paises = parsing(resposta)
        if lista_de_paises:
            for pais in lista_de_paises:
                print('{}: {}'.format(pais['name'], pais['population']))
    else:
        print('País não encontrado')


def mostar_moedas(nome_do_pais):
    resposta = requisicao('{}/{}'.format(URL_NAME, nome_do_pais))

    if resposta:
        lista_de_paises = parsing(resposta)
        if lista_de_paises:
            for pais in lista_de_paises:
                print('Moedas do', pais['name'])
                moedas = pais['currencies']
                for moeda in moedas:
                    print('{} - {}'.format(moeda['name'], moeda['code']))
    else:
        print('País não encontrado')


def ler_nome_do_pais():
    try:
        nome_do_pais = sys.argv[2]
        return nome_do_pais
    except:
        print('É preciso passar o nome do país')


if __name__ == '__main__':
    if len(sys.argv) == 1:
        print('Bem-vindo ao sistema de paises')
        print('Uso: python paises.py <ação> <nome do país>')
        print('Ações disponíveis: contagem, moeda, população')
    else:
        argumento1 = sys.argv[1]

        if argumento1 == 'contagem':
            print('Existem {} paises no mundo todo'.format(contagem_de_paises()))
        elif argumento1 == 'moeda':
            pais = ler_nome_do_pais()
            if pais:
                mostar_moedas(pais)
        elif argumento1 == 'população':
            pais = ler_nome_do_pais()
            if pais:
                mostar_populucao(pais)
        else:
            print('Argumento inválido')
