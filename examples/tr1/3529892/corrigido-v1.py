# POO - Lista de exercicios 2 - Parte 1
# Lucas Shindi Shimo        3529892
# Marco Aurelio Roncatti    3455855


#Ex1.1
def comp(x, y) :
    if x > y :
        return 1
    elif x == y :
        return 0
    else :
        return -1

#Ex1.2
import math

def distancia () :
    x1 = int(raw_input('X1: '))
    y1 = int(raw_input('Y1: '))
    x2 = int(raw_input('X2: '))
    y2 = int(raw_input('Y2: '))

    dx = x2 - x1
    dy = y2 - y1
    dsquared = dx**2 + dy**2
    result = math.sqrt(dsquared)
    print result


#Ex1.3

def isBetween(x, y, z) :
    if ((y <= x) and (x <= z)) :
        return 1
    else :
        return 0

#Ex1.4

def fibonacci(n) :
    i_a = 1
    i_b = 1
    i = 0
    while i <= n :
        if i == 0 or i == 1 :
            print 1
        else :
            i_c = i_a + i_b
            i_a = i_b
            i_b = i_c
            print i_c
        i = i + 1
    

#Ex1.5

def inv(strg) :
    for i in range (len(strg)-1, -1, -1):
        print strg[i]

#Ex1.5.b

def inv2(strg) :
    strg2 = ""
    for i in range (len(strg)-1, -1, -1):
        strg2 = strg2 + strg[i]
    print strg2

#Ex1.6

def conta(letra, strg) :
    cont = 0
    for x in strg :
        if letra == x :
            cont = cont + 1
    return cont
        
#Ex1.7

def conta2(palavra, frase) :
    cont = 0
    for x in range (0, len(frase) - len(palavra) + 1) :
        if frase[x:][:len(palavra)] == palavra :
            cont += 1
    return cont

# ERRO PARCIAL 1.7: Conta incorretamente o caracter "".

#Ex 1.8
def prob() :
    i = 1000
    while i <= 9999 :
        p1 = int(i / 100)
        p2 = i - p1 * 100
        if math.sqrt(i) == p1 + p2 :
            print i
        i += 1

# ERRO PARCIAL 1.8: Esqueceu de importar o pacote math.

#Ex1.9
def verifica(p, q) :
    if conta2(str(p), str(q)) :
        return 1
    else :
        return 0
