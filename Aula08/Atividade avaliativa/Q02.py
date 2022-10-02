# Q02 -[FORBELLONE, 2022] Construa um algoritmo que, tendo como dados de entrada dois pontos quaisquer do plano,
 P(x1, y1) e Q(x2, y2), imprima a distância entre eles. A formulá que efetua tal cálculo é: d = (x2 - x1)2 + (y2 - y1)2

x1 = int(input("Digite uma valor para x1: "))
x2 = int(input("Digite uma valor para x2: "))
y1 = int(input("Digite uma valor para y1: "))
y2 = int(input("Digite uma valor para y2: "))

d = ((x2-x1)*(x2-x1)+(y2-y1)*(y2-y1))**(0.5)

print(f"A distância entre os pontos é {d}")
