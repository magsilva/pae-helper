Programa��o Orientada a Objetos
2� Lista de exerc�cios

Lucas Antiqueira
Marcus Secato

1 - Fun��es

1.1
C�digo da fun��o compare:

def compare(x,y):
    if x > y:
        return 1
    if x == y:
        return 0
    if x < y:
        return -1

Testes da fun��o:

>>>
compare(32,76)
-1
>>> compare(10,2)
1
>>> compare(-1,-1)
0
>>> compare("eu","tu")
-1
>>> compare("pilha","pira")
-1
>>> compare("xena","xana")
1
>>> compare("seis","seis")
0


1.2
C�digo da fun��o distancia:

import math
def distancia():
    x1 = int (raw_input('Coordenas x do ponto 1: '))
    y1 = int (raw_input('Coordenas y do ponto 1: '))
    x2 = int (raw_input('Coordenas x do ponto 2: '))
    y2 = int (raw_input('Coordenas y do ponto 2: '))
    dx = x2-x1
    dy = y2-y1
    dsquare = dx**2 + dy**2
    result = math.sqrt(dsquare)
    print result 

Teste da fun��o distancia:

distancia()
Coordenas x do ponto 1: 3
Coordenas y do ponto 1: 4
Coordenas x do ponto 2: 7
Coordenas y do ponto 2: 9
6.4031242374328485
>>> distancia()
Coordenas x do ponto 1: 1
Coordenas y do ponto 1: 1
Coordenas x do ponto 2: 3
Coordenas y do ponto 2: 4
3.6055512754639891
>>> distancia()
Coordenas x do ponto 1: 0
Coordenas y do ponto 1: 0
Coordenas x do ponto 2: 3
Coordenas y do ponto 2: 4
5.0

1.3
C�digo da fun��o isBetween:

def isBetween(x,y,z):
    return y <= x <= z

Testes da fun��o isBetween:

>>> 
isBetween(2,0,5)
1
>>> isBetween(4,6,9)
0


1.4
C�digo das fun��es utilizadas neste exerc�cio:

def fibonacci(n):
    if n == 0 or n ==1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def sequencia(n,i=0):
    while i <= n:
        print fibonacci(i)
        i=i+1

Teste das fun��o:

>>> sequencia(9)
1
1
2
3
5
8
13
21
34
55


1.5
C�digo da fun��o imprime:

def imprime(word):
    word2 = list (word)
    word2.reverse()
    for i in word2:
	print i

Teste da fun��o:

imprime("truco")
o
c
u
r
t





1.6
C�digo da fun��o conta:

def conta(palavra, letra, i=0, cont=0):
    while i < len(palavra):
	if palavra[i] == letra:
	    cont=cont+1
	i=i+1
    return cont

Testes da fun��o:

conta("abacate","a")
3
>>> conta("araraquara","a")
5


1.7
C�digo da fun��o conta2:

def conta2(frase,palavra, i=0,cont=0):
    while i < len(frase):
	if frase[i:i+len(palavra)] == palavra:
	    cont=cont+1
	i=i+1
    return cont

Teste da fun��o conta2:

>>> conta2("Renata viajou na nave nacional ","na")
5


1.8
C�digo da fun��o milhares:

def milhares(i=1000):
    while (i < 10000):
	lista = str(i)
	num1 = int(lista[0:2])
	num2 = int(lista[2:])
	if math.sqrt(i) == num1 + num2:
	    print i
	i = i + 1


Teste da fun��o milhares:

>>> milhares()
2025
3025
9801


1.9
C�digo da fun��o subnumero:

def subnumero(p, q):
    ps = str(p)
    qs = str(q)
    if len(ps) <= len(qs):
	if conta2(qs, ps):
	    return 1
	else:
	    return 0
    else:
	return 0


Teste da fun��o subnumero:

>>> subnumero(23, 57238)
1
>>> subnumero(25, 57238)
0
>>> subnumero(57, 57238)
1
