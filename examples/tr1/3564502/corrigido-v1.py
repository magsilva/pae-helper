P.O.O. ? Programação Orientada a Objeto
18/03/03 ? Renata Pontim

Alunos:

José Arnaldo M. de Holanda		nº USP: 3564502
      Cleber Castro Hage		       nº USP: 3560345

Lista de exercícios ? Funções

EXERCÍCIO 1

def compara (x,y):
    if x>y :
        return 1
    elif x == y:
        return 0
    else:
        return ?1

RESULTADO:

compara(2,3)
-1
>>> 
compara(3,2)
1
>>> 
compara(2,2)
0

EXERCÍCIO 2

x1 = int(raw_input('Entre x1: '))
y1 = int(raw_input('Entre y1: '))
x2 = int(raw_input('Entre x2: '))
y2 = int(raw_input('Entre y2: '))

def distancia(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    dsquared = dx**2 + dy**2
    resultado = math.sqrt(dsquared)
    print resultado

distancia(x1, y1, x2, y2)

RESULTADO:

Entre x1: 4
Entre y1: 6
Entre x2: 7
Entre y2: 5
3.16227766017

EXERCÍCIO 3

def isBetween (x, y ,z):
    if (y <= x) and (x<=z) :
        return 1
    else :
        return 0

RESULTADO:

isBetween (4,5,6)
0
>>> 
isBetween(5,4,6)
1

EXERCÍCIO 4

def fibonacci(n):
    if (n==0) or (n==1):
        return 1
    else :
        return fibonacci(n-1)+ fibonacci(n-2)

def imprime(w):
    cont = 0
    while (cont <= w):
        print fibonacci (int(cont))
        cont = cont+1

RESULTADO:

imprime(7)
1
1
2
3
5
8
13
21

EXERCÍCIO 5

def inverte(palavra):
    tamanho = len(palavra)
    while (tamanho > 0):
        tamanho = tamanho -1
        print palavra[tamanho]

RESULTADO: 

inverte('Carolina')
a
n
i
l
o
r
a
C

EXERCÍCIO 6

def conta_letras(palavra, letra):
    tamanho = len(palavra)
    cont = 0
    while (tamanho >0):
        tamanho = tamanho - 1
        if (palavra[tamanho] == letra):
            cont = cont + 1
    print cont

RESULTADO:

conta_letras('palavra','a')
3

EXERCÍCIO 7

def encontra(frase,exp):
    tam_fra = len(frase)
    tam_exp = len(exp)
    i = 0
    cont = 0
    while (i < (tam_fra )):
        if (frase[i] == exp [0]):
            j = i + tam_exp
            if (frase[i : j] == exp[0 : tam_exp]):
                cont = cont + 1
        i = i + 1
    return cont

# ERRO PARCIAL 1.7: Dá erro se usado com o palavra "".

RESULTADO:

encontra('mamae comeu o almoco da maria','ma')
3

EXERCÍCIO 8

def gerador(i = 1000):
    while (i<10000):
        numero = str(i)
        num1 = int(numero[0:2])
        num2 = int(numero[2:4])
        if math.sqrt(i) == num1+num2 :
            print (i)
	i = i+1

gerador()

RESULTADO:

gerador()
2025
3025
9801

EXERCÍCIO 9

def subnumber(q,p):
    temp_q = str(q)
    temp_p = str(p)
    tam_q = len(temp_q)
    tam_p = len(temp_p)
    i = 0

# ERRO TOTAL 1.9: Não faz o solicitado no exercício.

RESULTADO:

subnumber(3456,34)
p eh subnumero de q
