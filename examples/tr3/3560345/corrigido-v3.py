Programa��o Orientada a Objetos
3a Lista de Exerc�cios
Nomes:

	Cleber Castro Hage	No USP: 3560345
	Glauco Becaro		No USP: ???????

1)
# ERRO TOTAL 1 4
# ERRO TOTAL 1 5
# ERRO TOTAL 1 7
1."Construtor" de objetos � a cria��o de objetos para que possam atuar, assim como as vari�veis precisam ser instanciadas para serem utilizadas.
"Destrutor" de objetos � quando objetos s�o apagados por serem desnecess�rios no momento. Assim, o espa�o alocado pelos objetos na mem�ria s�o liberados.
Todos os tipos de dados internos consistem de alguns dados e um conjunto de m�todos especiais aos objetos. Os nomes dos m�todos especiais s�o sempre precedidos e seguidos por duplo underscore ("__"). Para o construtor: __init__(self [,args]). Para o destrutor: __del__(self). Este torna poss�vel escrever em cima do espa�o antes alocado para objetos.

2.Pode-se passar uma inst�ncia como um par�metro.
# ERRO TOTAL 1 8

# ERRO TOTAL 1 9
3.Os 5 principais conceitos s�o:
Agrada v�rios n�veis de usu�rios
Encapsulamentos em m�dulos
Disciplina para acesso �s vari�veis
Controle de acesso dos programadores
Processo de projetar objetos apresenta mais desafios que  projeto procedural

4.Uma classe � uma especifica��o que define as vari�veis e fun��es comuns a todos os objetos de um certo tipo.
Um objeto � uma inst�ncia de uma classe.
M�todos s�o os mecanismos pelos quais se manipulam as vari�veis. Os par�metros s�o passados por mensagens de um objeto para o outro para seus m�todos.

5.Agrada v�rios n�veis de usu�rios
6.Encapsulamentos em m�dulos
7.Disciplina para acesso �s vari�veis
8.Controle de acesso dos programadores
9.T�m por objetivo construir uma classe que exponha ao programador cliente apenas o que ele necessita

2)
class Palavra:
	def __init__(self, word = "  ", letter = " "):
		self.word =word
		self.palavra=" "
		self.letter = letter
		
		
	def Conta_Char(self, word):
	    i = 0
	    j=" "
	    for j in word:
		if (j != "\0"):
		    i+= 1
	    print("O n�mero de caracteres de '%s' � %d") %(word,i)

	def Conta_o_Char(self, palavra, letter):
	    l = 0
	    c = 0
	    for c in palavra:
		if (c == letter):
		    l+= 1
			    
	    print("O n�mero de vezes em que '%c' ocorre � %d")%(letter,l)

3)
def Palavras(self):
    t = 0
    n = 0 
    linha = raw_input()
    linhaFinal = []
    t = linha.find(' ', n)
    Dict = {t:linhaFinal[0:t-1]}
    while n != -1:
	  n = t + 1
	  t = linha.find(' ', n)
	  Dict = {t:linha[n:t-1]}
# ERRO TOTAL 3 0

# ERRO TOTAL 3 3
# ERRO TOTAL 3 5
# ERRO TOTAL 3 6

4)
# ERRO TOTAL 4 1
# ERRO TOTAL 4 2 
# ERRO TOTAL 4 3
# ERRO TOTAL 4 4 
# ERRO TOTAL 4 5 
# ERRO TOTAL 4 6
# ERRO TOTAL 4 7
# ERRO TOTAL 4 8

O Python salvou o pr�ximo exerc�cio em cima deste fazendo com que eu perdesse a solu��o deste. (Mas se quiserem eu refa�o novamente e envio tudo certo: meu e-mail: cchage@grad.icmc.usp.br

5)
class Ponto:
    def __init__(self, x=0, y=0):
	self.x=x
	self.y=y

class Quadrilatero:
    def __init__(self):
	self.p1 = Ponto()
	self.p2 = Ponto()
	self.p3 = Ponto()
	self.p4 = Ponto()

class Trapezio(Quadrilatero):
    


