1.1

def compara(x,y):
    if (x>y): return 1
    if (x==y): return 0
    if (x<y): return -1


1.2

import math
def distancia():
    x1 = input("x1:")
    y1 = input("y1:")
    x2 = input("x2:")
    y2 = input("y2:")
    dx = x2 - x1
    dy = y2 - y1
    dsquared = dx**2 + dy**2
    result = math.sqrt(dsquared)
    print result

1.3

def isBetween(x, y, z):
    if (y<=x)and(x<=z): return 1
    else: return 0

1.4

def fibonacci(n):
    if (n==0) or (n==1) : return 1
    else:
        print "fibonacci",(n-1),"+ fibonacci",(n-2)
        return fibonacci(n-1)+ fibonacci(n-2)

# ERRO TOTAL 1.4: Não faz o solicitado.

1.5

def reverso(texto):
    tamanho = len(texto)
    while(tamanho>0):
        print texto[tamanho-1]
        tamanho = tamanho - 1

1.6

def ocorrencia(texto,c):
    tamanho = 0
    contador = 0
    while(tamanho<len(texto)):
        if (texto[tamanho]==c): contador = contador + 1
        tamanho = tamanho + 1
    return contador

1.7

def conta_palavras(frase,palavra):
    return string.count(frase, palavra)

# ERRO PARCIAL 1.7: Não importou o pacote string.
# ERRO TOTAL 1.7: Não funciona (caso de teste proposto no exercício retorna 3 e deveria retornar 4).

1.8

def um_oito():
    numero = "1000"
    while(int(numero)<10000):
        dezena1 = numero[0] + numero[1]
        dezena2 = numero[2] + numero[3]
        raiz1 = int(dezena1)+int(dezena2)
        raiz2 = math.sqrt(int(numero))
        if (raiz1==raiz2): print numero
        num = int(numero)
        num = num + 1
        numero = str(num)

# ERRO PARCIAL 1.8: Não importou o pacote math.

# ERRO TOTAL 1.9: Não fez o exercício.
