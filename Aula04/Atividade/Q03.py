num=float(input("quantas maçãs você deseja comprar?"))
pri=1.3 or 1
if num>=12:
    pri=1*num
    print(f'O preço total é: {pri:.2f}R$')
else:
    pri=1.3*num 
    print(f'O preço total é: {pri:.2f}R$')
