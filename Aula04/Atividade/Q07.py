nc=int(input("Digite o número da sua conta: "))
s=float(input("Digite o seu saldo: "))
d=float(input("Digite o débito da sua conta: "))
c=float(input("Digite o crédito da sua conta: "))
sat=s-d+c
print(f'Seu saldo atual é de: {sat:.2f}R$')
if sat>=0:
    print("Saldo positivo!")
else:
    print("saldo negativo!")
