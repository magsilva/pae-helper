Nome: Alexandra Kelli Barbato    nº USP: 3459053 
Nome: Ottone Alexandre Traldi    nº USP: 3457749
Nome: Marcos Fabio Martins       nº USP: 3458100

1.1
def compara (x,y):
    if (x < y):
	return -1
    elif (x == y):
	return 0
    else:
	return 1

print "Valor de x: "
x = input()
print "Valor de y: "
y = input()
print "Retorno: "
print compara (x,y)

1.2
import math

def distancia (x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    daquared = dx**2 + dy**2
    result = math.sqrt(daquared)
    return result

print "Valor x1: "
x1 = input()
print "Valor y1: "
y1 = input()
print "Valor x2: "
x2 = input ()
print "Valor y2: "
y2 = input ()
print "Distancia: "
print distancia (x1,y1,x2,y2)


1.3
def isBetween (x,y,z):
    if (y<=x and x<=z):
	return 1
    else:
	return 0

print "Valor de x: "
x = input ()
print "Valor de y:"
y = input ()
print "Valor de z: "
z = input ()
print "Resultado: "
print isBetween (x,y,z)


1.4
def fibo(n):
    i = 0
    atual = 0
    anterior = 1
    while (i<=n-1):
	temp=atual
	atual=atual + anterior
	anterior=temp
	print atual
	i = i+1
n = input("Entre com n")
fibo(n)


1.5
def inversa (str):
	i = 1 
	while (i <> len(str) + 1):
		print str[-i] 
		i = i + 1
print "entre com a string"
str = input ()
inversa(str)

1.6
def conta(str, ch):
        i = 0
	count = 0
        while (i <> len(str)):
		if (ch is str[i]):	
			count = count + 1
                i = i + 1
	print "Ocorrencias = "
	print count
	return 0
print "entre com a string"
str = input ()
print "entre com a letra"
ch = input ()
conta(str, ch)


1.7
print "entre com a 1 string"
str1 = input ()
print "entre com a 2 string"
str2 = input ()
print str1.count(str2)

# ERRO PARCIAL 1.7: Não é uma função.
# ERRO PARCIAL 1.7: Não conta corretamente (ver banana,ana).
# ERRO PARCIAL 1.7: Não conta corretamente o caracter "".

1.8
import math

def parte1 (x):
    return int (x/100)

def parte2 (x):
    return (x - parte1(x)*100)

i = 1000
while (i <= 9999):
    if ((parte1(i) + parte2(i)) == math.sqrt(i)):
	print i
	print "\n"
    i = i+1

# ERRO PARCIAL 1.8: Não é a função que faz o cálculo.

1.9
num1 = raw_input ("entre com o 1 numero")
num2 = raw_input ("entre com o 2 numero")
if (num1.count(num2) <> 0):
    print "Numero 2 e sub numero de Numero 1"

# ERRO TOTAL 1.9: Não funciona.
