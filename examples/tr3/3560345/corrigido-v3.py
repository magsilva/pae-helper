Programação Orientada a Objetos
3a Lista de Exercícios
Nomes:

	Cleber Castro Hage	No USP: 3560345
	Glauco Becaro		No USP: ???????

1)
# ERRO TOTAL 1 4
# ERRO TOTAL 1 5
# ERRO TOTAL 1 7
1."Construtor" de objetos é a criação de objetos para que possam atuar, assim como as variáveis precisam ser instanciadas para serem utilizadas.
"Destrutor" de objetos é quando objetos são apagados por serem desnecessários no momento. Assim, o espaço alocado pelos objetos na memória são liberados.
Todos os tipos de dados internos consistem de alguns dados e um conjunto de métodos especiais aos objetos. Os nomes dos métodos especiais são sempre precedidos e seguidos por duplo underscore ("__"). Para o construtor: __init__(self [,args]). Para o destrutor: __del__(self). Este torna possível escrever em cima do espaço antes alocado para objetos.

2.Pode-se passar uma instância como um parâmetro.
# ERRO TOTAL 1 8

# ERRO TOTAL 1 9
3.Os 5 principais conceitos são:
Agrada vários níveis de usuários
Encapsulamentos em módulos
Disciplina para acesso às variáveis
Controle de acesso dos programadores
Processo de projetar objetos apresenta mais desafios que  projeto procedural

4.Uma classe é uma especificação que define as variáveis e funções comuns a todos os objetos de um certo tipo.
Um objeto é uma instância de uma classe.
Métodos são os mecanismos pelos quais se manipulam as variáveis. Os parâmetros são passados por mensagens de um objeto para o outro para seus métodos.

5.Agrada vários níveis de usuários
6.Encapsulamentos em módulos
7.Disciplina para acesso às variáveis
8.Controle de acesso dos programadores
9.Têm por objetivo construir uma classe que exponha ao programador cliente apenas o que ele necessita

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
	    print("O número de caracteres de '%s' é %d") %(word,i)

	def Conta_o_Char(self, palavra, letter):
	    l = 0
	    c = 0
	    for c in palavra:
		if (c == letter):
		    l+= 1
			    
	    print("O número de vezes em que '%c' ocorre é %d")%(letter,l)

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

O Python salvou o próximo exercício em cima deste fazendo com que eu perdesse a solução deste. (Mas se quiserem eu refaço novamente e envio tudo certo: meu e-mail: cchage@grad.icmc.usp.br

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
    


