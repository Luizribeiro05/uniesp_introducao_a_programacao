# Q05 - Escrever um algoritmo que leia uma quantidade desconhecida de números e conte quantos deles estão nos seguintes intervalos: [0-25], [26-50], [51-75] e [76-100]. A entrada de dados deve terminar quando for lido um número negativo.

n = 1
c1 = 0
c2 = 0
c3 = 0
c4 = 0

while n > 0:
    n = int(input("Digite um número"))
    if n >= 0 and n <= 25:
        c1 = c1 + 1
    elif n >= 26 and n <= 50:
        c2 = c2 + 1
    elif n >= 51 and n <= 75:
        c3 = c3 + 1
    elif n >= 76 and n <= 100:
        c4 = c4 + 1

print(f"A quantidade de números entre 0 e 25 é: {c1}, entre votos 26-50 é: {c2}, entre votos 51-75 é: {c3}, e entre votos 76-100 é: {c3}")
