# ERRO 1 6
# ERRO 1 4

import copy
class CInt:
	# construtor de classe
	def __init__(self, l):
		self.lista = []
		tmp = copy.deepcopy(l)
		for i in l:
			count = 0
			for j in tmp:
				if i is j:
					count += 1
			if count > 1:
				print "mais de 1 referencia ao mesmo objeto"
				return
		self.lista = l

	# adição
	def __add__(self, e):
		if type(e) == type(1):
			self.lista.append(e)
		else:
			print "tipo invalido"
			return
		count = 0
		for i in self.lista:
			if i is e:
				count += 1
		if count > 1:
			print "objeto ja esta no conjunto"
			return

	# remoção
	def __sub__(self, e):
		count = 0
		for i in self.lista:
			if i == e:
				count += 1
		if count == 0:
			print "objeto a ser removido nao esta na lista"
			return
		self.lista.remove(e)

	# une com outro conjunto
	def uniao(self, conj):
		tmp = []
		for i in conj.lista:
			if self.lista.count(i) == 0:
				tmp.append(i)
		for j in tmp:
			self.lista.append(j)

	# interseccao
	def inter(self, conj):
		tmp = []
		for i in conj.lista:
			if self.lista.count(i) <> 0:
				tmp.append(i)
		return tmp

	# subtracao
	def subtr(self, conj):
		tmp = []
		for i in self.lista:
			if conj.lista.count(i) == 0:
				tmp.append(i)
		return tmp

	# imprime o conjunto
	def dump(self):
		for i in self.lista:
			print i


a = CInt([1, 2, 3, 4])
b = CInt([3, 4, 5, 6])

# ERRO 2 21 Não identifica todas as tags de cada frase.
# ERRO 2 22 Não identifica todas as tags incorretas (provavalmente em decorrência de 2 21).
# ERRO 2 23 Não mostra as tags incorretas.
# ERRO 2 25 Não definem-se as classes solicitadas.

import string
class arquiv:
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
		temp=file("saida.dat","a")
		linhaboa = "Linha " + str(a) + " - Numero de palavras: " + str(self.contagem) + " - <TAGS>: " + str(self.tags) + " - Linhas com problema: " + str(self.problema) + "\n"
		file.write(temp,linhaboa)
		file.close(temp)
		#print "Linha ",a," - Numero de palavras: ",self.contagem," - <TAGS>: ",self.tags, " - Linhas com problema: ",self.problema


a = arquiv()
a.trunca()
