Aluna: Carolina Toledo Ferraz nº Usp 3344524

3ª Lista de Exercícios

# ERRO TOTAL 1 1
# ERRO TOTAL 1 2
# ERRO TOTAL 1 3
# ERRO TOTAL 1 4
# ERRO TOTAL 1 5
# ERRO TOTAL 1 6
# ERRO TOTAL 1 7
# ERRO TOTAL 1 8
# ERRO TOTAL 1 9
# ERRO TOTAL 1 10

2)

class Palavras:
    def __init__(self, pal):
        self.palavra = pal

    def conta_char(self):
        return len(self.palavra)

    def conta_o_char(self, letra):
        tam = len(self.palavra)
        i = 0
        contador = 0
        while i < tam:
            if self.palavra[i] == letra:
                contador +=1
            i +=1
        return contador

a = Palavras('paralelepipedo')
print a.conta_char()
print a.conta_o_char('e')

3)

class Palavra:
    def __init__(self, pal):
        self.palavra = pal

        
    def conta_char(self):
        return len(self.palavra)

    def conta_o_char(self, letra):
        tam = len(self.palavra)
        i = 0
        contador = 0
        while i < tam:
            if self.palavra[i] == letra:
                contador +=1
            i +=1
        return contador


aux = ''
todas_palavras = []

# Le todas as palavras e instancia as classes
text = raw_input("entre com as frases \n")
for i in text:
    if not i.isspace():
        aux += i
    else:
        a = Palavra( aux )
	todas_palavras.append( a )
        aux = ''

k = 0 # Contador palavras
i = 1 # Quantidade de caracteres sendo procurados
# Loop para controlar ateh quando vai ser procuradas palavras
while k < len( todas_palavras ):
    palavras_x = [] # Palavras com i caracteres
    for x in todas_palavras:
        if x.conta_char() == i:
            palavras_x.append( x )
            k += 1
    print "Existem %d palavras com %d caracteres" % ( len(palavras_x), i)
    i +=1

4)

from random import *
class Randomico:
    def __init__(self):           
        self.artigo = ()
        self.substantivo = ()
        self.verbo = ()
        self.preposicao = ()
        
    def artigo1(self):
        self.artigo = ('o','a','um','uma')
        return self.artigo

    def substantivo1(self):
        self.substantivo = ('gata', 'cao', 'cidade', 'carro', 'bicicleta')
        return self.substantivo

    def verbo1(self):
        self.verbo = ('andou', 'correu', 'pulou', 'caiu')
        return self.verbo

    def preposicao1(self):
        self.preposicao = ('de', 'sobre', 'sob', 'embaixo')
        return self.preposicao

saida = ''
saida1 = ''
saida2 = ''
saida3 = ''
saida4 = ''
saida5 = ''
saida6 = ''
lista = []
a = Randomico()
k = a.artigo1()
j = a.substantivo1()
l = a.verbo1()
m = a.preposicao1()
x = 0

while x < 20:
    saida = choice(k)
    saida1 = choice(j)
    saida2 = choice(l)
    saida3 = choice(m)
    saida4 = choice(k)
    saida5 = choice(j)
    saida6 = saida + ' ' + saida1 + ' ' + saida2 + ' ' + saida3 + ' ' + saida4 + ' ' + saida5 + '.'
    saida6 = saida6.capitalize()
    lista.append(saida6)
    x +=1

for i in lista:
    print i


ou








from random import *
class Randomico:
    def __init__(self):           
        self.artigo = ()
        self.substantivo = ()
        self.verbo = ()
        self.preposicao = ()
        
    def artigo1(self):
        self.artigo = ('o','a','um','uma')
        return self.artigo

    def substantivo1(self):
        self.substantivo = ('gata', 'cao', 'cidade', 'carro', 'bicicleta')
        return self.substantivo

    def verbo1(self):
        self.verbo = ('andou', 'correu', 'pulou', 'caiu')
        return self.verbo

    def preposicao1(self):
        self.preposicao = ('de', 'sobre', 'sob', 'embaixo')
        return self.preposicao

saida = ''
saida1 = ''
saida2 = ''
saida3 = ''
saida4 = ''
saida5 = ''
saida6 = ''
lista = []
a = Randomico()
k = a.artigo1()
j = a.substantivo1()
l = a.verbo1()
m = a.preposicao1()
x = 0

while x < 20:
    result = randint(0,len(k)-1)
    saida = k[result]
    result = randint(0,len(j)-1)
    saida1 = j[result]
    result = randint(0,len(l)-1)
    saida2 = l[result]
    result = randint(0,len(m)-1)
    saida3 = m[result]
    result = randint(0,len(k)-1)
    saida4 = k[result]
    result = randint(0,len(j)-1)
    saida5 = j[result]
    saida6 = saida + ' ' + saida1 + ' ' + saida2 + ' ' + saida3 + ' ' + saida4 + ' ' + saida5 + '.'
    saida6 = saida6.capitalize()
    lista.append(saida6)
    x +=1

for i in lista:
    print i

