#3- Ler um vetor Q de 20 posições (aceitar somente números positivos). Escrever a seguir:
# a) O valor do maior elemento de Q e a respectiva posição que ele ocupa no vetor;
# b) O valor do menor elemento de Q e a respectiva posição que ele ocupa no vetor;

vetor = [
    10, 20, 30,
    50, 60, 5000, 70,
    3, 6, 91, 1000
]

n= vetor[0]
x = vetor[0]

for q in vetor:

    if q > n:
        n = q
    
    if q < x:
        x = q
    
    print(f'o menor valor {x} e seu indice {vetor.index(x)}')
    print(f'o maior valor {n} e seu indice {vetor.index(n)}')
