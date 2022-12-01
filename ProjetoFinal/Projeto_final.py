# Projeto Final - Introdução a programação 
# Discentes: João Henrique Medeiros, Gonçalo Gabriel, Luiz Gonzaga e Sergio Tavares  
# Sistemas para Internet, P1B 

from requests import get
from json import dumps
from os import system
from sys import stderr

# Consultar API 
def consultar_api(chave,latitude,longitude):
    url = (f'https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={chave}&lang={LANG}')
    responsta = get(url)
    return responsta.json()  

# Leitura do banco de dados 
def ler_banco_dados():
    try:
        with open(BANCO_DADOS, 'r',encoding='UTF-8') as b_dados:
            dados = []
            for linha in b_dados.readlines():
                linha = linha.replace('\n','').split(SEPARADOR)
                dados.append(linha)
        return dados
    except FileNotFoundError:
        print(f'[INFO] Base de dados não encontrada, cadastre uma cidade ou crie o arquivo {BANCO_DADOS} no mesmo diretorio.',file=stderr)

# Cadastro de cidades 
def cadastrar_cidade(info):
    try:
        with open(BANCO_DADOS, 'a', encoding='UTF-8') as b_dados:
            b_dados.write(info + '\n')
        print('Cidade cadastrada')
    except Exception as msg_err:
        print(f' Ocorreu um erro: {msg_err}',file=stderr)

# Salvar/Criar arquivo 
def exportar_dados_cidade(nome_cidade,dados):
    try:
        nome_arquivo = nome_cidade + '.json'
        with open(nome_arquivo, 'w',encoding='UTF-8') as arquivo:
            dados_json = dumps(dados, indent=4)
            arquivo.write(dados_json)
    except Exception as msg_err:
        print(f' Ocorreu um erro: {msg_err}',file=stderr)

#Funcionamento do programa 

while True:
    if op <= 0 or op > 5:
        print(f' Opção inválida: {op}', file=stderr)
        break 

#1
    elif op == 1:
        print(f'\t\t  Cadastro de cidades\n')
        nome_cidade = input('[>] Digite o nome da cidade: ')
        lat = input('Digite a latitude: ')
        lon = input('Digite a longitude: ')
        dados = SEPARADOR.join([nome_cidade,lat,lon])
        cadastrar_cidade(dados)
        

#2
    elif op == 2: 
    
        print(f'\t\t  Listando cidades\n')
        dados = ler_banco_dados()
        contador = 1
        if not dado_vazio(dados):
            for info in dados:
                print(f'{contador} - {info[0]} | latitude: {info[1]} | longitude: {info[2]}')
                contador += 1

#3
    elif op == 3:
        print(f'\t\t Consultar informações da cidade (API) \n')
        dados = ler_banco_dados()
        contador = 1
        linha = 0
        if not dado_vazio(dados):
            for info in dados:
                if linha == LIMITE_CIDADE_LINHA:
                    print(' ')
                    linha = 0
                print(f'({contador}) - {info[0]}',end='  ')
                contador += 1
                linha += 1

            cidade_id = int(input('\n\n[>] Digite o número da cidade: '))
            key = input('Chave de consulta (API):')
            if cidade_id <= 0 or cidade_id > len(dados):
                print(f'[INFO] Opção inválida: {cidade_id}')
            else:
                lat = dados[cidade_id - 1][1]
                lon = dados[cidade_id - 1][2]
                cidade = dados[cidade_id - 1][0]
                dados_cidade = consultar_api(key,lat,lon)
                exportar_dados_cidade(cidade,dados_cidade)
                print(f'[+] O arquivo com as informações da cidade foi criado: {cidade}.json')
    
#4
    elif op == 4:
        print('\t\t Consultando cidades cadastradas...\n')
        key = input('Chave de consulta (API): ')
        dados = ler_banco_dados ()
        if not dado_vazio(dados):
            for info in dados:
                cidade = info[0]
                lat = info[1]
                lon = info[2]
                dados_json = consultar_api(key,lat,lon)
                exportar_dados_cidade(cidade,dados_json)
                print(f'[+] Arquivo com as informações de {cidade} criado: {cidade}.json')  
