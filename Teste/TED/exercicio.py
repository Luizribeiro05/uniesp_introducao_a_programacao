#1- [FORBELLONE, 2022] Construa um algoritmo para calcular as raízes de uma equação do 2 grau (Ax² + Bx + C), 
# sendo que os valores A, B, C são fornecidos pelo usuário. (considere que a equação possui duas raizes reais).

from tkinter import Y


def bhaskara(a,b,c):
  delta = (b**2) - (4*a*c)
  x1 = (((-1)*b) + (delta**0.5))/(2*a)
  x2 = (((-1)*b) - (delta**0.5))/(2*a)
  if delta == 0:
    print()
    print("Nossa equação do 2º Grau: ",a,".x²",b,".x",c,"= 0")
    print("Como Delta = 0, temos um único valor de raiz (X1 = x2): ",x1)
  elif delta > 0:
    print()
    print("Nossa equação do 2º Grau: ",a,".x²",b,".x",c,"= 0")
    print("Como Delta > 0, temos dois valores distintos de raízes: ",x1,"e",x2)
  else:
    print()
    print("Nossa equação do 2º Grau: ",a,".x²",b,".x",c,"= 0")
    print("Como Delta < 0, não temos raízes reais!")
a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))
bhaskara(a,b,c)

#Programa em Python que calcula a distância entre dois pontos, dadas as suas coordenadas. 
#Considerando os pontos A(x1;y1) e B(x2;y2).

# Importando biblioteca matemática para a função de raiz quadrada
from math import sqrt

# Inserido coordenadas dos pontos
xA = float(input('Digite o valor do ponto A:'))
xB = float(input('Digite o valor do ponto B:'))

yA = float(input('Digite o valor do ponto A:'))
yB = float(input('Digite o valor do ponto B:'))

# Calculando a distância
distAB = sqrt((xA-xB)**2) + ((yA-yB)**2)

# Mostrando resultado
print('A distância entre esses dois pontos é de:', distAB, 'unidades de medida')
