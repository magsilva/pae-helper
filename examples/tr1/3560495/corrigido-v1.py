**********************************************
*                 Alunos                     * 
*      Santiago de Moura Luz 3560495         *
*    Marco Aurelio Rescia Alher 3560481      *
**********************************************



Segunda lista de POO

1-Funcoes

"1.1"
def compare(x, y):
        if x > y:
            return 1
        elif x == y:
            return 0
        else:
            return -1
    
"1.2"
import math
x1 = int(raw_input("digite o valor x1: "))
x2 = int(raw_input("digite o valor x2: "))
y1 = int(raw_input("digite o valor y1: "))
y2 = int(raw_input("digite o valor y2: "))
def distancia(x1, x2, y1, y2):
	dx = x2 - x1
	dy = y2 - y1
	dsquared = dx**2 + dy**2
	result = math.sqrt(dsquared)
	return result

# ERRO PARCIAL 1.2: Não imprime o resultado.


"1.3"
def isBetween(x, y, z):
	if y <= x and x <= z:
		return 1
	else:
		return 0

"1.4 ***"
def fibonacci(n):
	if n == 0 or n == 1:
		return 1
	else:
		return (fibonacci(n-1) + fibonacci(n-2))

# ERRO TOTAL 1.4: Não faz o solicitado.

"1.5"
def inverte(frase):
	n = len(frase)
	while n > 0:
		print (frase[n-1])
		n -= 1

"1.6"
def conta(frase, letra):
	n = frase.count(letra)
	return n

def conta2(frase, letra):
	cont = 0
	n = len(frase)
	while n > 0:
		if frase[n-1] == letra:
			cont += 1
		n -= 1
	return cont

"1.7"
def contapalavra(frase, palavra):
	cont = 0
	n = len(frase) 
	np = len(palavra) 
	n = n - np 
	while n >= 0:
		if frase[n:(n+np)] == palavra:
			cont += 1
		n -= 1
	print cont

"1.8"
import math
def mala():
	n = 9999
	while n > 1000:
		a = repr(n)
		x = int(a[0:2])
		y = int(a[2:4])
		if math.sqrt(n) == (x + y):
			print (n)
		n -= 1

	
"1.9"
import math
import string

def sub(p,q):
	if len(repr(p)) <= len(repr(q)):
		a=repr(p)
		b=repr(q)
		if string.find(b,a)<>-1:
			print("o numero ",p," eh subnumero de",q)
			#return 1
		else:
			print("o numero ",p," nao eh subnumero de",q)
			#return 0
	else:
		print("Operacao ilegal")
