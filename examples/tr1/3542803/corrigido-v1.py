1.1

def compare(x, y):
    if (x > y): return 1
    if (x < y): return -1
    return 0

Exerc�cio 1.2

import math

def distancia():
    x1 = int(raw_input("Digite o valor de X1: "))
    y1 = int(raw_input("Digite o valor de Y1: "))
    x2 = int(raw_input("Digite o valor de X2: "))
    y2 = int(raw_input("Digite o valor de Y2: "))
    dx = x2 - x1
    dy = y2 - y1
    dsquared = dx**2 + dy**2
    result = math.sqrt(dsquared)
    print("O valor da distancia eh %f" % result)


Exerc�cio 1.3
-------------

def isBetween(x, y, z):
    if (y <= x) and (x <= z): return 1
    return 0


Exerc�cio 1.4
-------------

Use a fun��o f(n) para exibir a resposta:

def fibonacci(n):
    if (n == 0) or (n == 1):
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def f(n):
    i = 0
    while(i < n):
        i = i + 1
        print fibonacci(i)


Exerc�cio 1.5
-------------

def strinv(s):
    i = len(s) - 1
    while i >= 0:
        print s[i]
        i = i - 1


Exerc�cio 1.6
-------------

def instr(s, c):
    i = len(s) - 1
    x = 0
    while i >= 0:
        if (s[i] == c): x = x + 1
        i = i - 1
    return x


Exerc�cio 1.7
-------------

def isinstr(s, q):
    i = len(s) - len(q)
    x = 0
    while i >= 0:
        if (s[i : i + len(q)] == q): x = x + 1
        i = i - 1
    return x

# ERRO PARCIAL 1.7: N�o conta corretamente se o caracter for "".

Exerc�cio 1.8
-------------

import math

def mucholoco():
    i = 1000
    while (i < 10000):
        s = str(i)
        i1 = int(s[0:2])
        i2 = int(s[2:4])
        if (math.sqrt(i) == (i1 + i2)):
            print "raiz de %d = %d + %d = %d" % (i, i1, i2, math.sqrt(i))
        i = i + 1


Exerc�cio 1.9
-------------

Usando a fun��o isinistr dada no exerc�cio 1.7:

def isinint(p, q):
    x = isinstr(str(q), str(p))
    if (x > 0):
        print "%d eh um subnumero de %d" % (p, q)
    else:
        print "%d nao eh um subnumero de %d" % (p, q)
