------------------------------------------------------------------------
	Exercicio de POO - Segunda Lista - Funções
	Katsumi Arackawa Junior #USP:3530185
	Computação 2001
------------------------------------------------------------------------

1.1))-----------------------------------------------------------------*/
>>> def compare(x,y):
	
	if x > y:
		return 1
	elif x == y:
		return 0
	else:
            return -1
--------testando-----------
>>> compare(1,2)
-1
>>> compare(2,1)
1
>>> compare(3,3)
0


1.2))-----------------------------------------------------------------*/
import math
def distancia():
    x1=int(raw_input('Coordenada X1: '))
    y1=int(raw_input('Coordenada Y1: '))
    x2=int(raw_input('Coordenada X2: '))
    y2=int(raw_input('Coordenada Y2: '))
    dx = x2-x1
    dy = y2-y1
    dsquared = dx**2 + dy**2
    result = math.sqrt(dsquared)
    print(result)

distancia()    
----testando------
>>> distancia()
Coordenada X1: 1
Coordenada Y1: 2
Coordenada X2: 3
Coordenada Y2: 4
2.82842712475

>>> distancia()
Coordenada X1: 1
Coordenada Y1: 1
Coordenada X2: 2
Coordenada Y2: 2
1.41421356237

1.3))-----------------------------------------------------------------*/
def isBetween(x,y,z):
    if ((y<=x) and (x<=z)):
        return 1
    else :
        return 0

----Testando------
>>> isBetween(1,2,3)
0
>>> isBetween(2,1,3)
1
>>> isBetween(3,1,2)
0

1.4))-----------------------------------------------------------------*/

1,1, 2, 3, 5, 8, 13 (Sequência de Fibonacci)

def fibonacci(n):
    if n==0 or n==1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def fibonacci2(x):
    a=0
    while(a<=x):
        print(fibonacci(int(a)))
        a=a+1

----testando----
fibonacci2(3)
1
2
3
>>> 
fibonacci2(8)
1
1
2
3
5
8
13
21
34

1.5))-----------------------------------------------------------------*/
>>> def inverso():
	lista=raw_input('Digite uma String: ')
	fim=len(lista)-1
	while (fim>=0):
		print lista[fim]
		fim=fim-1
----testando-----
>>> inverso()
Digite uma String: ABACATE
E
T
A
C
A
B
A


1.6))-----------------------------------------------------------------*/
def contletra():
	lista=raw_input('Digite uma String: ')
	letra=raw_input('Digite a Letra: ')
	c=0
	cont=0
	limite=len(lista)
	while(c<limite):
		if (lista[c]==letra):
			cont=cont+1
		c=c+1
	print(cont)

-----testando------
>>> contletra()
Digite uma String: ABACATE
Digite a Letra: A
3

1.7))-----------------------------------------------------------------*/

def contpalavra():
	frase=raw_input('Digite uma FRASE: ')
	palavra=raw_input('Digite a PALAVRA DA FRASE: ')
	c=0
	cont_frase=0
	tam_palavra=len(palavra)
	tam_frase=len(frase)
	j=c+tam_palavra
	while(c<tam_frase):
                if (frase[c:j]==palavra[0:tam_palavra]):
			cont_frase=cont_frase+1
		c=c+1
		j=c+tam_palavra
	print(cont_frase)


# ERRO PARCIAL 1.7: Não conta corretamente quando a palavra é ""
-----testando-------
contpalavra()
Digite uma FRASE: ANA ANA ANA
Digite a PALAVRA DA FRASE: ANA
3
>>> contpalavra()
Digite uma FRASE: ANA FALOU COM ANA JULIA SOBRE ANA MARIA
Digite a PALAVRA DA FRASE: ANA
3


1.8))-----------------------------------------------------------------*/
import math
def algarismo():
    numero=raw_input('Digite um numero de 4 algarismos: ')
    prim=int(numero[0:2])
    ult=int(numero[2:4])
    num=int(numero)
    raiz=math.sqrt(num)
    soma=prim+ult
    if soma == raiz :
        print(num)

# ERRO TOTAL 1.8: Função não faz o requerido pelo exercício.

------testando------------
>>> algarismo()
Digite um numero de 4 algarismos: 9801
9801
>>> 

1.9))-----------------------------------------------------------------*/
def subnumero():
	p=raw_input('Digite um numero p: ')
	q=raw_input('Digite um numero q: ')
	c=0
	cont=0
	tam_p=len(p)
	tam_q=len(q)
	j=c+tam_p
	while(c<tam_q):
                if (q[c:j]==p[0:tam_p]):
			cont=cont+1
		c=c+1
		j=c+tam_p
	if cont!=0 :
		print ("Eh subnumero")
	else :
		print ("Nao eh subnumero")

------testando--------
subnumero()
Digite um numero p: 10
Digite um numero q: 10121212110
Eh subnumero
>>> subnumero()
Digite um numero p: 1111
Digite um numero q: 221212121212
Nao eh subnumero
>>> 



