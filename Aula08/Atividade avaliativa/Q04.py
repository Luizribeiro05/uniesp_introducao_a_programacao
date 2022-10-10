# Q04 - O IMC - Índice de Massa Corporal - é um critério da Organização Mundial da Saudade para indicar a condição de peso de uma pessoa. A fórmula é IMC = peso / (altura)². Elabore um algoritmo que leia o peso e a altura de uma adulto e mostre sua condição.

peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))

imc = (peso/(altura)**2)

if imc < 18.5:
    print("Você está abaixo do peso")
elif 18.5 < imc < 25:
    print("Você está com o peso normal")
elif imc > 25 and imc < 30:
    print("Você está acima do peso")
else:
    print("Você está na obesidade")
