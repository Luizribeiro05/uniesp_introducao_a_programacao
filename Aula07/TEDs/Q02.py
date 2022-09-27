#Ler o ano atual e o ano de nascimento de uma pessoa. Escrever uma mensagem que diga se ela poderá ou não votar este ano (não é necessário considerar o mês em que a pessoa nasceu).


ano = 2022 
nascimento = int(input('Qual o seu ano de nascimento ?   '))
idade = ano - nascimento


if ano - nascimento >= 18: 
    print(f'Você tem {idade} anos de idade. Então, você pode votar')

elif  ano - nascimento > 16:
    print(f'Você tem entre 16 e 17 anos de idade. O seu Voto é facultativo')

else: 
    print(f'Você tem {idade} anos de idade. Portanto é menor de idade. Então não pode votar.')
