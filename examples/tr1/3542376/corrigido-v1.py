#Programa feito em 18 de marco de 2003 por
#	    LUIZ CARLOS GENOVES JUNIOR <*-*> NUSP: 3542376


#este programa executa todos os exercicios da lista 2 de exercicios da disciplina
# POO SCE-213, using Python language


#################################################################################
print "\n\n FUNCOES: 1.1"

def func1():
	x = raw_input("digite x: ")
	y = raw_input("digite y: ")
	if x>y:
		return 1
	else:
		if x<y:
			return -1
		else:
			return 0
print func1()

#################################################################################
print "\n\n FUNCOES: 1.2 -> distancia entre dois pontos"

import math

def distancia():
  x1 = raw_input("digite x1: ")
  y1 = raw_input("digite y1: ")
  x2 = raw_input("digite x2: ")
  y2 = raw_input("digite y2: ")
  dx = int(x2) - int(x1)
  dy = int(y2) - int(y1)
  dsquared = dx**2 + dy**2
  result = math.sqrt(dsquared)
  print result

distancia()

#################################################################################
print "\n\n FUNCOES: 1.3"

def isBetween(x,y,z):
  if (y<=x) and (x<=z):
    return 1
  else:
    return 0

x = int(raw_input("digite x:"))
y = int(raw_input("digite y:"))
z = int(raw_input("digite z:"))

print isBetween(x,y,z)

#################################################################################

print "\n\n FUNCOES: 1.4 Fibonacci"
def fibonacci(n):
  if n==0 or n==1:
    return 1
  else:
    return fibonacci(n-1) + fibonacci(n-2)

def printfibo(n):
  for i in range(n):
    print fibonacci(i)

x = int(raw_input("digite n:"))

printfibo(x)

#################################################################################

print "\n\n FUNCOES: 1.5 inverte string"

def inverte(s):
  n = len(s) - 1
  for i in range (n+1):
    print s[n-i] + "\n"

x = raw_input("digite uma palavra:")
inverte(x)

print "\n\n FUNCOES: 1.6 conta numero de letra em string"

def ocorrencia(letra, palavra):
  return palavra.count(letra)
  
x = raw_input("digite uma palavra:")
y = raw_input("digite letra:")
print ocorrencia(y,x)

#################################################################################

print "\n\n FUNCOES: 1.7 conta sequencias de string em string"

def ocorrencia2(palavra, frase):
  return frase.count(palavra)
  
x = raw_input("digite uma frase:")
y = raw_input("digite palavra:")
print ocorrencia2(y,x)

# ERRO PARCIAL 1.7: Se a palavra for "", conta errado.

print "\n\n FUNCOES: 1.8 x**(1/2)= ab + cd"

def especialnumber():
  for i in range(1000,10000):
    root = math.sqrt(i)
    crazysum = (i/100) + (i%100)
    if (root == crazysum):
       print i

especialnumber() 
 
# ERRO PARCIAL 1.8: Esqueceu de importar o pacote "math".

#################################################################################

print "\n\n FUNCOES: 1.9 dados dois numeros, achar se existe o menor entre os algarismos do maior"

def subnumero(x,y):
  #procura x em y
  s = str(y)
  subs = str(x) 
  if s.count(subs):
    print x, ' eh subnumero de ',y

x = int(raw_input("digite um numero(maior):"))
y = int(raw_input("digite um subnumero:"))

subnumero(y,x)

#################################################################################
