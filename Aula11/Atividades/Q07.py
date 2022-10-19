#Faça um algoritmo para ler dois vetores V1 e V2 de 10 números cada. Calcular e escrever a quantidade de vezes que 
#V1 e V2 possuem os mesmos números e nas mesmas posições.

from random import randint

v1 =[]
v2 =[]

for n in range(10):
    v1.append(randint(0,20))
    v2.append(randint(0,20))

print(v1)
print(v2)

for i in range(len(v1)):
     if v1[i] == v2[i]:
        print(f"O valor {v1[i]} e {v2[i]} são iguais !")
        print("Estão os dois na posição{i}")
