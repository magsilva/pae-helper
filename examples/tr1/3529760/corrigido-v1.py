
Alunos:	Guilherme de Almeida Cordeiro	3456690		18/03/2003
	jefferson Otuka Kuramoto	3529760

[1.1]

>>> def compara(x, y):
	if x > y:
		return 1
	else:
		if x == y:
			return 0
		else:
			return -1

		
>>> compara(1,1)
0
>>> compara(0,1)
-1
>>> compara(9999,0)
1
>>> compara(1,0.1)
1
>>> compara("abacate",0)
1
>>> compara("abacate", 3845)
1

*******************************************************************

[1.2]

>>> def distancia():
	x1 = int(raw_input('Valor do x1: '))
	x2 = int(raw_input('Valor do x2: '))
	y1 = int(raw_input('Valor do y1: '))
	y2 = int(raw_input('Valor do y2: '))
	dx = x2 - x1
	dy = y2 - y1
	dsquared = dx**2 + dy**2
	result = math.sqrt(dsquared)
	print(result)

	
>>> distancia()
Valor do x1: 1
Valor do x2: 2
Valor do y1: 1
Valor do y2: 2
1.41421356237

*******************************************************************

[1.3]

>>> def isBetween(x, y, z):
	return ((x >= y) and (x <= z)) or ((x >= z) and (x <= y))

>>> isBetween(2,2,1)
1
>>> isBetween(2,3,1)
1
>>> isBetween(2,1,3)
1
>>> isBetween(1,2,3)
0
>>> isBetween("jeff","bola","canela")
0
>>> isBetween("canela","jeff", "bola")
1

*******************************************************************

[1.4]

>>> def fibo(nacci):
	if nacci == 0 or nacci == 1:
		return 1
	else:
		return fibo(nacci-1) + fibo(nacci-2)

	
>>> def fb(n):
	i = 0
	while i < n:
		print (fibo(i))
		i = i + 1

		
>>> fb(0)
>>> fb(1)
1
>>> fb(2)
1
1
>>> fb(10)
1
1
2
3
5
8
13
21
34
55

*******************************************************************

[1.5]

>>> def contacara(stri):
	tam = len(stri)
	i = tam - 1
	while i >= 0:
		print (stri[i])
		i = i - 1

		
>>> contacara('jeffe')
e
f
f
e
j

*******************************************************************

[1.6]

>>> def contacara(stri, chara):
	tam = len(stri)
	i = tam - 1
	contach = 0
	while i >= 0:
		if chara == stri[i]:
			contach = contach + 1
		i = i - 1
	return contach

>>> print (contacara("aracatuba", 'a'))
4
>>> print (contacara("xilomena", 'y'))
0

*******************************************************************

[1.7]

>>> def contastr(frase, pala):
	tam = len(frase)
	tam2 = len(pala)
	i = 0
	conta = 0
	while i <= (tam - tam2):
		j = 0
		while j < (tam2): 
			if frase[i+j] == pala[j]:
				j = j + 1
			else:
				j = tam2 +1
		if j == tam2:
			conta = conta + 1
		i = i + 1
	return conta

# ERRO PARCIAL 1.7: Não conta corretamente caracteres "".

>>> contastr("ana banana","ana")
3
>>> contastr("ana banana mariana","ana")
4
>>> contastr("a","a")
1
>>> contastr("aaa","a")
3
>>> contastr("alalal","ala")
2
>>> contastr("alalala","ala")
3
>>>

*******************************************************************

[1.8]

>>> def mil():
	m=0
	while m<10:
		c=0
		while c<10:
			d=0
			while d<10:
				u=0
				while u<10:
					num=(1000*m)+(100*c)+(10*d)+u
					pa=(10*m)+c
					pb=(10*d)+u
					if (math.sqrt(num)==pa+pb):
						print(num)
					u=u+1
				d=d+1
			c=c+1
		m=m+1


# ERRO PARCIAL 1.8: Mostra números que não deveriam ser mostrados (0,1).
		
>>> mil()
0
1
2025
3025
9801
>>> 

*******************************************************************

[1.9]

>>> def subnum():
	n1 = raw_input('Numero1: ')
	n2 = raw_input('Numero2: ')
	tam1 = len(n1)
	tam2 = len(n2)
	if tam1 < tam2:
		print("Erro. Numero1 nao pode ser menor que Numero2")
	else:	
		i = 0
		ok = 0
		conta = 0
		while i <= (tam1 - tam2):
			j = 0
			while j < (tam2): 
				if n1[i+j] == n2[j]:
					j = j + 1
				else:
					j = tam2 +1
			if j == tam2:
				ok = 1
			i = i + 1
		if ok:
			print("Eh subnumero")
		else:
			print("Nao eh subnumero")

# ERRO PARCIAL 1.9: O caso 1,11 deve ser aceito!
		
>>> subnum()
Numero1: 1
Numero2: 1
Eh subnumero
>>> subnum()
Numero1: 11
Numero2: 1
Eh subnumero
>>> subnum()
Numero1: 12
Numero2: 5
Nao eh subnumero
>>> subnum()
Numero1: 1
Numero2: 11
Erro. Numero1 nao pode ser menor que Numero2
>>> subnum()
Numero1: 12
Numero2: 12
Eh subnumero
>>> subnum()
Numero1: 12
Numero2: 21
Nao eh subnumero
>>> 
