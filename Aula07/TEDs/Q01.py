'''Problema 1 : As maçãs custam R$ 1,30 cada se forem compradas menos de uma dúzia, e R$ 1,00 se forem 
compradas pelo menos 12. Escreva um programa que leia o número de maçãs compradas, calcule e escreva o
 custo total da compra.'''


print('[ ! ]PROMOÇÃO: A partir de 12 maças,o valor de cada uma será R$ 1,00. Valor normal R$ 1,30 [ ! ]')
maçãs = int(input('Digite o número de maçãs que deseja comprar (0 pra sair do programa): '))
preço_promoção = 1.00
preço_normal = 1.30
if maçãs == 0: #Se digitado 0,encerra o programa
    print('Tchau !')
    exit(0)
elif maçãs < 0: # Caso digite um número negativo,mostra essa mensagem de "Erro"
    print(f'O número digitado é negativo: {maçãs}')
    exit(1)
elif maçãs >= 12: # Calcula o valor total incluso o valor da promoção
    total = preço_promoção * maçãs
    print(f'Você comprou {maçãs} e faz parte da promoção.Valor total: R$ {total}')
else: # Calculando com o valor normal
    total = preço_normal * maçãs
    print(f'Você comprou {maçãs} e não faz parte da promoção.Valor total: R$ {total}')    
