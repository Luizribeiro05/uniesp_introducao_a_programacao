# Use um dicionário para armazenar informações sobre uma pessoa que você conheça. 
# Armazene seu primeiro nome, o sobrenome, a idade e a cidade em que ela vive.
# Você deverá ter chaves como primeiro_nome, sobrenome, idade e cidade.
# Por fim, mostre cada informação armazenada em seu dicionário.

dados = {"primeiro_nome": "Samara", "sobrenome": "Vasconcellos", "idade": 22, "cidade": "João Pessoa"}
print(dados.keys())
print(dados.values())
print(dados.items())

for r,s in dados.items():
    print(f"A chave e o valor deste item são: {r} e {s}.")
