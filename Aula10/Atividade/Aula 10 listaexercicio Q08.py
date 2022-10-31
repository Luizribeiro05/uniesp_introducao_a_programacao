# Faça um algoritmo para ler um vetor de 30 números. Após isto, ler mais um número qualquer, 
# calcular e escrever quantas vezes esse número aparece no vetor.


from random import randint

v1 = []

for n in range(30):
    v1.append(randint(0, 31))

print(v1)

b1 = int(input("Digite o número que deseja buscar na lista: "))

if b1 in v1:
    print(f"O número {b1} aparece {v1.count(b1)} vezes na lista")
else:
    print(f"O número {b1} não está na lista.")
