import requests
from colorama import init, Fore, Back, Style
import xmltodict
import os

# Inicia o colorama
init()

print(Back.RED + "Currency Converter" + Back.RESET)

'''
link = "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL"

req = requests.get(link)

print(req.json())'''

# Cria o dicionario para que o xml seja usado no python
def dicionario_nomes_moedas():
    moedas_arquivo = os.path.join('moedas.xml')

    with open(moedas_arquivo, 'rb') as xml_file:
        dic_moedas = xmltodict.parse(xml_file)
    moedas = dic_moedas['xml']
    return moedas

def dicionario_conversoes_disponiveis():
    conversoes_arquivo = os.path.join('conversoes.xml')

    with open(conversoes_arquivo, 'rb') as xml_file:
        dic_conversoes = xmltodict.parse(xml_file)
    conversoes = dic_conversoes['xml']
    return conversoes

# Pega o arquivo "moedas.xml" no site da awesome api e salva
def atualizar_arquivo_moedas():
    response = requests.get('https://economia.awesomeapi.com.br/xml/available/uniq')

    # Verifica se a requisição foi bem-sucedida
    if response.status_code == 200:
        # Salva o conteúdo XML em um arquivo
        with open("moedas.xml", "wb") as file:
            file.write(response.content)
        print("Arquivo salvo com sucesso.")
    else:
        print("Falha ao acessar a API. Código de status:", response.status_code)


# Atualiza o arquivo conversoes.xml
def atualizar_conversoes():
    response = requests.get('https://economia.awesomeapi.com.br/xml/available')

    # Verifica se a requisição foi bem-sucedida
    if response.status_code == 200:
        # Salva o conteúdo XML em um arquivo
        with open("conversoes.xml", "wb") as file:
            file.write(response.content)
        print("Arquivo salvo com sucesso.")
    else:
        print("Falha ao acessar a API. Código de status:", response.status_code)


# Filtra as moedas disponiveis para conversão
def filtrar_conversoes_disponiveis():
    lista = dicionario_conversoes_disponiveis()
    print(lista)

    filtro_conversoes_disponiveis = {}
    for moeda in lista:
        moeda_origem, moeda_destino = moeda.split('-')
        if moeda_origem in filtro_conversoes_disponiveis:
            filtro_conversoes_disponiveis[moeda_origem].append(moeda_destino)
        else:
            filtro_conversoes_disponiveis[moeda_origem] = [moeda_destino]
    print(filtro_conversoes_disponiveis)
    return filtro_conversoes_disponiveis


def main():
    lista_moedas_disponiveis = filtrar_conversoes_disponiveis()

    print("main", lista_moedas_disponiveis)

    for moeda in lista_moedas_disponiveis:
        print(Back.RED + moeda + Back.RESET)



if __name__ == '__main__':
    main()






