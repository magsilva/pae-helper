# Desenvolvido por:
#                     Eduardo Carui       3458604
#                     Kaio M. Tuleski     3530056
#                                                   COMP 01



def compare(x,y):
    if x > y:
        return 1
    elif x == y:
        return 0
    else:
        return -1

#-------------------------------------------
import math

def leitura():
    a = int(raw_input("Digite x1: "))
    b = int(raw_input("Digite y1: "))
    c = int(raw_input("Digite x2: "))
    d = int(raw_input("Digite y2: "))
    result = distancia(a, b, c, d)
    return result

def distancia(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    dsquared = dx ** 2 + dy ** 2
    result = math.sqrt(dsquared)
    return result

#------------------------------------------------

def isBetween(x, y, z):
    if (y <= x) and (x <= z):
        return 1
    else:
        return 0
        
#--------------------------------------------------

def fibonacci(n): 
    if n == 0 or n == 1: 
        return 1 
    else: 
        return fibonacci(n-1) + fibonacci(n-2) 
 

def imprime(n): 
    result=[] 
    for x in range(0,n+1): 
        result.append(fibonacci(x))
        print result 

#---------------------------------------------------

def inverte():
    estringue = raw_input("Digite algo: ")
    n = len(estringue)
    n -= 1
    while n >= 0:
        print estringue[n]
        n -= 1

#-------------------------------------------------------

def contador():
    word = raw_input("Digite algo de novo: ")
    letra = raw_input("Digite a letra a ser contada: ")
    n = len(word)
    n -= 1
    contador = 0
    for i in range(0,n):
        if letra == word[i]:
            contador += 1
    return contador
    

#----------------------------------------------------------------

def conta_palavras():
    frase = raw_input("Digite uma frase: ")
    palavra = raw_input("Digite a palavra desejada: ")
    nf = len(frase) - 1
    cont = 0
    for i in range(0,nf):
	if frase.startswith(palavra,i):
	    cont += 1
    return cont

# ERRO PARCIAL 1.7: Não conta corretamente o caracter "".

#-------------------------------------------------------------------

def dezoito():
    for num in range(1000,9999):
	n = str(num)
	a = n[0]
	b = n[1]
	c = n[2]
	d = n[3]
	ab = (int(a) * 10) + int(b)
	cd = (int(c) * 10) + int(d)
	xy = ab + cd
	xysquared = xy ** 2
	if xysquared == num:
	    print num

#-----------------------------------------------------------------------

def ultimo():
    p = int(raw_input("Digite p: "))
    q = int(raw_input("Digite q: "))
    sp = str(p)
    sq = str(q)
    nq = len(sq) - 1
    cont = 0
    for i in range(0,nq):
	if sq.startswith(sp,i):
	    cont += 1
    if cont > 0:
	return 'p eh subnumero de q'
    else:
	return 'p nao eh subnumero de q'
