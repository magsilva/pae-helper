1.
# ERRO PARCIAL 1 4
# ERRO TOTAL 1 5
# ERRO TOTAL 1 5
# ERRO PARCIAL 1 7
Um "construtor" � o c�digo para a inicializa��o do objeto, sendo executado quando o objeto � referenciado. J� o "descritor" corresponde a opera��o de finaliza��o do objeto, liberando-o da mem�ria. O mecanismo de "construtor" � defin�do em Python pelo m�todo __init__, o "destrutor" � executado quando n�o h� mais nenhuma refer�ncia ao objeto, ocorrida com o fim do programa ou pelo comando del, defin�do na classe pelo m�todo __del__.

2.
# ERRO TOTAL 1 8

3.
- Objetos e classes
- Comunica��o com mensagens
- Heran�a
- Encapsulamento
- Sobrecarga e polimorfismo

# ERRO TOTAL 1 1
# ERRO TOTAL 1 2
# ERRO TOTAL 1 3

4.
Classe � a defini��o dos atributos e m�todos que ser�o associados aos objetos.
Objeto � a declara��o de uma classe, tornando o c�digo desta classe aplicavel a um programa.
M�todo � uma fun��o pertencente a um objeto.

5.
Uma linguagem de programa��o orientada a objetos permite uma representa��o muito mais pr�xima aos termos utilizados no mundo real em rela��o �s outras linguagem procedurais. Permite tamb�m a utiliza��o de diversas ferramentas de desenvolvimento de software, que facilitam muito mais a compreen��o do projeto tanto pelos desenvolvedores quanto pelos clientes. Aumentando tamb�m a possibilade de reuso de recursos do software e ajudando a manuten��o.

# ERRO PARCIAL 2 3

class Palavras:

	"Classe para contar o numero de letras de cada palavra em uma senten�a e\
	o numero de ocorrencias de um caracter em uma palavra"

	def __init__(self, frase):
		#Armazena cada palavra da sente�a com um elemento de uma lista
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

#20 repeti��es...
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
