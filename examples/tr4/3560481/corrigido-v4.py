
#  Quarta Lista de exercícios de POO

#  Alunos:

#  Santiago de Moura Luz
#  Marco Aurelio Rescia Alher
#  Alexandre Almeida da Costa Lucas


#********************************************************************

class frase:
    def __init__(self):
        self.f = open('frases.txt', 'r')
        self.pal = []
        self.pal = self.f.readline()
        self.tamanho = len(self.pal)
        self.lista = []
        for i in range(0,self.tamanho):
            if self.pal[i] == " ":
                self.lista.append(i)


class palavra(frase):
    def __init__(self):
        frase.__init__(self)
        #lista vai ter tamanho 4 espacos em branco entao:
        self.palavra1 = self.pal[0:self.lista[0]]
        self.palavra2 = self.pal[self.lista[0]+1:self.lista[1]]
        self.palavra3 = self.pal[self.lista[1]+1:self.lista[2]]
        self.palavra4 = self.pal[self.lista[2]+1:self.lista[3]]
        self.palavra5 = self.pal[self.lista[3]+1:self.tamanho]
    def genero(self):

	if self.palavra1 == 'A':
	    artigo1 = "O"
	if self.palavra1 == 'O':
	    artigo1 = "A"
	if self.palavra1 == 'As':
	    artigo1 = "Os"
	if self.palavra1 == 'Os':
	    artigo1 = "As"
	if self.palavra1 == 'Uma':
	    artigo1 = "Um"
	if self.palavra1 == 'Um':
	    artigo1 = "Uma"
	if self.palavra1 == 'Umas':
	    artigo1 = "Uns"
	if self.palavra1 == 'Uns':
	    artigo1 = "Umas"
	    
	i = 0
	subst2 = ''
	if self.palavra2[-1] == 's':
	    n=len(self.palavra2)
	    while i < n-2:
		subst2 = subst2 + self.palavra2[i]
		i+=1
	    if self.palavra2[i] == 'a':
		subst2 = subst2 + 'os'
	    else:
		subst2 = subst2 + 'as'
		
	i = 0
	if (self.palavra2[-1] == 'a' or self.palavra2[-1] == 'o'):
	    n=len(self.palavra2)
	    while i < n-1:
		subst2 = subst2 + self.palavra2[i]
		i+=1
	    if self.palavra2[i] == 'a':
		subst2 = subst2 + 'o'
	    else:
		subst2 = subst2 + 'a'
		
	if self.palavra4 == 'a':
	    artigo4 = "o"
	if self.palavra4 == '0':
	    artigo4 = "a"
	if self.palavra4 == 'as':
	    artigo4 = "os"
	if self.palavra4 == 'os':
	    artigo4 = "as"
	if self.palavra4 == 'uma':
	    artigo4 = "um"
	if self.palavra4 == 'um':
	    artigo4 = "uma"
	if self.palavra4 == 'umas':
	    artigo4 = "uns"
	if self.palavra4 == 'uns':
	    artigo4 = "umas"

	    
	i = 0
	subst5 = ''
	if self.palavra5[-1] == 's':
	    n=len(self.palavra5)
	    while i < n-2:
		subst5 = subst5 + self.palavra5[i]
		i+=1
	    if self.palavra5[i] == 'a':
		subst5 = subst5 + 'os'
	    else:
		subst5 = subst5 + 'as'
		
	i = 0
	if (self.palavra5[-1] == 'a' or self.palavra5[-1] == 'o'):
	    
	    n=len(self.palavra5)
	    while i < n-1:
		subst5 = subst5 + self.palavra5[i]
		i+=1
	    if self.palavra5[i] == 'a':
		subst5 = subst5 + 'o'
	    else:
		subst5 = subst5 + 'a'

	
	gener = artigo1 + " " + subst2 + " " + self.palavra3 + " " + artigo4 + " " + subst5
	print(gener)

        #Cinco palavras alocadas
        #obtem palavras


class artigo(palavra):
    def __init__(self):
	palavra.__init__(self)
    def palavraum(self):
        if self.palavra1 == 'O':
            self.artigonovo = "Os"
        if self.palavra1 == 'A':
            self.artigonovo = "As"
        if self.palavra1 == 'Os':
            self.artigonovo = "O"
        if self.palavra1 == 'As':
            self.artigonovo = "A"
        if self.palavra1 == 'Um':
            self.artigonovo = "Uns"
        if self.palavra1 == 'Uma':
            self.artigonovo = "Umas"
        if self.palavra1 == 'Uns':
            self.artigonovo = "Um"
        if self.palavra1 == 'Umas':
            self.artigonovo = "Uma"
        return self.artigonovo
    def palavraquatro(self):
        if self.palavra1 == 'o':
            self.artigonovo = "os"
        if self.palavra1 == 'a':
            self.artigonovo = "as"
        if self.palavra1 == 'os':
            self.artigonovo = "o"
        if self.palavra1 == 'as':
            self.artigonovo = "a"
        if self.palavra4 == 'um':
            self.artigonovo2 = "uns"
        if self.palavra4 == 'uma':
            self.artigonovo2 = "umas"
        if self.palavra4 == 'uns':
            self.artigonovo2 = "Um"
        if self.palavra4 == 'umas':
            self.artigonovo2 = "uma"
        return self.artigonovo2       


class verbo(palavra):
    def __init__(self):
	palavra.__init__(self)

    def verbonovo(self):
        if self.palavra3[-1] == 'i':
            self.verbonovo = self.palavra3[0:-1] + 'em'
        else:
            if self.palavra3[-1] == "a" or self.palavra3[-1] == "e":
                self.verbonovo = self.palavra3 + 'm'
        return self.verbonovo


class substantivo(palavra):
    def __init__(self):
	palavra.__init__(self)
    def subs(self):
	i = 0
	self.subsnovo = ''
	if self.palavra2[-1] != 's':
            self.subsnovo = self.palavra2 + 's'
        else:
	    n=len(self.palavra2)
	    while i < n-1:
		self.subsnovo = self.subsnovo + self.palavra2[i]
		i+=1
	    if self.palavra2[i] == 'a':
		self.subsnovo = self.subsnovo + 'as'
	    else:
		self.subsnovo = self.subsnovo + 'os'
        return self.subsnovo
    def subs2(self):
	i = 0
	self.subsnovo2 = ''
	if self.palavra5[-1] != 's':
            self.subsnovo2 = self.palavra2 + 's'
        else:
	    n=len(self.palavra5)
	    while i < n-1:
		self.subsnovo2 = self.subsnovo2 + self.palavra5[i]
		i+=1
	    if self.palavra5[i] == 'a':
		self.subsnovo2 = self.subsnovo2 + 'as'
	    else:
		self.subsnovo2 = self.subsnovo2 + 'os'
        return self.subsnovo2

a=frase()
b=palavra()
print('Frase com genero alterado: ')
b.genero()

a = frase()
b = palavra()
c = artigo()
c1 = c.palavraum()
c2 = c.palavraquatro()
d = verbo()
d1 = d.verbonovo()
e = substantivo()
e1= e.subs()
e2= e.subs2()

numero = c1 + " " +  e1 + " " + d1 + " " + c2 + " " + e2
print ('Frase com numero alterado: ')
print numero

# ERRO 1 11 100
# ERRO 1 14 50
# ERRO 1 15 50

# Programa não funciona
# ERRO 1 3 100
# ERRO 1 4 100
# ERRO 1 5 100
# ERRO 1 6 100
# ERRO 1 7 100
