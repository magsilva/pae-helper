import copy
class ConjuntoInteiros:
# ERRO 1 2
# ERRO 1 7
	def __init__(self, l):
		self.lista = []
		tmp = copy.deepcopy(l)
		for i in l:
			count = 0
			for j in tmp:
				if i is j:
					count += 1
			if count > 1:
				print "Objeto com mais de uma referencia"
				return
		self.lista = l
	def __add__(self, e):
		if type(e) == type(1):
			self.lista.append(e)
		else:
			print "Tipo Invalido"
			return
		count = 0
		for i in self.lista:
			if i is e:
				count += 1
		if count > 1:
			print "Objeto Existente"
			return
	def __sub__(self, e):
		count = 0
		for i in self.lista:
			if i == e:
				count += 1
		if count == 0:
			print "Objeto nao existe"
			return
		self.lista.remove(e)
	def uniao(self, conj):
		tmp = []
		for i in conj.lista:
			if self.lista.count(i) == 0:
				tmp.append(i)
		for j in tmp:
			self.lista.append(j)
	def inter(self, conj):
		tmp = []
		for i in conj.lista:
			if self.lista.count(i) <> 0:
				tmp.append(i)
		return tmp
	def subtr(self, conj):
		tmp = []
		for i in self.lista:
			if conj.lista.count(i) == 0:
				tmp.append(i)
		return tmp
	def dump(self):
		for i in self.lista:
			print i


a = ConjuntoInteiros([1, 2, 3, 4])
b = ConjuntoInteiros([3, 4, 5, 6])
import string
class arquivo:
	def __init__(self):
		self.l=file.readlines(file("entrada.dat","r"))
	def trunca(self):
		self.n = 0
		for i in self.l:
		 self.tags = 0
		 self.problema = 0
		 self.contagem = 0
		 for j in string.split(i, ):
			p = string.find(j,"<")
			if p <> -1:
				if string.find(j,">",p) <> -1:
					self.tags += 1
				else:
					self.problema += 1
			self.contagem += 1
		self.n += 1
		self.result(self.n)
	def result(self, a):
#		temp=file("saida.dat","a")
#		linhaboa = "Linha " + a + " - Numero de palavras: " + str( self.contagem ) + " - <TAGS>: " + str( self.tags ) + " - Linhas com problema: " +  str( self.problema  ) + "\n"
#		file.write(temp,linhaboa)
#		file.close(temp)
		print "Linha ",a," - Numero de palavras: ",self.contagem," - <TAGS>: ",self.tags, " - Linhas com problema: ",self.problema

# ERRO 2 17 50
# ERRO 2 19 100
# ERRO 2 22 100
# ERRO 2 21 100
# ERRO 2 23 100
# ERRO 2 25 100



a = arquiv()
a.trunca()
