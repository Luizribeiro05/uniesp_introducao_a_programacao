'''Lista de Convidados'''
convidados = ["Ronaldinho Gaúcho", "Jack Chan", "Orochi", "Lionel Messi", "Tupac Sharkur"]

'''Convite '''
for nome in convidados:
    print(f"Bora pra balada, {nome}!")

'''Quem não poderar ir '''
print("Jack Chan: Não vou !")
print("Orochi: Não vou !")

'''Modifique sua lista, substitua os desistentes por novos convidados'''

convidados[1] = "Bob"
convidados[2] = "Lula"

for nome in convidados:
    print(f"Bora pra balada, {nome}!")
