#	Exercicio 2.2
#
#		Feito por: Rafael Henrique Manoel
#			   Monica Ribeiro Porto Ferreira
#---------------------------------------------------------------------


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

	def exibe_relatorio(self):
		i = 0
		fim = len(self.lista_frases)
		while i < fim:
			print "Linha %d - "%i,
			self.lista_frases[i].quebra_em_palavras()
			self.lista_frases[i].exibe_resultado()
			i +=1 
	

class Frase:
	def __init__(self):
		self.texto = ""
		self.n_palavras = 0
		self.n_tags = 0
		self.n_tags_defeito = 0
		self.tamanho = 0
		self.lista_tags = []

	def atribui(self, nova_frase):
		fim = nova_frase.find("\n")
		self.tamanho = len(nova_frase)

		if fim==-1:
			self.texto = nova_frase
			return ""
		else:
			self.texto = nova_frase[0:fim]
			return nova_frase[fim+1:len(nova_frase)]

	def quebra_em_palavras(self):
		p = Palavra()
		t = Tag()
		inicio = 0
		fim = 0

		while fim <> -1:
			fim = self.texto.find(" ",inicio)
			if fim == -1:
				result = t.atribui(self.texto[inicio:self.tamanho])
			else:
				result = t.atribui(self.texto[inicio:fim])
			inicio = fim+1		
			#tag certa
			if result > 0:
				#adicionando como str na lista para
				#facilitar na impressao
				self.lista_tags.append(t.texto)
				self.n_tags += 1
			#tag com problema
			elif result < 0:
				self.n_tags_defeito += 1		
			#nao eh tag
			else:
				p.atribui = t.texto

			self.n_palavras += 1

	def exibe_resultado(self):
		print self.n_palavras, "palavras - ", self.n_tags, "(", self.lista_tags, ") - ", self.n_tags_defeito, "tags-problema"
		

	def __len__(self):
		return len(self.texto)

	def imprime(self):
		print self.texto

class Palavra:

	def __init__(self):
		self.texto = ""

	def atribui(self):
		return self.texto

	def __len__(self):
		return len(self.texto)


class Tag(Palavra):

	texto = ""

	def atribui(self, palavra):
		if palavra[0] == '<' and palavra[len(palavra)-1] == '>':
			self.texto = palavra
			#tudo certo
			return 1
		elif palavra[0] == '<' or palavra[len(palavra)-1] == '>':
			self.texto = palavra
			#tag com defeito
			return -1
		else:
			#naum eh tag
			return 0		
		

#fim das definicoes de classe			
			

#altere a localizacao do arquivo
a = Texto("a.txt")
a.quebra_frases()
a.exibe_relatorio()


# ERRO 2 23

#Exercicio 2.1##########################################
#                                                      #
#   Feito por:                                         #
#               Rafael Henrique Manoel          3285310#
#               Monica Ribeiro Porto Ferreira   3458121#
########################################################

# ERRO 1 6
# ERRO 1 2

class ConjuntoInteiros:

    #funcao para inicializacao
    def __init__(self, Lista=[]):
        self.elementos = []
        tamanho_lista = len(Lista)
        i = 0
        while i < tamanho_lista:
            self.insere(Lista[i])
            i+=1

    #funcao que insere na classe
    def insere(self, X):
        nX = self.elementos.count(X)
        if nX == 0:
            self.elementos.append(int(X))

    #funcao que remove do conjunto
    def remove(self, X):
        if self.elementos.count(X) > 0:
            self.elementos.remove(X)

    #sobrecarga de funcoes para poder usar o polimorfismo
    def __len__(self):
        return len(self.elementos)

    def __getitem__(self, i):
        return self.elementos[i]
    #fim sobrecarga

    #uniao de conjuntos
    def __add__(self, cjB):
        i = 0
        tamanho_cjB = len(cjB)
        result = ConjuntoInteiros(self)
        while i < tamanho_cjB:
            result.insere(cjB[i])
            i+=1
        return result

    #interseccao
    def __mul__(self, cjB):
        i,j=0,0
        size_self, size_cjB = len(self), len(cjB)
        result = ConjuntoInteiros()
        while i < size_self:
            while j < size_cjB:
                if self[i] == cjB[j]:
                    result.insere(cjB[j])
                j+=1
            j=0
            i+=1 
        return result

    #subtracao
    def __sub__(self, cjB):
        i,j=0,0
        size_self, size_cjB = len(self), len(cjB)
        result = ConjuntoInteiros(self)
        while i < size_self:
            while j < size_cjB:
                if self[i] == cjB[j]:
                    result.remove(cjB[j])
                j+=1
            j=0
            i+=1 
        return result

    def imprime(self):
        print self.elementos
        
#Fim da classe

        
        

L = [1,2,3,4]
a = ConjuntoInteiros(L)
b = ConjuntoInteiros()
b.insere(5)
b.insere(6)
b.insere(7)
b.insere(2)
c = ConjuntoInteiros(a)
c.insere(90)
d = ConjuntoInteiros()
e = ConjuntoInteiros()
d.insere(2)
d.insere(3)

                

    
