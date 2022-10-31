#Crie um vetor N que seja resultado da soma dos itens de outros dois vetores A e B.
#  Exemplo: A[0] + B[0] deverá ser salva em N[0].

a = [10, 20, 30, 40, 50]
b = [1, 2, 3, 4, 5]
n = []

for i in range(len(a)):
    n.append(a[i] + b[i])

print(n)
