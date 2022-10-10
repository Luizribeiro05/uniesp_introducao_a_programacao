#Use um dicionário para armazenar informações sobre uma pessoa que você 
# conheça. Armazene seu primeiro nome, o sobrenome, a idade e a cidade
#  em que ela vive. Você deverá ter chaves como primeiro_nome, sobrenome, 
# idade, e cidade. Por fim, mostre cada informação armazenada em seu dicionário.


pessoa = dict()

pessoa['nome'] = str(input('nome :'))
pessoa['sobrenome'] = str(input('sobrenome :'))
pessoa['idade'] = str(input('idade :'))
pessoa['cidade'] = str(input('cidade :'))

print(pessoa)
