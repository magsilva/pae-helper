#LISTA 04: HERANÇA
#Mônica Ribeiro Porto Ferreira - 3458121

import copy
class Texto:
	def __init__(self, nome_arq):
		self.arq = open(nome_arq, "r")
		self.texto = self.arq.read()
		self.lista_frases = []
	def quebra_frases(self):
		texto_buf = self.texto
		inicio = fim = 0
		buf = Frase()
		a = Frase()
		while 1:
			texto_buf = buf.atribui(texto_buf)
			if buf.texto == "":
				break
			a = copy.deepcopy(buf)
			self.lista_frases.append(a)

class Frase:
	def __init__(self):
		self.texto = ""
		self.n_palavras = 0
		self.tamanho = 0
	def quebra_em_palavras(self):
		p = Palavra()
		inicio = 0
		fim = 0
		while fim <> -1:
			fim = self.texto.find(" ",inicio)
			if fim == -1:
				result = t.atribui(self.texto[inicio:self.tamanho])
			else:
				result = t.atribui(self.texto[inicio:fim])
			inicio = fim+1		
			self.n_palavras += 1

class Palavra(Frase):
	def __init__(self):
            self.artigo=["o","a","os","as","um","uma","uns","umas"]
            self.subst = []
            self.vervo = []
		

#altere a localizacao do arquivo
a = Texto("a.txt")
a.quebra_frases()

# ERRO 1 3 100
# ERRO 1 4 100
# ERRO 1 5 100
# ERRO 1 6 100
# ERRO 1 7 100
# ERRO 1 8 100
# ERRO 1 9 100
# ERRO 1 10 100
# ERRO 1 11 100
# ERRO 1 12 100
# ERRO 1 13 100
# ERRO 1 14 100
