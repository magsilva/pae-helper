Exercicio 1 da lista de POO:

# ERRO TOTAL 1 4
# ERRO TOTAL 1 5
# ERRO PARCIAL 1 7
a) Construtor eh a funcao usada para criar o objeto para que este possa atuar. Jah o destrutor eh a funcao utilizada para destruir
o objeto quando o uso deste nao eh mais necessario. Em python, o construtor eh definido seguindo a seguinte sintaxe:
	def __init__(self)
e se desejarmos passar algum valor como parametro para algum atributo, estes parametros devem vir seguindo 'self'.
O mecanismo de destrutor utilizado eh conhecido como Garbage Collector, que consiste em detectar quais objetos nao sao mais
utilizados e destrui-los automaticamente.

b) 
# ERRO TOTAL 1 8

c) Os 5 principais conceitos introduzidos pelo paradigma de orientação a objetos são:
	- Objetos e Classes
	- Comunicacao com Mensagens
	- Herancas
	- Encapsulamento
	- Sobrecarga e Polimorfismo

d) Classe eh uma especificacao que define as variaveis e funcoes comuns a todos os objetos de um mesmo tipo
   Um objeto eh uma instancia de uma classe, semelhante a uma variável do tipo classe.
   Os métodos são funções que podem ser utilizadas pelos objetos da respectiva classe, e por objetos de outras classes em alguns casos.

e) LPOOs apresentam vantagens para todos os níveis de usuários, entre gerentes, analistas e programadores, pois garantem:
	desenvolvimento e manutenção mais rápido e mais barato
	processo de modelagem se torna mais simples
	produz um projeto limpo e gerenciável
	modelo objeto aliado às bibliotecas proporcionam aos programadores:
		programação se torna mais agradável
		melhora a produtividade

 #classe do exercicio 2 da lista
#chamada: a = Palavra('coisa')
#         a.conta_char()
#         a.conta_o_char('s')

class Palavra :
    def __init__(self, p='') :
        self.palavra = p

    def conta_char(self) :
        return len(self.palavra)

    def conta_o_char(self, char) :
        return self.palavra.count(char)


#programa do exercicio 3 da lista

# ERRO TOTAL 3 3
c1 = 0
c2 = 0
c3 = 0
c4 = 0
c5mais = 0
print 'Digite o texto (entre com linha em branco para terminar):\n'
linha = raw_input()
while linha != '' :
    lstpalavras = linha.split(' ')
    for pal in lstpalavras :
        p = Palavra(pal)
        count = p.conta_char()
        if count == 1 :
            c1 += 1
        elif count == 2 :
            c2 += 1
        elif count == 3 :
            c3 += 1
        elif count == 4 :
            c4 += 1
        elif count >= 5 :
            c5mais += 1
    linha = raw_input()
print '\n\nNumero de Palavras com:\n'
print '1 letra: %d' %c1
print '2 letras: %d' %c2
print '3 letras: %d' %c3
print '4 letras: %d' %c4
print '5 ou mais letras: %d' %c5mais
#exercicio 4 da lista
#chamada: a = Frases()
#         a.Gerar()

# ERRO PARCIAL 3 5

class Frases :
    def __init__(self) :
        self.artigo = ['o', 'a', 'um', 'uma']
        self.substantivo = ['gata', 'cao', 'cidade', 'carro', 'bicicleta', 'caixa', 'tomate']
        self.verbo = ['andou', 'correu', 'pulou', 'caiu', 'passou', 'se escondeu']
        self.preposicao = ['de', 'sobre', 'sob', 'ante','apos']

    def Gerar(self) :
        import random
        self.listafrases = []
        for n in range (0,20) :
            self.frase = ''
            self.frase = self.frase + random.choice(self.artigo) + ' '
            self.frase = self.frase + random.choice(self.substantivo) + ' '
            self.frase = self.frase + random.choice(self.verbo) + ' '
            self.frase = self.frase + random.choice(self.preposicao) + ' '
            self.frase = self.frase + random.choice(self.artigo) + ' '
            self.frase = self.frase + random.choice(self.substantivo) + '.'
            fraseupper = self.frase.capitalize()
            self.listafrases.append(fraseupper)
        for obj in self.listafrases :
            print obj
