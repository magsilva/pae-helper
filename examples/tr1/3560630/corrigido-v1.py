Lista de Exercício 2 de POO

Alunos:
João Paulo Scardua Coelho	3560630
Alexandre Lucas 		3541980
--------------------------------------------------------------------------------------------------------------


Exercício 1

def compare(x,y):
    a = -1
    if x > y:
        a = 1
    elif x == y:
        a = 0
    return a

Exercício 2

Arquivo texto utilizado no exercício 2

4
0
0
3

import math
def distancia():
    f = open("C:\Python\distancia.txt")
    linha = f.readline()
    l = []  #[x1,y1,x2,y2]
    while linha:
        l.append(int(linha))
        linha = f.readline()
    f.close()
    dx = l[2] - l[0]
    dy = l[3] - l[1]
    dsquared = dx**2 + dy**2
    result = math.sqrt(dsquared)
    print result
distancia()

Resultado : 5.0



Exercício 3

def isBetween(x,y,z):
    if y <= x and x <= z:
        return 1
    else:
        return 0
isBetween(2,4,3)

Resultado: 0

Exercício 4

def fibonacci(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def imprime_fibonacci(valor):
    i = 0
    while i <= valor:
        print fibonacci(i)
        i +=1

imprime_fibonacci(7)

Resultado:

1
1
2
3
5
8
13
21

Exercício 5

Neste exercício foi utilizado o arquivo string.txt abaixo:

otejbo a oacatneiro

def inverte_string():
    f = open("c:\Python\string.txt")
    s = f.readline()
    l = str(s)
    tam = len(l) - 1
    while tam >= 0:
        print l[tam]
        tam -=1
inverte_string()

Resultado: 

o
r
i
e
n
t
a
c
a
o

a

o
b
j
e
t
o

Exercício 6

def conta_ocorrencia(s,c):
    tam = len(s)
    i = 0
    cont = 0
    while i < tam:
        if s[i] == c:
            cont +=1
        i +=1
    print cont
conta_ocorrencia('PARALELEPIPEDO', 'P')

Resultado: 3

Exercício 7

def conta_ocorrencia2(frase,palavra):
    l1 = len(frase)
    l2 = len(palavra)    
    i = 0
    cont = 0
    while i < l1:
        if palavra == frase[i: i + l2]:
            cont +=1
        i +=1
    print cont
conta_ocorrencia2('ana e mariana gostam de banana', 'ana')

# ERRO PARCIAL 1.7: Não conta corretamente se a palavra sendo procurada for "".

Resultado: 4

# ERRO TOTAL 1.8: Não foi feito o exercício.

Exercício 9

def subnumero(num1,num2):
    s1 = str(num1)
    s2 = str(num2)
    l1 = len(s1)
    l2 = len(s2)    
    i = 0
    ret = 0
    while i < l2:
        if s1 == s2[i: i + l1]:
            ret = 1
        i +=1
    print ret
subnumero(34,4534)

Resultado: 1
