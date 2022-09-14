'''Crie uma lista de convidados para um jantar em sua casa, com pelo menos 5 celebridades.
'''

lista_celebridades = ["Ronaldinho Gaúcho", "Jack Chan", "Orochi", "Lionel Messi", "Tupac Sharkur"]

'''Envie um convite para cada uma dessas pessoas. Com a mesma mensagem e nome personalizado.
'''

for nome in lista_celebridades:
    print(f"{nome},Convite para festa no Local : Hotel California,420.Domingo,04/02, às 22 horas")

'''Sabendo que uma dessas pessoas não poderá ir ao seu jantar, você deverá enviar novos convites. Imprima o nome das pessoas que não poderão comparecer.
'''

print("Jack Chan e Orochi não poderão ir ao jantar")

'''Modifique sua lista, substitua os desistentes por novos convidados.
'''

nova_lista_celebridades = ["Ronaldinho Gaúcho", "Eminem", "Bruce Lee", "Lionel Messi", "Tupac Sharkur"]

'''Exiba um novo convite para cada pessoa que continua presente em sua lista.
'''

for nome in nova_lista_celebridades:
    print(f"{nome},Convite para festa no Local : Hotel California,420.Domingo,04/02, às 22 horas")
