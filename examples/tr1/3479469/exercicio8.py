# Arquivo: exercicio8.py
from math import sqrt

def separa (numero):
    parte1 = numero/100
    parte2 = numero%100
    
    if sqrt(numero) == parte1+parte2:
	print numero


for i in range (1000, 9999):
    separa(i)
