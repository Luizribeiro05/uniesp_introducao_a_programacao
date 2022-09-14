'''Faça um programa que receba um número e que calcule e mostre a tabuada desse número..
'''

num = int(input("Digite um número: "))

for mult in range(1, 11):
    result = num * mult
    print(f"{num} x {mult} = {result}")
