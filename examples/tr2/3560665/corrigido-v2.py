# Exercicio de POO
# Hugo Degiovanni Jr        3530230
# Koji E. Sasaoka           3560665
# Marco Aurelio Roncati     3455855


#Exercicio 2.1
#Implementacao da classe Conjunto Inteiros

class conjuntointeiros :
    def __init__(self,*p_arbitrarios):
        self.inteiros = []
        for p_atual in p_arbitrarios:
            if type(p_atual) == int:
                self.inteiros.append (p_atual)
            elif p_atual.__class__ == conjuntointeiros:
                self.inteiros.extend(p_atual.inteiros)

# ERRO 1 4
                    
    def inserir(self, valor):
        if type(valor) == int:
            self.inteiros.append (valor)
        elif valor.__class__ == conjuntointeiros:
            self.inteiros.extend(valor.inteiros)

    def remover(self, valor):
        if valor in self.inteiros:
            self.inteiros.remove(valor)
    
    def imprimir(self):
        print self.inteiros

# ERRO 1 2
    def uniao (self, outro):
        import copy
        resultado = []
        resultado = copy.deepcopy(self.inteiros)
        for valor in outro.inteiros:
            if valor not in self.inteiros:
                resultado.append (valor)
        return resultado
        
        
        
    def interseccao (self, outro):
        resultado = []
        for valor in self.inteiros:
            for outrovalor in outro.inteiros:
                if valor == outrovalor:
                    resultado.append (valor)
        return resultado
        
    def subtracao (self, outro):
        import copy
        resultado = []
        resultado = copy.deepcopy(self.inteiros)
        for valor in outro.inteiros:
            if valor in resultado:
                resultado.remove(valor)
        return resultado



#Exercicio 2.2

class Frases :
	def __init__ (self) :
		f = open('entrada.txt', 'r')
		self.frases = f.readlines()
		f.close
	def percorre (self) :
		cont_linha = 1
		for x in self.frases :
			o_palavras = Palavras()
			o_tags = Tags()
			l_palavras = o_palavras.contas(x)
			l_tags = o_tags.certas(l_palavras)

			print 'linha', cont_linha, '-', len(l_palavras), 'palavras -', len(l_tags), 'tags', l_tags, '-', o_tags.n, 'tags-problema'
			cont_linha += 1

class Palavras :
	def __init__ (self) :
		self.palavra = []        
	def contas (self, frase) :
		while ' ' in frase :
			self.palavra.append(frase[:frase.index(' ')])
			frase = frase[frase.index(' ') + 1:]
		self.palavra.append(frase)
		return self.palavra

class Tags :
	def __init__ (self) :
		self.tag = []
		self.n = 0

	def certas (self, palavra) :
		for x in palavra :
			if '<' in x or '>' in x :
				if x[0] == '<' and x[-1] == '>': 
					self.tag.append(x)
				elif x[0] == '<' and x[-2:] == '>\n':
					self.tag.append(x[:-1])
				else :
					self.n += 1
		return self.tag

print 'arq. entrada:'
f = open('entrada.txt', 'r')
linha = f.read()
while linha != '' :
	print linha
	linha = f.read()
f.close
print 'arq. saida'
o_frases = Frases()
o_frases.percorre ()

# ERRO 2 23
