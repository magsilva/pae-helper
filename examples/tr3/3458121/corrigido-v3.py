UNIVERSIDADE DE S�O PAULO ? USP/ICMC
SCE-213: Programa��o Orientada � Objetos ? Profa. Renata Pontin
M�nica Ribeiro Porto Ferreira ? 3458121

LISTA DE EXERC�CIOS:

1Responda, objetivamente, com suas palavras:
2O que � ?Construtor? e ?Destrutor? de objetos? Cite as regras de sintaxe que devem ser empregadas na defini��o do construtor em Python e qual � o mecanismo de ?destrutor? que Python emprega.
# ERRO PARCIAL 1 4
Construtor � um m�todo utilizado para a cria��o de um objeto; quando seu programa cria um objeto, ele geralmente atribui valores ao objeto, e o construtor � utilizado para que esse objeto criado possa atuar.
# ERRO TOTAL 1 5
Como todo objeto possui um ciclo de vida, ent�o ele necessita ser criado, ter sua atua��o no sistema e logo depois, destru�do para desocupar espa�o na mem�ria. E para isso, existe o Destrutor: quando os objetos n�o s�o mais utilizados, eles s�o apagados e a mem�ria � liberada. 
# ERRO PARCIAL 1 7
No Python, a cria��o e destrui��o de objetos necessitam de m�todos especiais aos objetos. Os nome dos m�todos especiais s�o precedidos e seguidos por duplo underscore (__). Em Python, as inst�ncias s�o criadas usando um M�todo Especial j� definido (?__init__(self [args]?) e s�o destru�das atrav�s de um contador de refer�ncias ? garbage collected ? isto �, quando o contador se torna zero, a inst�ncia � destru�da. Mas uma inst�ncia tamb�m pode ser destru�da usando del

- Quais as formas de acesso que se pode normalmente utilizar na defini��o de uma classe?
Em uma classe, pode-se:
- Criar dinamicamente as instancias de uma classe 
Ex.: class Ponto:
		pass
			(
	prim . x = 2;    (  Cria��o Din�mica das Inst�ncias
	prim . y = 5;	(
- Passar uma inst�ncia como par�metros.
Ex.: class Ponto:
# ERRO TOTAL 1 8
	 def __str__ (self):
		return ?(? +str(self.x)+ ?,' + str(self.y)+ ?)'

- Quais s�o os 5 principais conceitos que se consolidaram no paradigma de ?Orienta��o a Objetos? que est�o dispon�veis na maioria das Linguagens de Programa��o Orientada � Objetos?
Os cinco principais conceitos de uma LPOO pura s�o:
- Tudo � um objeto
- Um programa � formado por um conjunto de objetos que dizem uns aos outros o que fazer atrav�s de m�todos/mensagens.
- Cada objeto tem a sua pr�pria mem�ria reservada quando ele � criado.
- Todo objeto tem uma classe ( � formado por um tipo de dado)
- Todos os objetos da mesma classe podem receber as mesmas mensagens e executar os mesmos m�todos.

# ERRO PARCIAL 1 9

- O que � uma classe? E um objeto? O que s�o m�todos de uma classe?
Classe: � um conjunto de atributos (especifica��es) que s�o associados a uma cole��o de objetos; � o principal mecanismo para se criar estruturas de dados e novos tipos de dados.
Objeto: � abstra��o de algo cujas caracter�sticas e comportamento s�o conhecidos e que tem uma interface definida e restrita com entidades externas.
M�todos: procedimentos para manipular os dados dos objetos.

- Quais as vantagens de se utilizar Linguagens de Programa��o Orientadas a Objetos em rela��o �s Linguagens Procedurais?
A principal vantagem de se utilizar uma LPOO ao inv�s da LP � a diminui��o do ?Gap Sem�ntico?, isto �, a diferen�a de significados ( linguagens de computa��o ( linguagens usuais dos clientes). Com isso, aumenta-se a produtividade do programador (fase do projeto fica mais ligada a fase da implementa��o).

1Escreva um programa para criar classe de palavras (Palavras), que possua um m�todo que retorne o nro de caracteres de cada palavra (Conta_char) e um outro m�todo que retorne o nro de ocorr�ncias de um dado caracter em uma palavra (Conta_o_char).
class Palavras:

# Funcao para inicializacao
   def __init__ (self, p=[]):
        self.palavra = p

#Funcao que conta o nro de caracteres de cada palavra
    def conta_char (self):
        return len(self.palavra)

#Funcao que conta o nro de ocorrencias de um dado caracter
    def conta_o_char (self, letra):
        return self.palavra.count(letra)
#Fim da Classe Palavras.
L = Palavras("lagosta")
print L.palavra
print L.conta_char()
print L.conta_o_char("a")
1Escreva um programa que l� v�rias linhas de texto do teclado e imprima uma tabela indicando o numero de palavras com uma letra, palavras com duas letras, palavras com tr�s letras, etc. que aparecem no texto. Esse programa deve utilizar a classe ?Palavras?do exerc�cio anterior.
#Exercicio 3:
class Tabela:
    #Funcao de inicializacao
    def __init__(self, M =[]):
        self.texto = M

              #Funcao de quebra do texto em uma lista de palavras
    def quebra (self):
        self.palavras = []

        while self.texto.count(" "):        
            while self.texto[0] == (" "):
                self.texto = self.texto[1:]
            pal = self.texto[:self.texto.index(" ")]
            self.palavras.append(pal)
            self.texto = self.texto[self.texto.index(" ")+1:]
        self.palavras.append(self.texto)

    #Funcao conta palavras...
    def numero_palavra (self):

        maxlen = -1

        for i in range(0,len(self.palavras)):
            if len(self.palavras[i]) > maxlen:
                maxlen = len(self.palavras[i])

        while maxlen > 0:
            count = 0
            for i in self.palavras:
                x = Palavras(i)
                if x.conta_char() == maxlen:
                  count += 1
            if count:        
                print ("ha ", count, "palavras com ", maxlen, "letras")
            maxlen -= 1

temp = str(raw_input("Digite o texto e tecle <enter> quando terminar: "))
tab = Tabela(temp)
print tab.texto
tab.quebra()
print tab.palavras
tab.numero_palavra()

1Escreva um programa que use gera��o de n�meros rand�micos para criar senten�as. O programa deve usar 4 tuplas de palavras chamadas ?artigo?, ?substantivo?, ?verbo? e ?preposi��o?. O programa deve criar uma senten�a atrav�s da sele��o de uma palavra de cada tupla na seguinte ordem: ?artigo?, ?substantivo?, ?verbo?, ?preposi��o?, ?artigo? e ?substantivo?. Cada vez que a palavra � obtida ela deve ser concatenada com a palavra anterior em uma lista para armazenar a senten�a inteira. As palavras devem ser separadas por espa�os. Quando a senten�a final � emitida, ela deve iniciar com letra mai�scula e terminar com um ponto final. O programa deve gerar 20 senten�as.
Exemplos de dados para os vetores:
?artigo? = ?o? ? ?a? - ?um? ? ?uma?
?substantivo0? = ?gata? ? ?c�o? - ?cidade? ? ?carro? ? ?bicicleta?
?verbo? = ?andou? ? ?correu? - ?pulou? ? ?caiu?
?preposi��o? = ?de? ? ?sobre? - ?sob? ? ?embaixo?

#Exercicio 4:
import random

artigo = ('o','a','um', 'uma')
substantivo = ('gata','cao','cidade','carro', 'bicicleta')
verbo = ('andou','correu','pulou', 'caiu')
preposicao = ('de','sobre','sob', 'embaixo')

for i in range (0,20):
  temp = []
  temp = artigo[int(random.random()*len(artigo))] +" "+substantivo[int(random.random()*len(artigo))]
+" "+verbo[int(random.random()*len(artigo))]+" "+preposicao[int(random.random()*len(artigo))] + " " + artigo[int(random.random()*len(artigo))]+ " " +substantivo[int(random.random()*len(artigo))]+ "."
    temp =  temp.capitalize()	
    print temp

# ERRO TOTAL 4 8
