# Lista de Exercicios 4 - P.O.O. - 25/04/2003
#
# Alunos:
# Fabio Margarido  nUSP: 3459647
# Marcus Vinicius Secato  nUSP: 3285140
# Jose Arnaldo M. de Holanda  nUSP: 3564502


import string

######## CLASSE PALAVRA #################

class Palavra:

    def __init__(self, word):
        self.palavra = word

######## CLASSE ARTIGO ##################

class Artigo(Palavra):

    def __init__(self,art):
        Palavra.__init__(self,art)

######## CLASSE ARTIGO DEFINIDO #########

class ArtigoDefinido(Artigo):

    def __init__(self,definido):
        Artigo.__init__(self,definido)

    def numero(self):

        if self.palavra == 'o':
            self.palavra = 'os'
        elif self.palavra == 'a':
            self.palavra = 'as'
        elif self.palavra == 'os':
            self.palavra = 'o'
        elif self.palavra == 'as':
            self.palavra = 'a'
        return self.palavra

    def genero(self):

        if self.palavra == 'o':
            self.palavra = 'a'
        elif self.palavra == 'a':
            self.palavra = 'o'
        elif self.palavra == 'os':
            self.palavra = 'as'
        elif self.palavra == 'as':
            self.palavra = 'os'
        return self.palavra

######### CLASSE ARTIGO INDEFINIDO #####

class ArtigoIndefinido(Artigo):

    def __init__ (self,indefinido):
        Artigo.__init__(self,indefinido)

    def numero(self):

        if self.palavra == 'um':
            self.palavra = 'uns'
        elif self.palavra == 'uma':
            self.palavra = 'umas'
        elif self.palavra == 'uns':
            self.palavra = 'um'
        elif self.palavra == 'umas':
            self.palavra = 'uma'
        return self.palavra

    def genero(self):

        if self.palavra == 'um':
            self.palavra = 'uma'
        elif self.palavra == 'uma':
            self.palavra = 'um'
        elif self.palavra == 'uns':
            self.palavra = 'umas'
        elif self.palavra == 'umas':
            self.palavra = 'uns'
        return self.palavra
    


######### CLASSE SUBSTANTIVO ###########

class Substantivo(Palavra):

    def __init__ (self,subs):
        Palavra.__init__(self,subs)

    def numero(self):

        if self.palavra[-1] != 's':
            self.palavra += 's'
        elif self.palavra[-1] == 's':
            self.palavra = self.palavra[:-1]

        return self.palavra

    def genero(self):

        if self.palavra[-1] == 'o':
            self.palavra = self.palavra[:-1] + 'a'
        elif self.palavra[-1] == 'a':
            self.palavra = self.palavra[:-1] + 'o'
        elif self.palavra[-2:] == 'os':
            self.palavra = self.palavra[:-2] + 'as'
        elif self.palavra[-2:] == 'as':
            self.palavra = self.palavra[:-2] + 'os'
 
        return self.palavra

######### CLASSE VERBO ################

class Verbo(Palavra):

    def __init__ (self,verb):
        Palavra.__init__(self,verb)

#### CLASSE PRIMEIRA CONJUGACAO #######

class PC (Verbo):

    def __init__ (self,pc):
        Verbo.__init__(self,pc)

    def numero(self):

	if self.palavra[-1] == 'a':
	    self.palavra += 'm'
	elif self.palavra[-1] == 'm':
	    self.palavra = self.palavra[:-1]

	return self.palavra

#### CLASSE SEGUNDA CONJUGACAO #######

class SC (Verbo):

    def __init__ (self, sc):
	Verbo.__init__(self,sc)

    def numero(self):

	if self.palavra[-1] == 'e':
	    self.palavra += 'm'
	elif self.palavra[-1] == 'm':
	    self.palavra = self.palavra[:-1]

	return self.palavra

#### TERCEIRA SEGUNDA CONJUGACAO #####

class TC (Verbo):

    def __init__ (self, tc):
	Verbo.__init__(self,tc)

    def numero(self):

	if self.palavra[-1] == 'e':
	    self.palavra += 'm'
	elif self.palavra[-1] == 'i':
	    self.palavra = self.palavra[:-1] + 'em'
	elif self.palavra[-1] == 'm':
	    self.palavra = self.palavra[:-1]

	return self.palavra

############ CLASSE FRASE ############


class frase:

    def __init__ (self):
	fp = open("frases.txt",'r') 
	frase = fp.readline()

	if frase[-1] == '\n':
            frase = frase[:-1]

	self.aux = []
	self.aux1 = []
	while frase != '':
		lista = frase.split(' ')             
		self.numero(lista)
		self.genero(lista)
		frase = fp.readline()
		if frase != '' and frase[-1] == '\n':
                    frase = frase[:-1]
		self.aux = []
		self.aux1 = []
		
    def numero(self,lista):
        word = ''
	## primeiro artigo ##
	if lista[0] in ['o','a','os','as']:
		ca = ArtigoDefinido(lista[0])
		self.aux.append(ca.numero())
	elif lista[0] in ['um','uma','uns','umas']:
		ca = ArtigoIndefinido(lista[0])
		self.aux.append(ca.numero())
   
	## primeiro substantivo ##
	cs = Substantivo(lista[1])
	self.aux.append(cs.numero())

	## verbo ##
	if lista[2][-1] == 'a' or lista[2][-2:] == 'am':
		cv = PC(lista[2])
		self.aux.append(cv.numero())
	elif lista[2][-1] == 'e' or lista[2][-2:] == 'em':
		cv = SC(lista[2])
		self.aux.append(cv.numero())
	elif lista[2][-1] == 'i':
		cv = TC(lista[2])
		self.aux.append(cv.numero())

	## segundo artigo ##
	if lista[3] in ['o','a','os','as']:
		ca2 = ArtigoDefinido(lista[3])
		self.aux.append(ca2.numero())
	elif lista[3] in ['um','uma','uns','umas']:
		ca2 = ArtigoIndefinido(lista[3])
		self.aux.append(ca2.numero())

	## segundo substantivo ##

	cs2 = Substantivo(lista[4])
	self.aux.append(cs2.numero())

	i =0
	while(i<5):
            word += self.aux[i] + ' '
            i += 1

        print word.capitalize()

    def genero(self, lista):
        word = ''

        ## primeiro artigo ##
        if lista[0] in ['o','a','os','as']:
		ca = ArtigoDefinido(lista[0])
		self.aux1.append(ca.genero())
	elif lista[0] in ['um','uma','uns','umas']:
		ca = ArtigoIndefinido(lista[0])
		self.aux1.append(ca.genero())

	## primeiro substantivo ##
	cs = Substantivo(lista[1])
	self.aux1.append(cs.genero())

        ## verbo ##
        self.aux1.append(lista[2])
	

	## segundo artigo ##
	if lista[3] in ['o','a','os','as']:
		ca2 = ArtigoDefinido(lista[3])
		self.aux1.append(ca2.genero())
	elif lista[3] in ['um','uma','uns','umas']:
		ca2 = ArtigoIndefinido(lista[3])
		self.aux1.append(ca2.genero())

	## segundo substantivo ##

	cs2 = Substantivo(lista[4])
	self.aux1.append(cs2.genero())

	i =0
	while(i<5):
            word += self.aux1[i] + ' '
            i += 1

        print word.capitalize() + '\n'

a = frase()

# ERRO 1 3 100
# ERRO 1 8 100
# ERRO 1 11 50
# ERRO 1 15 100
