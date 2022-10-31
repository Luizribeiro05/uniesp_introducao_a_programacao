# Escreva um algoritmo que permita a leitura dos nomes de 10 clubes de futebol e armazene os nomes lidos em um vetor (lista). 
# Após isto, o algoritmo deve permitir a leitura de mais 1 nome qualquer de clube e depois escrever a mensagem ACHEI, 
# se o nome estiver entre os 10 nomes lidos anteriormente (guardados no vetor), ou NÃO ACHEI caso contrário

clubes = []
clubes.append(input("Digite o primeiro clube: "))
clubes.append(input("Digite o segundo clube: "))
clubes.append(input("Digite o terceiro clube: "))
clubes.append(input("Digite o quarto clube: "))
clubes.append(input("Digite o quinto clube: "))
clubes.append(input("Digite o sexto clube: "))
clubes.append(input("Digite o sétimo clube: "))
clubes.append(input("Digite o oitavo clube: "))
clubes.append(input("Digite o nono clube: "))
clubes.append(input("Digite o décimo clube: "))

busca = str(input("Digite o clube que deseja buscar na lista: "))

if busca in clubes:
    print(f"ACHEI! {busca} está na lista!")
else:
    print(f"NÃO ACHEI! {busca} não está na lista")
