# 4- Ler um vetor A de 10 números. Após, ler mais um número e guardar em uma variável X. 
# Armazenar em um vetor M o resultado de cada elemento de A multiplicado pelo valor X.
#  Logo após, imprimir o vetor M.

from random import randint

lista_num = []
nova_lista = []

for i in range(10):
    lista_num.append(randint(0,100))

x = randint(0,9)

for i in range(len(lista_num)):
    nova_lista.append(x * lista_num[i])

print(lista_num)
print(x)
print(nova_lista)

