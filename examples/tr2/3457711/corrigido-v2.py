#!/usr/bin/python
#alunos: Breno Leitao  3457711
#        Jonatas Oliveira 3457774

class inte:
	def __init__(self):
		self.lista = []

# ERRO 1 2 Na operação de união (a primeira definida), pode adicionar objetos que não são inteiros.
# ERRO 1 5
# ERRO 1 6
# ERRO 1 7

	def add(self,x):
		if x not in self.lista:
			self.lista.append(int(x))

	def remove(self, numero):
		if numero in self.lista:
			del self.lista[self.lista.index(numero)]		

	def imprime(self):
		print  "lista: ", self.lista 

	def uniao(self, classe):
		for x in classe.lista: 
			if x not in self.lista:
				self.lista.append(x)

	def interseccao(self, classe):
		for x in self.lista:
			if x not in classe.lista:
				self.remove(x)

	def uniao(self, classe):
		for x in classe.lista:
			if x not in self.lista:
				self.add(x)
			



a = inte()
a.add(2)
a.add(4)
b = inte()
b.add(3)
b.add(4)
#a.interseccao(b)
a.uniao(b)
a.imprime()

#!/usr/bin/python
#alunos: Breno Leitao 3457711 Jonatas Kerr 3457774
import string

# ERRO 2 25
# ERRO 2 23

def verifica_tag(linha):
	erro = 0
	tags = 0;
	fecha = 0
	for i in range(0,len(linha)):
		if (linha[i] == "<") and (fecha != 1): # <Hello>
			fecha = 1
		if (linha[i] == ">") and (fecha != 1): # <>>
			erro +=1;
			fecha = 0;
		if (linha[i] == ">") and (fecha == 1): #Situacao perfeita
			fecha = 0;
			tags +=1;
		if (linha[i] == "<") and (fecha == 1): # <body<title> 
			erro +=1;
			
			

	return [erro-tags, tags]  #Eis a carta na manga

member = []
file = open("file.tag","r")
i = 0;
while 1: 
	i +=1;
	text = file.readline()
	if text == "":
		break 
	lista_palavras = string.split(text," ") 
 	lista_tags = string.split(text, "<")	
	lista_tags = lista_tags[1:]
	Socatres = verifica_tag(text);
#	if string.count(text, '<') == string.count(text, '>'):
#		print "Tags perfeitas" 
#	else:
#		print "Tags com problemas" 

	print "linha " , i , " com ", len(lista_palavras) , " palavras ", Socatres[1], "tags e", Socatres[0], " erros"  

	verifica_tag(text)

