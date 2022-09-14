'''Faça um cadastro de usuários com nome, idade e email, utilizando apenas o que você aprendeu até agora.
'''


nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
email = input("Digite seu email: ")

pessoa = nome, idade, email

lista = [pessoa]

for pessoa in lista:
    print(f"Nome:{nome}, idade:{idade}, email:{email}. Inscrição bem sucedida.")
