# Arquivo: exercicio2.py

import math

def distancia (x1, y1, x2, y2):
    dx = x2-x1
    dy = y2-y1
    dsquared = dx**2 + dy**2
    result = math.sqrt(dsquared)
    return result
x1=0.0
x2=0.0
x3=0.0
x4=0.0

x1 = input("Por favor, digite x1: ")
y1 = input("Por favor, digite y1: ")

x2 = input("Por favor, digite x2: ")
y2 = input("Por favor, digite y2: ")

resultado = distancia (x1,y1,x2,y2)
print("O resultado eh %f" % resultado)
