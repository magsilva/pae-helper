1.
# ERRO PARCIAL 1 4
# ERRO TOTAL 1 5
# ERRO TOTAL 1 5
# ERRO PARCIAL 1 7
Um "construtor" é o código para a inicialização do objeto, sendo executado quando o objeto é referenciado. Já o "descritor" corresponde a operação de finalização do objeto, liberando-o da memória. O mecanismo de "construtor" é definído em Python pelo método __init__, o "destrutor" é executado quando não há mais nenhuma referência ao objeto, ocorrida com o fim do programa ou pelo comando del, definído na classe pelo método __del__.

2.
# ERRO TOTAL 1 8

3.
- Objetos e classes
- Comunicação com mensagens
- Herança
- Encapsulamento
- Sobrecarga e polimorfismo

# ERRO TOTAL 1 1
# ERRO TOTAL 1 2
# ERRO TOTAL 1 3

4.
Classe é a definição dos atributos e métodos que serão associados aos objetos.
Objeto é a declaração de uma classe, tornando o código desta classe aplicavel a um programa.
Método é uma função pertencente a um objeto.

5.
Uma linguagem de programação orientada a objetos permite uma representação muito mais próxima aos termos utilizados no mundo real em relação às outras linguagem procedurais. Permite também a utilização de diversas ferramentas de desenvolvimento de software, que facilitam muito mais a compreenção do projeto tanto pelos desenvolvedores quanto pelos clientes. Aumentando também a possibilade de reuso de recursos do software e ajudando a manutenção.

# ERRO PARCIAL 2 3

class Palavras:

	"Classe para contar o numero de letras de cada palavra em uma sentença e\
	o numero de ocorrencias de um caracter em uma palavra"

	def __init__(self, frase):
		#Armazena cada palavra da senteça com um elemento de uma lista
		self.lista = []
		while frase.count(' '):
			self.lista.append(frase[:frase.index(' ')])
			frase = frase[frase.index(' ') + 1:]
		self.lista.append(frase)

	def Conta_char(self):
		#Conta o numero de caracteres em cada palavra da lista, retornando uma lista como resultado
		resultado = []
		for x in self.lista:
			resultado.append(len(x))
			#print len(resultado)
			resultado[-1] -= self.Conta_o_char(x, '.')
			resultado[-1] -= self.Conta_o_char(x, ',')
			resultado[-1] -= self.Conta_o_char(x, '!')
			resultado[-1] -= self.Conta_o_char(x, '?')
		return resultado

	def Conta_o_char(self, palavra, char):
		#Conta o numero de ocorrencias de um determinado caracter em uma palavra	
		cont = 0
		for x in range(len(palavra)):
			if palavra[x] == char:
				cont = cont + 1
		return cont

#Entrada do texto
texto = raw_input('Digite o texto: ')

#Declara o objeto
ob_pal = Palavras(texto)

#Inicia vetor para contagem dos valores da resposta
resposta = []
for x in range(11):
	resposta.append(0)

#Percorre o resultado obtido e soma os valores no vetor
for x in ob_pal.Conta_char():
	if x > 10:
		resposta[10] += 1
	else:
		resposta[x-1] += 1

#Imprime a resposta
for x in range(10):
	print resposta[x], 'palavras com', x+1, 'letras'
print resposta[10], 'palavras com mais de 10 letras'

# ERRO PARCIAL 3 3		
# ERRO PARCIAL 3 5




#Carrega a classe Random
from random import Random

#inicializa as tuplas
art = ('o', 'a', 'um', 'uma')
sub = ('gata', 'cao', 'cidade', 'carro', 'bicicleta')
verbo = ('andou', 'correu', 'pulou', 'caiu')
prep = ('de', 'sobre', 'sob', 'embaixo de')

#declara o objeto para gerar numeros aleatorios
r = Random()

print

#20 repetições...
for x in range(20):
    
    #string para a primeira palavra
    ini = art[(int)(r.random() * len(art))]

    #junta todas as strings
    frase = art[(int)(r.random() * len(art))].capitalize() + ' ' +\
            sub[(int)(r.random() * len(sub))] + ' ' +\
            verbo[(int)(r.random() * len(verbo))] + ' ' +\
            prep[(int)(r.random() * len(prep))] + ' ' +\
            art[(int)(r.random() * len(art))] + ' ' +\
            sub[(int)(r.random() * len(sub))] + '.'

    #imprime a frase
    print frase

# ERRO TOTAL 4 8
