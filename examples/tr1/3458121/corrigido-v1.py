#-----------------------------------------------
#Alunos:
#           Rafael Henrique Manoel      3285310
#           Monica R. Porto Ferreira    3458121
#-----------------------------------------------


#Exercicio 1.1
def compara(x, y):
    if (x>y):
        return 1
    elif (x==y):
        return 0
    else:
        return -1

#-----------------------------------------------


#Exercicio 1.2

import math

def distancia(x1,y1,x2,y2):

    dx = x2 - x1
    dy = y2 - y1

    dsquared = dx**2 + dy**2
    result = math.sqrt(dsquared)
    return result


x1 = int(raw_input("Digite a coordenada x1: "))
y1 = int(raw_input("Digite a coordenada y1: "))
x2 = int(raw_input("Digite a coordenada x2: "))
y2 = int(raw_input("Digite a coordenada y2: "))


result = distancia(x1,y1,x2,y2)
print result

#-----------------------------------------------    

#Exercicio 1.3

def isBetween(x,y,z):
    if ( (y<=x) and (x<=z) ):
        return 1
    else:
        return 0


#-----------------------------------------------

#Exercicio 1.4

def fibonacci(n):
    if n==0 or n==1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def fibo(n):
    i=0
    while (i<n):
        print fibonacci(i),
        i=i+1
    
#-----------------------------------------------


#Exercicio 1.5

def imprime_inverso(texto):
    tam = len(texto)-1
    while (tam >= 0):
        print texto[tam]
        tam-=1

#-----------------------------------------------


#Exercicio 1.6

def abacate(texto, letra):
    return texto.count(letra)

#-----------------------------------------------


#Exercicio 1.7

def substring(texto, palavra):
    i = 0
    nrepeticoes=0
    tam = len(texto)
    while (i<tam):
        if (texto.startswith(palavra,i)):
            nrepeticoes+=1
        i+=1
    return nrepeticoes

#-----------------------------------------------


#Exercicio 1.8

def raiz(n):
    d1 = n / 100
    d2 = n%100
    if (math.sqrt(n) == d1+d2):
        print n
    
def imprima_raizes():
    xi = 1000
    while (xi<10000):
        raiz(xi)
        xi+=1

# ERRO PARCIAL 1.8: Não importou o pacote math. 
    
#-----------------------------------------------


#Exercicio 1.9

def subnumero(num, sub):
    snum = str(num)
    ssub = str(sub)
    if (abacate(snum,ssub)):
        return "eh subnumero"
    else:
        return "naum eh subnumero"

# ERRO TOTAL 1.9: Não funciona (abacate).
        
#-----------------------------------------------
