#exercicio 1.1

def compare (x, y):
    if x > y :
        return 1
    elif x == y :
        return 0
    else :
        return -1


#exercicio 1.2
import math

def distancia ():
    arq = open("z:/arqdados.txt")
    x1 = int(arq.readline())
    y1 = int(arq.readline())
    x2 = int(arq.readline())
    y2 = int(arq.readline())

    arq.close()
    
    dx = x2 - x1
    dy = y2 - y1
    dsquared = dx**2 + dy**2
    result = math.sqrt(dsquared)
    print result

#exercicio 1.3
def isBetween(x, y, z):
    if (y <= x) and (x <=z):
        return 1
    else :
        return 0

#exercicio 1.4
def fib (n):
    if n==0 or n==1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def fibonacci (n):
    for a in range(0, n):
        print fib(a)

#exercicio 1.5
import string

def imprime(texto):
    qtos = len(texto) - 1
    while qtos >= 0:
        print texto[qtos]
        qtos -= 1

#exercicio 1.6
import string

def conta(texto, letra):
    indice = 0
    qtos = 0
    while indice < len(texto):
        if texto[indice] == letra:
            qtos += 1
        indice += 1
    print qtos

#exercicio 1.7
import string
def qtas_vezes(frase, palavra):
    indice1 = string.find(frase, palavra)
    qtos = 0
    while indice1 != -1:
        qtos += 1
        indice1 += 1
        indice2 = string.find(frase, palavra, indice1, len(frase))
        if indice2 != -1:
            indice1 = indice2 + 1
        else :
            indice1 = indice2
    print qtos

#exercicio 1.8
import math
def numero(qual):
    pri_dezena = qual%100
    seg_dezena = (qual - pri_dezena)/100
    raiz = math.sqrt(qual)
    if raiz == (pri_dezena + seg_dezena):
        print qual

def imprime_numeros():
    for a in range(1000,9999):
        numero(a)


#exercicio 1.9
def subnumero(p,q):
    texto_p = str(p)
    texto_q = str(q)
    if len(texto_p) <= len(texto_q):
        if string.find (texto_q, texto_p) != -1:
            print "E subnumero"
            return
    print "Nao e subnumero"
