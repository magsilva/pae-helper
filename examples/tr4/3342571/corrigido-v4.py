class frase:
    def __init__(self):
        self.f = open('frases.txt', 'r') #editar arquivo antes
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
	if self.palavra4[-1] == 'a':
	    artigo4 = "um"
	if self.palavra4[-1] == 'o':
	    artigo4 = "uma"
	gener = self.palavra1 + " " + self.palavra5 + " " + self.palavra3 + " " + artigo4 + " " + self.palavra2 #chame palavra.genero para mudanca de genero()
	print gener
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
        return self.artigonovo
    def palavraquatro(self):
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
        self.subsnovo = self.palavra2 + 's'
        return self.subsnovo
    def subs2(self):
        self.subsnovo2 = self.palavra5 + 's'
        return self.subsnovo2


def numero():
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
    b.genero()
    
numero()

# ERRO 1 3 50
# ERRO 1 8 100
# ERRO 1 11 100
# ERRO 1 12 100
# ERRO 1 14 50
# ERRO 1 15 50

# O programa não funciona.
# ERRO 1 3 100
# ERRO 1 4 100
# ERRO 1 5 100
# ERRO 1 6 100
# ERRO 1 7 100
