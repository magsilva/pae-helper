1.1- escreva uma função compare que retorna 1 if x > y, 0 if x == y, and -1 if x < y.
 Resolução:

>>> def compare():
        x = 1
        y = 2
        if x == y:
            return 0 
        if x < y:
            return -1
        else:
            return 1

# chamada da função
>>> compare()

-1   # Este é o resultado da função

# ERRO PARCIAL 1.1: A função deveria receber x e y como parâmetros.


1.2- Modifique a função distancia abaixo para incluir a leitura dos dados x1, y1, x2, y2 e imprimir
     o resultado calculado.

	
>>> compare()
-1
>>> def compare1(x,y,z):
	x = input()
	y = input()
	z = input()
	print x+y+z

	
>>> compare1(0,0,0)
21
32
43
96
>>> import math
>>> def distancia(x1,y1,x2,y2):
	dx = x2 - x1
	dy = y2 - y1
	dsquared = dx * 2 + dy * 2
	result = math.sqrt(dsquared)
	return result

>>> def teste():
	print 'Entre com o valor de a : '
	a = input()
	print 'Entre com o valor de b : '
	b = input()
	print 'Entre com o valor de c : '
	c = input()
	print 'Entre com o valor de d : '
	d = input()
	print 'DISTANCIA = ',distancia(a,b,c,d)




>>> # A saída do programa
>>> teste()
Entre com o valor de a : 
5
Entre com o valor de b : 
5
Entre com o valor de c : 
10
Entre com o valor de d : 
15
DISTANCIA =  5.47722557505
>>> 
_______________________________________________________


1.3- Escreva uma função isBetween(x, y, z) que retorna 1 se y é igual a x e x menor ou igual a 
     z , caso contrario, retorna 0.


>>> def isbetween(x,y,z):
	if y <= x:
		return 1
	if x <= z:
		return 1
	else:
		return 0

	
>>> def between():
	print 'Entre com o valor de a : '
	a = input()
	print 'Entre com o valor de b : '
	b = input()
	print 'Entre com o valor de c : '
	c = input()
        print 'O RESULTADO : ',isbetween(a,b,c)

#primeiro teste        
>>> between()
Entre com o valor de a : 
5
Entre com o valor de b : 
6
Entre com o valor de c : 
5
O RESULTADO :  1

#Segundo teste
>>> between()
Entre com o valor de a : 
5
Entre com o valor de b : 
6
Entre com o valor de c : 
4
O RESULTADO :  0
>>> 

_______________________________________________________

1.4- Modifique a função abaixo para imprimir as n primeiras  linhas da sequencia de
     fibonacci. 


>>> def fibonaci(n):
	f1 = 0
	f2 = 1
	i = 1
	if n == 0 or n == 1:
	   print 1
	else:   
	   while (i <= n):
		f3 = f1 + f2
		print ' ',f3
		f1 = f2
		f2 = f3
		i += 1


		
>>> def fib():
	print 'Entre com o valor de N : '
	n = input()
	print 'Sequencia de fibonacci (',n,') : '
	fibonaci(n)

	

>>> # Resultado
>>> fib()
Entre com o valor de N : 
10
Sequencia de fibonacci ( 10 ) : 
  1
  2
  3
  5
  8
  13
  21
  34
  55
  89
>>> 

____________________________________________________________
1.5- Escreva uma função para imprimir as letras de uma dada string,
     em ordem inversa, uma letra por linha.


>>> 
>>> def Inversa():
	nome = "mamadu"
	i = len(nome)-1
	print 'O nome original eh : ',nome
	print ' '
	print 'O nome inverso eh : '
	while (i >= 0):
		print nome[i]
		i -=1

# Saída do programa
		
>>> Inversa()
O nome original eh :  mamadu
 
O nome inverso eh : 
u
d
a
m
a
m
>>> 

# ERRO PARCIAL 1.5: Era para receber a palavra como parâmetro.


1.6- Escreve uma função para que dado uma string e dada uma letra, conte quantas vezes esta letra 
     ocore na string Ex:Dado ABACATE e a letra A, o resultado será 3.



>>> def teste():
	print 'Entre com a palavra : '
	s = raw_input()
	achou = s.isalpha()
	if achou:
		print 'Palavra valida '
	else:
		print 'palavra invalida '
	if achou:
		print 'Entre com a letra para ocorencia : '
		c = raw_input()
		print 'A ocorencia da letra (',c,') ocoreu : '
		contador = s.count(c)
		print contador
	else:
		print 'Operacao invalida '

		
>>> teste()
Entre com a palavra : 
mamadu
Palavra valida 
Entre com a letra para ocorencia : 
u
A ocorencia da letra ( u ) ocoreu : 
1
>>> 

1.7- Dadas duas strings (um contendo uma frase e outro contendo uma palavra), determine
     o número de vezes que a palavra ocorre na frase. por exemplo:
     para palavra "ANA "e a frase "ANA E MARIANA GOSTAM DE BANANA", TEMOS QUE A PALAVRA OCORRE 4 VEZES NA FRASE.


>>> def frase():
	print 'Digite a frase : '
	frase1 = raw_input()
	print 'Vc digitou : ', frase1
	print ' '
	print 'Entre com uma palavra da frase para verificar as ocorencias: '
	palavra = raw_input()
	contador = frase1.count(palavra)
	print 'A palavra (',palavra,') ocorreu : [',contador,'] vezes na frase'

# ERRO PARCIAL 1.7: Não funciona com o caso de teste proposto no exercício.	

>>> frase()
Digite a frase : 
mamadu ana saliu alfa carimo ide mamadu fatumata mamadu alfa idrissa
Vc digitou :  mamadu ana saliu alfa carimo ide mamadu fatumata mamadu alfa idrissa
 
Entre com uma palavra da frase para verificar as ocorencias: 
mamadu
A palavra ( mamadu ) ocorreu : [ 3 ] vezes na frase
>>> 

1.8- Qualquer número natural de quatro algarismos pode ser dividido em duas dezenas formadas 
     pelos seus dois primeiros e dois últimos dígitos. Por exemplo:
     1297 -> 12 e 97, 5314 -> 53 e 14.Escreva uma funçào que imprime todos os milhares (4 algarismos)
     cuja raiz quadrada seja a soma das dezenas formadas pela divisão acima. Exemplo: raiz de 
  
   >>> def raiz():
	for i in range(30,100):
		num = i
		quadrado = num * num
		if (quadrado <= 10000 and quadrado >= 1000):
			print quadrado
			i +=1

# saída do programa			
>>> raiz()
1024
1089
1156
1225
1296
1369
1444
1521
1600
1681
1764
1849
1936
2025
2116
2209
2304
2401
2500
2601
2704
2809
2916
3025
3136
3249
3364
3481
3600
3721
3844
3969
4096
4225
4356
4489
4624
4761
4900
5041
5184
5329
5476
5625
5776
5929
6084
6241
6400
6561
6724
6889
7056
7225
7396
7569
7744
7921
8100
8281
8464
8649
8836
9025
9216
9409
9604
9801
>>> 

# ERRO TOTAL 1.8: Não faz o pedido pelo exercício.
__________________________________________

1.9- São dados dois números positivos p e q, sendo que o número de digitos de p é menor ou igual ao número de digitos de q.
     Verificar se p é um subnúmero de q. Exemplos: p = 23, q =57238, p é subnúmero de q, p =


>>> def teste():
	print 'Entre com o valor de p : '
	p = raw_input()
	print 'Entre com o valor de q : '
	q = raw_input()
	if len(p) <= len(q) :
	    sub = q.count(p)
	else:
		print 'O p deve ser menor que q : '
	if sub == 0:
		print p,'naum eh subnumero de ', q
	else:
		print p,'eh subnumero de ',q

# Saída do programa	
>>> teste()
Entre com o valor de p : 
12
Entre com o valor de q : 
32112
12 eh subnumero de  32112
>>> 

______________________________________________________________


                     FIM DA PRIMEIRA PARTE DO EXERCÍCIO
     
