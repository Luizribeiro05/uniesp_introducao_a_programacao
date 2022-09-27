'''Faça um cadastro de usuários com nome, idade e email, 
utilizando apenas o que você aprendeu até agora.
'''
cadastro=[]

botao = 1000
while botao != 0:
    print("Digite 1 para cadastrar um novo usuario")
    print("Digite 2 para imprimir todos os usuarios")
    print("Digite 0 para sair")
    botao = int(input("digite a opção desejada: "))

    if botao == 1:
        nome = input("Digite o nome: ")
        idade = int(input("digite a idade: "))
        email = input("Digite o e-mail: ")
        dados = [nome,idade,email]
        cadastro.append(dados)
    
    
    elif botao == 2:
        for p in cadastro:
            print(p)
    
    elif botao == 0:
        print("Obrigado Por acessar este software !")

    else:
        print("Digite um numero válido!")
