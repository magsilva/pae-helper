NOME: Mamadú bubacar Da Silva baldé
NÚMERO- USP : 3538162

# ERRO 1 6
# ERRO 1 7
# ERRO 1 2
# ERRO 1 4
# ERRO 1 12
                

2- CLASSE

>>> class ConjuntoInteiros:
	def __init__(self):
		self.x = []
		self.tecla = 0
	def Insere(self,item):
		self.x.append(item)
		print 'O item foi inserido com sucesso '
		print 'Tecle um numero enseguida ENTER '
		self.tecla = input()
	def Remove(self,item):
		self.x.remove(item)
		print 'O item foi removido com sucesso '
		print 'Tecle um numero enseguida ENTER '
		self.tecla = input()
	def Imprime(self):
		print 'A lista : ',self.x
        	print 'Tecle um numero em seguida tecle ENTER '
        	self.tecla = input()
        def Uniao(self,lista):
		self.x.extend(lista)
		print 'Uniao de duas listas com sucesso '
		print 'Tecle um numero enseguida tecle ENTER '
		self.tecla = input()
	def Interseccao(self,lista):
		self.x.extend(lista)
		self.x.sort()
		print 'Interseccao com sucesso '
		print 'Tecle um numero enseguida ENTER '
		self.tecla = input()
	def Subtracao(self,lista):
		contador = 0
		i = 0
		while (i < len(lista)):
			contador = self.x.count(lista[i])
			if (contador != 0):
			      self.x.remove(lista[i])
			      i +=1
			else:
				i +=1
		print 'O processo terminou com sucesso '
		print 'tecle um numero enseguida ENTER '
		self.tecla = input()
	def Imprime(self):
		print 'LISTA : ', self.x

		
>>> def Menu():
	print 'MENU : '
	print '************************'
	print '1- Inserir um elemento na lista '
	print '2- Remover um elemento na lista '
	print '3- Unificar duas listas '
	print '4- Interseccao de duas listas '
	print '5- Subtracao da lista '
	print '6- Imprimir a lista '
	print '7- Sair do programa '
	print '**************************'
	print '    '
	print 'Entre com uma opcao do menu : '
	opcao = input()
	return opcao

>>> def principal1():
	a = ConjuntoInteiros()
	opcao = 0
	while (opcao != 7):
		opcao = Menu()
		if (opcao == 1):
			print 'Entre com um numero inteiro para inserir '
			item = input()
			a.Insere(item)
		if (opcao == 2):
			print 'Entre com um numero inteiro para remover '
			item = input()
			a.Remove(item)
		if (opcao == 3):
			print 'Entre com numro N para quantidade elemento'
			n = input()
			i = 0
			lista = []
			while (i < n):
				print 'Entre com elemento ',i
				item = input()
				lista.append(item)
				i +=1
			a.Uniao(lista)	
		if (opcao == 4):
			a.Interseccao(lista)
		if (opcao == 5):
			a.Subtracao(lista)
		if (opcao == 6):
			a.Imprime()
                        print 'Tecle um numero para voltar ao menu ou 7-> sair'
                        tecla = input()


 # SAIDA DO PROGRAMA
                   
>>> principal()
MENU : 
  
1- Insere um elemento 
2- Remove elemento da lista 
3- Imprime a lista 
4- Sair do programa 
****************************
Entre com uma opcao do menu : 
3
Entre com numro N para quantidade elemento
4
Entre com elemento  0
12
Entre com elemento  1
13
Entre com elemento  2
14
Entre com elemento  3
15
Uniao de duas listas com sucesso 
Tecle um numero enseguida tecle ENTER 
1
MENU : 
  
1- Insere um elemento 
2- Remove elemento da lista 
3- Imprime a lista 
4- Sair do programa 
****************************
Entre com uma opcao do menu : 

Traceback (most recent call last):
  File "<pyshell#171>", line 1, in ?
    principal()
  File "<pyshell#160>", line 5, in principal
    opcao = menu()
  File "<pyshell#31>", line 11, in menu
    opcao = input()
  File "<string>", line 0
    
    ^
SyntaxError: unexpected EOF while parsing
>>> principal1()
MENU : 
************************
1- Inserir um elemento na lista 
2- Remover um elemento na lista 
3- Unificar duas listas 
4- Interseccao de duas listas 
5- Subtracao da lista 
6- Imprimir a lista 
7- Sair do programa 
**************************
    
Entre com uma opcao do menu : 
3
Entre com numro N para quantidade elemento
3
Entre com elemento  0
12
Entre com elemento  1
13
Entre com elemento  2
14
Uniao de duas listas com sucesso 
Tecle um numero enseguida tecle ENTER 
1
MENU : 
************************
1- Inserir um elemento na lista 
2- Remover um elemento na lista 
3- Unificar duas listas 
4- Interseccao de duas listas 
5- Subtracao da lista 
6- Imprimir a lista 
7- Sair do programa 
**************************
    
Entre com uma opcao do menu : 
4
Interseccao com sucesso 
Tecle um numero enseguida ENTER 
1
MENU : 
************************
1- Inserir um elemento na lista 
2- Remover um elemento na lista 
3- Unificar duas listas 
4- Interseccao de duas listas 
5- Subtracao da lista 
6- Imprimir a lista 
7- Sair do programa 
**************************
    
Entre com uma opcao do menu : 
6
LISTA :  [12, 12, 13, 13, 14, 14]
Tecle um numero para voltar ao menu ou 7-> sair
1
MENU : 
************************
1- Inserir um elemento na lista 
2- Remover um elemento na lista 
3- Unificar duas listas 
4- Interseccao de duas listas 
5- Subtracao da lista 
6- Imprimir a lista 
7- Sair do programa 
**************************
    
Entre com uma opcao do menu : 
5
O processo terminou com sucesso 
tecle um numero enseguida ENTER 
1
MENU : 
************************
1- Inserir um elemento na lista 
2- Remover um elemento na lista 
3- Unificar duas listas 
4- Interseccao de duas listas 
5- Subtracao da lista 
6- Imprimir a lista 
7- Sair do programa 
**************************
    
Entre com uma opcao do menu : 
6
LISTA :  [12, 13, 14]
Tecle um numero para voltar ao menu ou 7-> sair
1
MENU : 
************************
1- Inserir um elemento na lista 
2- Remover um elemento na lista 
3- Unificar duas listas 
4- Interseccao de duas listas 
5- Subtracao da lista 
6- Imprimir a lista 
7- Sair do programa 
**************************
>>> nome: Mamadú Bubacar Da Silva Baldé
Número usp : 3538162

exercícios : 2- Classes


                

Python 2.2.2 (#37, Oct 14 2002, 17:02:34) [MSC 32 bit (Intel)] on win32
Type "copyright", "credits" or "license" for more information.
IDLE 0.8 -- press F1 for help
>>> 
>>> class frases:
	def __init__(self,num):
		self.countline = num
	"funcao que retorna umm lista de linhas"	
	def Numline(self):
		return self.countline


	
>>> class palavras:
	def __init__(self,num):
		self.countline = num
		self.countword = []
        def Numword(self):
		f = open("mamadu.txt", "r")
		tamlinha = len(self.countline)
		i = 1
		while (i <= tamlinha):
			linha = f.readline()
			k = len(linha)-1
			j = 0
			count = 0
			while (j < len(linha)):
				if ((" "==linha[j]) or (linha[j]==linha[k])):
					count +=1 
				j +=1
			self.countword.append(count) 
			i +=1
		f.close()
		return self.countword

	
>>> class tags:
	def __init__(self,num):
		self.countline = num
		self.countags = []
		self.countproblema = []
        def Numprob(self):
		f = open("mamadu.txt", "r")
		c1 = 0
		c2 = 0
		tamlinha = len(self.countline)
		i =1
		while (i <= tamlinha):
			num = 0
			linha = f.readline()
			c1=linha.count("<")
			c2=linha.count(">")
			num = c1 - c2
			if num < 0:
				num *=-1
			else:
				num *=1 
			self.countproblema.append(num)
			i +=1
		f.close()
		return self.countproblema
	def Numtags(self):
		f = open("mamadu.txt", "r")
		tamlinha = len(self.countline)
		i = 1
		while (i <= tamlinha):
			feito = 0
			contador = 0
			c1 = 0
			c2 = 0
			linha = f.readline()
			final = len(linha)-1
			j = 0
			k = -1
			c = 0
			while (feito != 1):
				if ((" "==linha[j]) or (linha[j]==linha[final])):
					c1 = 0
					c2 = 0
					c = k+1
					k = j
					palavra = linha[c:k]
					c1=palavra.count("<")
					c2=palavra.count(">")
					if ((c1 == 1) and (c2==1)):
						contador +=1
					else:
						contador *=1 
					if (linha[j]==linha[final]):
						feito = 1
					else:
						feito = 0
						j +=1
				else:
					feito = 0
					j +=1
			i +=1
			self.countags.append(contador)
		f.close()	
		return self.countags

	
>>> class paltags:
	def __init__(self,num):
		self.countline = num
		self.paltags = []
	def Numpaltags(self):
		f = open("mamadu.txt", "r")
		i = 1
		tamlinha = len(self.countline)
		while (i <= tamlinha):
			countags = []
			linha = f.readline()
			final = len(linha)-1
			feito = 0
			j = 0
			k = -1
			c = 0
			while (feito != 1):
				
				if ((" "==linha[j]) or (linha[j]==linha[final])):
					c1 = 0
					c2 = 0
					c=k + 1
					k = j
					palavra = linha[c:k]
					c1 = palavra.count("<")
					c2 = palavra.count(">")
					if ((c1==1) and (c2==1)):
						countags.append(palavra)
					else:
						" nao eh tags "
					if (linha[j]==linha[final]):
						feito = 1
					else:
						feitp = 0
						j +=1
				else:
					j +=1
			self.paltags.append(countags)
			i +=1
		f.close()
		return self.paltags

	
>>> def menu():
	print "MENU : "
	print "                                  "
	print "**********************************"
	print "*1- Iniciar o programa           *"
	print "*2- processar as frases          *"
	print "*3- Sair do programa             *"
	print "**********************************"
	print "                                  "
	print "Digite a opcao do menu            : ",
	opcao = input()
	return opcao

>>> def principal():
	op = 0
	linha = []
	opcao = 0
	numline = []
	numword = []
	numprobtags = []
	numtags = []
	paltag = []
	
	while (opcao != 3):
		opcao = menu()
	        if (opcao==1):
			op = 1
                        f = open("mamadu.txt", "w")	
                	print "Entre numero de frases : ",
		        n = input()
		        i = 1
		        while (i <= n):
				
				print "Digite a frase [",i,"] : ",
			        frase = raw_input()
			        linha.append(i)
			        print >>f,frase
			        i +=1
		f.close()
	        if (opcao == 2):
			if (op==0):
				print "escolhe primeiro a opcao numero 1 "
				print "Tecle uma tecla enseguida ENTER e tente novamente : ",
				c = raw_input()
			else:
				a = frases(linha)
				numline = a.Numline()
				b = palavras(linha)
				numword = b.Numword()
				c = tags(linha)
				numtags = c.Numtags()
				numprobtags=c.Numprob()
				d = paltags(linha)
				paltag = d.Numpaltags()
				#f = open("processamento.txt", "w")
				#print >>f,"arq saida : "
				i = 0
				tamlinha = len(linha)
				while (i < tamlinha):
					print "linha : ",numline[i],
					print " -- ",numword[i],"palavras -- ",
					print numtags[i]," ","tags (",paltag[i],") -- ",numprobtags[i]," -- problemas"
					i +=1
				print "        "	
				print "tecle uma tecla para voltar ao menu ",
				tecla = raw_input()
def principal():
	op = 0
	linha = []
	opcao = 0
	numline = []
	numword = []
	numprobtags = []
	numtags = []
	paltag = []
	
	while (opcao != 3):
		opcao = menu()
	        if (opcao==1):
			op = 1
                        f = open("mamadu.txt", "w")	
                	print "Entre numero de frases : ",
		        n = input()
		        i = 1
		        while (i <= n):
				
				print "Digite a frase [",i,"] : ",
			        frase = raw_input()
			        linha.append(i)
			        print >>f,frase
			        i +=1
		f.close()
	        if (opcao == 2):
			if (op==0):
				print "escolhe primeiro a opcao numero 1 "
				print "Tecle uma tecla enseguida ENTER e tente novamente : ",
				c = raw_input()
			else:
				a = frases(linha)
				numline = a.Numline()
				b = palavras(linha)
				numword = b.Numword()
				c = tags(linha)
				numtags = c.Numtags()
				numprobtags=c.Numprob()
				d = paltags(linha)
				paltag = d.Numpaltags()
				f = open("processamento.txt", "w")
				print >>f,"arq saida : "
				i = 0
				tamlinha = len(linha)
				while (i < tamlinha):
					print >>f,"linha : ",numline[i],
					print >>f," -- ",numword[i],"palavras -- ",
					print >>f,numtags[i]," ","tags (",paltag[i],") -- ",numprobtags[i]," -- problemas"
					i +=1
				print "        "
				f.close()
				print "tecle uma tecla para voltar ao menu ",
				tecla = raw_input()



Exemplo de execussao :


MENU : 
                                  
**********************************
*1- Iniciar o programa           *
*2- processar as frases          *
*3- Sair do programa             *
**********************************
                                  
Digite a opcao do menu            : 




OBSERVAÇÃO : O ultimo caracter de cada palavra nau deve ser igual com o ultimo caracter da ultima palavra.				

# ERRO 2 23
