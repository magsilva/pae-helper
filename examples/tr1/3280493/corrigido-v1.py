Euardo Martinelli 3342571
Eduardo Ferreira 3280493


1.1
def compare(x,y):
    if x>y: return 1
    elif x==y: return 0
    else: return ?1


1.2
import math

x = open("c:\\documents and settings\\3342571\\Desktop\\arquivo.txt")
a = int(x.readline())
b = int(x.readline())
c = int(x.readline())
d = int(x.readline())


def distancia(x1,y1,x2,y2):
    dx = x2 - x1
    dy = y2 - y1
    dsquared = dx**2 + dy**2
    result = math.sqrt(dsquared)
    return result

1.3

def isbetween(x,y,z):
    if y<=x and y<=z:
        return 1
    else:
        return 0

1.4
def fibonacci(n):
    if n==0 or n==1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


def fib(n):
    i=0
    while i<=n:
        print(fibonacci(i))
        i+=1


1.5
def inverte(valor):
    qt = len(valor)
    while qt>0:
        qt-=1
        print (valor[qt])


1.6
def conte(valor,letra):
    qt=len(valor)
    cont=0
    while qt>0:
        qt-=1
        if valor[qt]==letra :
            cont+=1
    print(cont)


1.7    
def conte(valor,letra):
    i = 0
    qt=len(valor)
    qt2 = len(letra)
    cont=0
    while i < qt:
        if valor[i]==letra[0] :
            valido = 1
            aux = 0
            while aux < (qt2 -1) :
                aux +=1
                if valor[i+aux] == letra[aux]:
                   valido = 0
            if valido == 1 :
                cont += 1
        i += 1     
    print(cont)

# ERRO TOTAL 1.7: Não funciona.

1.8
import string

retorno = 0

def algarismo(valor):
    pridez = abs(valor/100)
    segdez = valor - pridez*100   
    return pridez + segdez


def funcaoalg(valor1):
    ret = algarismo(valor1)    
    quad = (ret*ret)
    print quad
    if quad == valor1:
        print "ent"
    else:
        print "Este valor nao corresponde"
    for i in range(1000,9999):
        alg = (algarismo(i)*algarismo(i))
        if (alg == i):
            print I

# ERRO TOTAL 1.8: Não funciona: erro sintático, deveria mostrar todos os números.

 1.9

import string

def subnum(num1,num2):
    valor= str(num1)
    num = str(num2)
    for i in range(0,5):
        if valor[i]==num[0] and valor[i+1]==num[1]:
            print "Eh subnumero"

# ERRO TOTAL 1.9: Não funciona corretamente, não detecta se não é sub-número, sempre estoura os índices.
