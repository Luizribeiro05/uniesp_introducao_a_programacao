qat=int(input("Qual a quantidade atual em estoque? "))
qma=int(input("Qual a quantidade máxima em estoque? "))
qmi=int(input("Qual a quantidade mínima em estoque? "))
qm=(qma+qmi)/2
print(f'A quantidade média é de: {qm}')
if qat>=qm:
    print("Não efetuar a compra!")
else:
    print("Efetuar compra!")
