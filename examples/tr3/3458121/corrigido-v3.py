UNIVERSIDADE DE SÃO PAULO ? USP/ICMC
SCE-213: Programação Orientada à Objetos ? Profa. Renata Pontin
Mônica Ribeiro Porto Ferreira ? 3458121

LISTA DE EXERCÍCIOS:

1Responda, objetivamente, com suas palavras:
2O que é ?Construtor? e ?Destrutor? de objetos? Cite as regras de sintaxe que devem ser empregadas na definição do construtor em Python e qual é o mecanismo de ?destrutor? que Python emprega.
# ERRO PARCIAL 1 4
Construtor é um método utilizado para a criação de um objeto; quando seu programa cria um objeto, ele geralmente atribui valores ao objeto, e o construtor é utilizado para que esse objeto criado possa atuar.
# ERRO TOTAL 1 5
Como todo objeto possui um ciclo de vida, então ele necessita ser criado, ter sua atuação no sistema e logo depois, destruído para desocupar espaço na memória. E para isso, existe o Destrutor: quando os objetos não são mais utilizados, eles são apagados e a memória é liberada. 
# ERRO PARCIAL 1 7
No Python, a criação e destruição de objetos necessitam de métodos especiais aos objetos. Os nome dos métodos especiais são precedidos e seguidos por duplo underscore (__). Em Python, as instâncias são criadas usando um Método Especial já definido (?__init__(self [args]?) e são destruídas através de um contador de referências ? garbage collected ? isto é, quando o contador se torna zero, a instância é destruída. Mas uma instância também pode ser destruída usando del

- Quais as formas de acesso que se pode normalmente utilizar na definição de uma classe?
Em uma classe, pode-se:
- Criar dinamicamente as instancias de uma classe 
Ex.: class Ponto:
		pass
			(
	prim . x = 2;    (  Criação Dinâmica das Instâncias
	prim . y = 5;	(
- Passar uma instância como parâmetros.
Ex.: class Ponto:
# ERRO TOTAL 1 8
	 def __str__ (self):
		return ?(? +str(self.x)+ ?,' + str(self.y)+ ?)'

- Quais são os 5 principais conceitos que se consolidaram no paradigma de ?Orientação a Objetos? que estão disponíveis na maioria das Linguagens de Programação Orientada à Objetos?
Os cinco principais conceitos de uma LPOO pura são:
- Tudo é um objeto
- Um programa é formado por um conjunto de objetos que dizem uns aos outros o que fazer através de métodos/mensagens.
- Cada objeto tem a sua própria memória reservada quando ele é criado.
- Todo objeto tem uma classe ( é formado por um tipo de dado)
- Todos os objetos da mesma classe podem receber as mesmas mensagens e executar os mesmos métodos.

# ERRO PARCIAL 1 9

- O que é uma classe? E um objeto? O que são métodos de uma classe?
Classe: é um conjunto de atributos (especificações) que são associados a uma coleção de objetos; é o principal mecanismo para se criar estruturas de dados e novos tipos de dados.
Objeto: é abstração de algo cujas características e comportamento são conhecidos e que tem uma interface definida e restrita com entidades externas.
Métodos: procedimentos para manipular os dados dos objetos.

- Quais as vantagens de se utilizar Linguagens de Programação Orientadas a Objetos em relação às Linguagens Procedurais?
A principal vantagem de se utilizar uma LPOO ao invés da LP é a diminuição do ?Gap Semântico?, isto é, a diferença de significados ( linguagens de computação ( linguagens usuais dos clientes). Com isso, aumenta-se a produtividade do programador (fase do projeto fica mais ligada a fase da implementação).

1Escreva um programa para criar classe de palavras (Palavras), que possua um método que retorne o nro de caracteres de cada palavra (Conta_char) e um outro método que retorne o nro de ocorrências de um dado caracter em uma palavra (Conta_o_char).
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
1Escreva um programa que lê várias linhas de texto do teclado e imprima uma tabela indicando o numero de palavras com uma letra, palavras com duas letras, palavras com três letras, etc. que aparecem no texto. Esse programa deve utilizar a classe ?Palavras?do exercício anterior.
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

1Escreva um programa que use geração de números randômicos para criar sentenças. O programa deve usar 4 tuplas de palavras chamadas ?artigo?, ?substantivo?, ?verbo? e ?preposição?. O programa deve criar uma sentença através da seleção de uma palavra de cada tupla na seguinte ordem: ?artigo?, ?substantivo?, ?verbo?, ?preposição?, ?artigo? e ?substantivo?. Cada vez que a palavra é obtida ela deve ser concatenada com a palavra anterior em uma lista para armazenar a sentença inteira. As palavras devem ser separadas por espaços. Quando a sentença final é emitida, ela deve iniciar com letra maiúscula e terminar com um ponto final. O programa deve gerar 20 sentenças.
Exemplos de dados para os vetores:
?artigo? = ?o? ? ?a? - ?um? ? ?uma?
?substantivo0? = ?gata? ? ?cão? - ?cidade? ? ?carro? ? ?bicicleta?
?verbo? = ?andou? ? ?correu? - ?pulou? ? ?caiu?
?preposição? = ?de? ? ?sobre? - ?sob? ? ?embaixo?

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
