"Aluno: Rodrigo Mithuhiro Oshiro No. 3528863"
"renata@icmc.usp.br"

# ERRO TOTAL 1 4
# ERRO TOTAL 1 5
# ERRO TOTAL 1 6
# ERRO PARCIAL 1 7
# ERRO TOTAL 1 8
# ERRO PARCIAL 1 9
"""
1)
* Construtor e a criacao de um objeto no mundo logico, ou seja, o instanciamento deste.
  Destrutor e a eliminacao do objeto do mundo logico, ou seja, a remocao de sua existencia.
  Para se definir um construtor em Python, basta atribuirmos a um objeto um dado valor, podendo ser, por exemplo,
  uma classe. Assim, a atribuicao cria objetos em Python. O destrutor em Python e feito pelo mecanismo de garbage collection,
  ou seja, o objeto e destruido assim que nao ha mais referencias a ele. Isso e possivel com o uso de contadores as
  referencias de cada objeto.
* Acesso a atributos e metodos, por meio de mensagens
* Abstracao, encapsulamento, polimorfismo, heranca, troca de mensagens
* Classe e uma especificacao que define atributos e metodos para uma dada representacao do mundo real.
  Objeto e uma instancia de uma classe, ou seja, representacao daquilo que e concreto, por meio de uma interface bem
  definida. Metodos sao procedimentos definidos pela classe que realizam operacoes relativas a elas.
* A OO permite maior abstracao no modo de representar os dados e procedimentos, encapsulando-os em forma de objetos
  mais estaveis e mais definidos em relacao a uma linguagem procedimental.
"""

"""
2)
"""
class Palavra:
	def __init__(self,palavra):
		self.palavra = palavra
	def Conta_char(self):
		return len(self.palavra)
	def Conta_o_char(self,c):
		result = 0
		for x in self.palavra:
			if x == c:
				result += 1
		return result


def ordena(x,y):
    if x.Conta_char() > y.Conta_char():
        return 0
    return -1

"""
3)
"""
# ERRO TOTAL 3 3

def texto():
	linha = "0"
	palavras = []
	while linha:
		linha = raw_input()
		lista = []
		lista = linha.split(" ")
		for x in lista:
			if x:
				y = Palavra(x)
				palavras.append(y)
        palavras.sort(ordena)
        lista = []
        for x in range(palavras[0].Conta_char(),1+palavras[-1].Conta_char()):
		lista.append(0)
	size = palavras[0].Conta_char()
	for x in palavras:
		lista[x.Conta_char()-size] += 1
	for x in lista:
		if x:
			print "Palavras com %d caracteres: %d" % (size,x)
		size += 1

"""
4)
"""
artigo = ('o','a','um','uma')
substantivo = ('gata','cachorro','cidade','carro','bicicleta','onibus','maria','macaco','sofa','dinheiro')
verbo = ('andou','correu','pulou','caiu','roubou','deixou','enganou','sentou')
preposicao = ('de','sobre','sob','embaixo','acima','acerca','com')

# ERRO PARCIAL 4 6
# ERRO TOTAL 4 8
import random
def sentenca():
	x = 200
	while x:
		fisrt = artigo[random.randrange(0,len(artigo))]
		result = fisrt[0].upper() + fisrt[1:] + ' '
		result += substantivo[random.randrange(0,len(substantivo))] + ' '
		result += verbo[random.randrange(0,len(verbo))] + ' '
		result += preposicao[random.randrange(0,len(preposicao))] + ' '
		result += artigo[random.randrange(0,len(artigo))] + ' '
		result += substantivo[random.randrange(0,len(substantivo))] + '.'
		print result
		x -= 1
