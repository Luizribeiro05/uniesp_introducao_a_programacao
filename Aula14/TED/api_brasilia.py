# Selecione a Longitude e Latitude das capitais de Portugal, Espanha, Itália, França e Inglaterra;
# Crie um arquivo TXT organizando as informações: País, Capital, Logintude, Latitude (modelo abaixo);
# Seu programa deverá utilizar o arquivo como fonte de dados para consumir a API;
# Utilize uma estrutura de repetição para chamar a API até o final dos dados;
# Imprima o resultado em arquivos JSON separados, e cada um deverá conter o nome do país específico;  

# Discentes: João Henrique, Gonçalo Gabriel, Luiz Gonzaga e Sergio Tavares 
# Sistemas para internet, Uniesp introdução a programação, P1B 

from requests import get 
from json import dumps

API_KEY = input ('87ddcd5407eb23e77c015f8b1776115c')
nome_arquivo = input("base_dados") 

dados = []
with open(nome_arquivo , 'r', encoding='UTF-8') as arquivo:
    for linha in arquivo.readlines():
        linha = linha.replace('\n','').replace(' ','')
        novo_formato = linha.split(',')
        dados.append(novo_formato) 

for info in dados:    
    
    url = f'https://api.openweathermap.org/data/2.5/weather?lat={info[-15.793889]}&lon={info[-47.882778 ]}&appid={'87ddcd5407eb23e77c015f8b1776115c'} 
    resposta = get(url) 

    if resposta.status_code == 200:
        print(f'Criando arquivo: {info[0]}.json')
        with open(info[0] + '.json', 'w', encoding='UTF-8') as arquivo:
            dados_json = dumps({info[1]:resposta.json()}, indent=4) 
            arquivo.write(dados_json) 
 
