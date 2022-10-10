# Q03 - Elabore um algoritmo que leia o valor de dois números inteiros e a operacão aritimética desejada; calcule, então, a resposta adequada. Utilize os símbolos da tabela a seguir para ler qual operacão aritmética escolhida.

a = int(input("Digite um número: "))
b = int(input("Digite um outro número: "))
operação = input("Digite a operação deseja realizar (+, -, * ou /): ")

if operação == "+":
    resultado = a + b
elif operação == "-":
    resultado = a - b
elif operação == "*":
    resultado = a * b
elif operação == "/":
    resultado = a / b
else:
    print("Operação inválida!")

print(f"O resultado é {resultado}")
