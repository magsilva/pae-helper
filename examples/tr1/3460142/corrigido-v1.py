#Marcelo Kenji Hotta 3460142
#Jonatas Kerr de Oliveira 3457774


#1.1
def compare (a, b):
    if a > b:
	return 1
    if a == b:
	return 0
    if a < b:
	return -1 
#----------------------------------------------------
    
#1.2
import math
def distancia ():
    x1 = float(raw_input("x1: "))
    print(type(x1))
    y1 = float(raw_input("y1: "))
    print(type(y1))

    x2 = float(raw_input("x2: "))
    print(type(x2))
    y2 = float(raw_input("y2: "))
    print(type(y2))
    
    dx = x2 - x1
    dy = y2 - y1
    dsquared = dx**2 + dy**2
    result = math.sqrt(dsquared)
    return result
#----------------------------------------------------

#1.3
def isBetween (x, y, z):
    if (x >= y) and (x <=z):
	return 1
    else:
	return 0
#----------------------------------------------------

#1.4 ++++++++
def fibonacci (n):
    if n == 0 or n == 1:
	return 1
    else:
        return  fibonacci(n-1) + fibonacci(n-2)

# ERRO TOTAL 1.4: Não faz o solicitado no exercício.

#----------------------------------------------------

#1.5
def invert():
    str = raw_input("string: ")
    tam = len(str)
    while tam > 0:
	print(str[tam-1])
	tam -= 1
#----------------------------------------------------

#1.6
def conta():
    tam = 0
    count = 0
    str = raw_input("string: ")
    letra = raw_input("letra: ")
    while tam < len(str):
	if letra == str[tam]:
	    count += 1
        tam += 1
    return count
#----------------------------------------------------

#1.7
def conta2():
    count = 0
    flag = 0
    str = raw_input("string: ")
    letra = raw_input("palavra: ")
    tam = len(letra)
    while flag < len(str):
	if letra == str[flag:flag+tam]:
	    count += 1
	flag += 1
    return count

# ERRO PARCIAL 1.7: Não conta corretamente se a palavra for "".

#----------------------------------------------------

#1.8
import math

def funcao():
    num = 0
    dez1 = 0
    dez2 = 0
    while num < 10000:
	dez1 = int(num/100)
	dez2 = int(num%100)
	if math.sqrt(num) == dez1 + dez2:
	    print(num)
	num += 1

# ERRO PARCIAL 1.8: Mostra números que não deveriam ser considerados na resposta (0,1).

#----------------------------------------------------

#1.9
def subnum():
    count = 0
    flag = 0
    num1 = raw_input("Numero1: ")
    num2 = raw_input("Numero2: ")
    tam = len(str(num2))
    while flag < len(str(num1)):
	if num2 == str(num1)[flag:flag + tam]:
	    count += 1
	flag += 1
    return count

    
#----------------------------------------------------

