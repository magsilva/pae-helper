"""
Alunos:
    Andreza Miqueletti        -  3672701
    Alexandre Branda Viriato  -  3167972
    Rodrigo Mithuhiro Oshiro  -  3528863
"""
class Palavra:
    def __init__(self,palavra):
        self.palavra = palavra.lower()
    def altera_genero(self):
        pass
    def altera_numero(self):
        pass
    def __str__(self):
        return self.palavra

class Substantivo(Palavra):
    def __init__(self,palavra):
        Palavra.__init__(self,palavra)
    def altera_genero(self):
        if self.palavra[-1]=='s':
            if self.palavra[-2]=='o':
                self.palavra = self.palavra[0:-2] + 'as'
            elif self.palavra[-2]=='a':
                self.palavra = self.palavra[0:-2] + 'os'
        elif self.palavra[-1]=='o':
            self.palavra = self.palavra[0:-1] + 'a'
        elif self.palavra[-1]=='a':
            self.palavra = self.palavra[0:-1] + 'o'
    def altera_numero(self):
        if self.palavra[-1]=='s':
            self.palavra = self.palavra[0:-1]
        else:
            self.palavra += 's'

class Verbo(Palavra):
    def __init__(self,palavra):
        Palavra.__init__(self,palavra)
    def altera_numero(self):
        if self.palavra[-1] != 'm':
            self.palavra += 'm'
        else:
           self.palavra = self.palavra[0:-1]

class VerboAr(Verbo):
    def __init__(self,palavra):
        Verbo.__init__(self,palavra)

class VerboEr(Verbo):
    def __init__(self,palavra):
        Verbo.__init__(self,palavra)

class VerboIr(Verbo):
    def __init__(self,palavra):
        Verbo.__init__(self,palavra)    

class Artigo(Palavra):
    def __init__ (self,palavra):
        Palavra.__init__(self,palavra)

class ArtigoDefinido(Artigo):
    def __init__ (self,palavra):
        Artigo.__init__(self,palavra)
    def altera_genero(self):
        if self.palavra[-1]=='s':
            if self.palavra[-2]=='o':
                self.palavra = self.palavra[0:-2] + 'as'
            elif self.palavra[-2]=='a':
                self.palavra = self.palavra[0:-2] + 'os'
        elif self.palavra[-1]=='o':
            self.palavra = self.palavra[0:-1] + 'a'
        elif self.palavra[-1]=='a':
            self.palavra = self.palavra[0:-1] + 'o'
    def altera_numero(self):
        if self.palavra[-1] == 's':
            self.palavra = self.palavra[0:-1]
        else:
            self.palavra += 's'

class ArtigoIndefinido(Artigo):
    def __init__ (self,palavra):
        Artigo.__init__(self,palavra)
    def altera_genero(self):
        if self.palavra[-1]=='s':
            if self.palavra[-2]=='n':
                self.palavra = self.palavra[0:-2] + 'mas'
            elif self.palavra[-2]=='a':
                self.palavra = self.palavra[0:-3] + 'ns'
        elif self.palavra[-1]=='m':
            self.palavra += 'a'
        else:
            self.palavra = self.palavra[0:-1]
    def altera_numero(self):
        if self.palavra[-2]=='n':
            self.palavra = self.palavra[0:-2] + 'm'
        elif self.palavra[-1]=='s':
            self.palavra = self.palavra[0:-1]
        elif self.palavra[-1]=='a':
            self.palavra += 's'
        elif self.palavra[-1]=='m':
            self.palavra = self.palavra[0:-1] + 'ns'

def escolhe(palavra):
    if 'm' in palavra:
        return ArtigoIndefinido(palavra)
    elif 'n' in palavra:
        return ArtigoIndefinido(palavra)
    else:
        return ArtigoDefinido(palavra)

class Frase:
    def __init__(self,file):
        self.file = open(file,"r")
    def resultado(self):
        linha = self.file.readline()
        while linha:
            if linha[0] == '\n':
                linha = self.file.readline()
                continue
            array = linha.split(" ")
            primeiro_artigo = escolhe(array[0])
            primeiro_substantivo = Substantivo(array[1])
            verbo = Verbo(array[2])
            segundo_artigo = escolhe(array[3])
            segundo_substantivo = Substantivo(array[4][0:-1])
            p = primeiro_artigo.palavra.capitalize()
            print "%s %s %s %s %s." % (p,primeiro_substantivo,verbo,segundo_artigo,segundo_substantivo)
            primeiro_artigo.altera_numero()
            primeiro_substantivo.altera_numero()
            verbo.altera_numero()
            segundo_artigo.altera_numero()
            segundo_substantivo.altera_numero()
            p = primeiro_artigo.palavra.capitalize()
            print "%s %s %s %s %s." % (p,primeiro_substantivo,verbo,segundo_artigo,segundo_substantivo)
            primeiro_artigo = escolhe(array[0])
            primeiro_substantivo = Substantivo(array[1])
            verbo = Verbo(array[2])
            segundo_artigo = escolhe(array[3])
            segundo_substantivo = Substantivo(array[4][0:-1])
            primeiro_artigo.altera_genero()
            primeiro_substantivo.altera_genero()
            segundo_artigo.altera_genero()
            segundo_substantivo.altera_genero()
            p = primeiro_artigo.palavra.capitalize()
            print "%s %s %s %s %s." % (p,primeiro_substantivo,verbo,segundo_artigo,segundo_substantivo)
            linha = self.file.readline()
        self.file.close()

def do():
    f = Frase("teste.txt")
    f.resultado()

do()

# ERRO 1 9 50
# ERRO 1 11 50
# ERRO 1 12 100
# ERRO 1 14 15
# ERRO 1 15 50
