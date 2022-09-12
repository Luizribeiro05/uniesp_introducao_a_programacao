num1=float(input("Digite a nota da sua primeira avaliação: "))
num2=float(input("Digite a nota da sua segunda avaliação: "))
M=(num1+num2)/2
if M>=6:
    print(f'Você está aprovado, parabéns! Sua média é {M}')
else:
    print(f'Você está reprovado :(, sua média é {M}')    
