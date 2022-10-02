# Q01 - [FORBELLONE, 2022] Construa um algoritmo para calcular as raízes de uma equação do 2 grau (Ax² + Bx + C), 
sendo que os valores A, B, C são fornecidos pelo usuário. (considere que a equação possui duas raizes reais).

a = int(input("Digite um valor para A: "))
b = int(input("Digite um valor para B: "))
c = int(input("Digite um valor para C: "))

d = (b**2) - (4*a*c) 

x1 = (-b-d)/(2*a) 
x2 = (-b+d)/(2*a)

print(f"X1: {x1} e x2: {x2}")
