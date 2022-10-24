# Use um dicionário para armazenar os números favoritos de algumas pessoas.
# Escolha cinco colegas, e pergunte quais seus números favoritos.
# Use seus nomes para serem as chaves de cada número favorito. 
# Ao final, exiba o nome de cada pessoa e seu número favorito.

nprefer = {"Gabriel": 24, "Luiz": 42, "Andre": 12, "Roberto": 69, "Matuê": 20}

for r,s in nprefer.items():
    print(f'O número preferido de {r} é {s}.')
