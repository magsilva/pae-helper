#################################
# Lucas Antiqueira, 3457180     #
# 4a Lista de Exercicios - POO  #
#################################

class Frase:
    def __init__(self, frase):
        self.palavras = frase.split(' ')
        if self.palavras[0] == 'a' or self.palavras[0] == 'as' or self.palavras[0] == 'o' or self.palavras[0] == 'os':
            self.art1 = Artigo_definido(self.palavras[0])
        else:
            self.art1 = Artigo_indefinido(self.palavras[0])
        self.subst1 = Substantivo(self.palavras[1])
        if self.palavras[2].endswith('a') or self.palavras[2].endswith('am'):
            self.verbo = Prim_conjugacao(self.palavras[2])
        else:
            self.verbo = Seg_conjugacao(self.palavras[2])            
        if self.palavras[3] == 'a' or self.palavras[3] == 'as' or self.palavras[3] == 'o' or self.palavras[3] == 'os':
            self.art2 = Artigo_definido(self.palavras[3])
        else:
            self.art2 = Artigo_indefinido(self.palavras[3])
        self.subst2 = Substantivo(self.palavras[4])

    def muda_genero(self):
        self.art1.muda_genero()
        self.subst1.muda_genero()
        self.art2.muda_genero()
        self.subst2.muda_genero()        
    def muda_numero(self):
        self.art1.muda_numero()
        self.subst1.muda_numero()
        self.verbo.muda_numero()
        self.art2.muda_numero()
        self.subst2.muda_numero()        
    def escreve_frase(self):
        print self.art1.le_palavra(), self.subst1.le_palavra(), self.verbo.le_palavra(), self.art2.le_palavra(), self.subst2.le_palavra()

class Palavra:
    def __init__(self, palavra):
        self.palavra = palavra
    def le_palavra(self):
        return self.palavra

class Artigo(Palavra):
    pass

class Artigo_definido(Artigo):
    def __init__(self, palavra):
        Artigo.__init__(self, palavra)
        if self.palavra == 'a':
            self.fem = 1
            self.pl = 0
        elif self.palavra == 'as':
            self.fem = 1
            self.pl = 1
        elif self.palavra == 'o':
            self.fem = 0
            self.pl = 0
        elif self.palavra == 'os':
            self.fem = 0
            self.pl = 1
    def muda_genero(self):
        if self.fem == 1:
            self.fem = 0
            if self.palavra == 'a':
                self.palavra = 'o'
            else:
                self.palavra = 'os'
        else:
            self.fem = 1
            if self.palavra == 'o':
                self.palavra = 'a'
            else:
                self.palavra = 'as'
    def muda_numero(self):
        if self.pl == 1:
            self.pl = 0
            if self.palavra == 'as':
                self.palavra = 'a'
            else:
                self.palavra = 'o'
        else:
            self.pl = 1
            if self.palavra == 'o':
                self.palavra = 'os'
            else:
                self.palavra = 'as'

class Artigo_indefinido(Artigo):
    def __init__(self, palavra):
        Artigo.__init__(self, palavra)
        if self.palavra == 'uma':
            self.fem = 1
            self.pl = 0
        elif self.palavra == 'umas':
            self.fem = 1
            self.pl = 1
        elif self.palavra == 'um':
            self.fem = 0
            self.pl = 0
        elif self.palavra == 'uns':
            self.fem = 0
            self.pl = 1
    def muda_genero(self):
        if self.fem == 1:
            self.fem = 0
            if self.palavra == 'uma':
                self.palavra = 'um'
            else:
                self.palavra = 'uns'
        else:
            self.fem = 1
            if self.palavra == 'um':
                self.palavra = 'uma'
            else:
                self.palavra = 'umas'
    def muda_numero(self):
        if self.pl == 1:
            self.pl = 0
            if self.palavra == 'umas':
                self.palavra = 'uma'
            else:
                self.palavra = 'um'
        else:
            self.pl = 1
            if self.palavra == 'um':
                self.palavra = 'uns'
            else:
                self.palavra = 'umas'

class Substantivo(Palavra):
    def __init__(self, palavra):
        Palavra.__init__(self, palavra)
        if self.palavra.endswith('a'):
            self.fem = 1
            self.pl = 0
        elif self.palavra.endswith('as'):
            self.fem = 1
            self.pl = 1
        elif self.palavra.endswith('o'):
            self.fem = 0
            self.pl = 0
        elif self.palavra.endswith('os'):
            self.fem = 0
            self.pl = 1
    def muda_genero(self):
        if self.fem == 1:
            self.fem = 0
            if self.palavra.endswith('a'):
                self.palavra = self.palavra[0:-1] + 'o'
            else:
                self.palavra = self.palavra[0:-2] + 'os'
        else:
            self.fem = 1
            if self.palavra.endswith('o'):
                self.palavra = self.palavra[0:-1] + 'a'
            else:
                self.palavra = self.palavra[0:-2] + 'as'
    def muda_numero(self):
        if self.pl == 1:
            self.pl = 0
            if self.palavra.endswith('as'):
                self.palavra = self.palavra[0:-1]
            else:
                self.palavra = self.palavra[0:-1]
        else:
            self.pl = 1
            if self.palavra.endswith('o'):
                self.palavra = self.palavra[0:-1] + 'os'
            else:
                self.palavra = self.palavra[0:-1] + 'as'


class Verbo(Palavra):
    pass

class Prim_conjugacao(Verbo):
    def __init__(self, palavra):
        Palavra.__init__(self, palavra)
        if self.palavra.endswith('a'):
            self.pl = 0
        elif self.palavra.endswith('am'):
            self.pl = 1
    def muda_numero(self):
        if self.pl == 1:
            self.pl = 0
            self.palavra = self.palavra[0:-1]
        else:
            self.pl = 1
            self.palavra += 'm'

#Eh o mesmo para a terceira conjugacao (para os verbos usados neste exemplo)
class Seg_conjugacao(Verbo):
    def __init__(self, palavra):
        Palavra.__init__(self, palavra)
        if self.palavra.endswith('e'):
            self.pl = 0
        elif self.palavra.endswith('em'):
            self.pl = 1
    def muda_numero(self):
        if self.pl == 1:
            self.pl = 0
            self.palavra = self.palavra[0:-1]
        else:
            self.pl = 1
            self.palavra += 'm'




file = open('lista_4.txt', 'r')
line = file.readline()
while line != '':
    if line.endswith('\n'):
        line = line[0:-1] #tira quebra de linha
    f = Frase(line)
    f.escreve_frase()
    f.muda_numero()
    f.escreve_frase()
    f.muda_numero()
    f.muda_genero()
    f.escreve_frase()
    print '\n'
    line = file.readline()

# Programa não funciona
# ERRO 1 3 100
# ERRO 1 4 100
# ERRO 1 5 100
# ERRO 1 6 100
# ERRO 1 7 100

# ERRO 1 11 50
# ERRO 1 15 50
