# Exercicio sobre heranca
# Koji E. Sasaoka 3560665

class Palavra :
    def __init__ (self, valor):
        self.texto = valor

    def genero (self):
        pass

    def numero (self):
        pass

    def __str__ (self):
        return self.texto

    def t (self) :
        return self.texto


class Subst (Palavra):
    def __init__ (self, t):
        Palavra.__init__ (self, t)

    def numero(self):
        if self.texto[-1] != 'S':
            self.texto += 'S'
        elif self.texto[-2:] == 'AS':
            self.texto = self.texto[:-2] + 'A'
        elif self.texto[-2:] == 'OS':
            self.texto = self.texto[:-2] + 'O'

    def genero(self):
        if self.texto[-1] == 'O':
            self.texto = self.texto[:-1] + 'A'
        elif self.texto[-1] == 'A':
            self.texto = self.texto[:-1] + 'O'
        elif self.texto[-2:] == 'AS':
            self.texto = self.texto[:-2] + 'OS'
        elif self.texto[-2:] == 'OS':
            self.texto = self.texto[:-2] + 'AS'
    
class Artigo (Palavra) :
    def __init__ (self, art):
        Palavra.__init__ (self, art)

class ArtigoDefinido (Artigo) :
    def __init__ (self, art):
        Artigo.__init__ (self, art)

    def genero (self) :
        if self.texto == 'O':
            self.texto = 'A'
        elif self.texto == 'A':
            self.texto = 'O'        
        elif self.texto == 'AS':
            self.texto = 'OS'        
        elif self.texto == 'OS':
            self.texto = 'AS'        

    def numero (self) :
        if self.texto == 'O':
            self.texto = 'OS'
        elif self.texto == 'A':
            self.texto = 'AS'        
        elif self.texto == 'AS':
            self.texto = 'A'        
        elif self.texto == 'OS':
            self.texto = 'O'        
        
class ArtigoIndefinido (Artigo) :
    def __init__ (self, art):
        Artigo.__init__ (self, art)
    def genero (self) :
        if self.texto == 'UM':
            self.texto = 'UMA'
        elif self.texto == 'UMA':
            self.texto = 'UM'        
        elif self.texto == 'UNS':
            self.texto = 'UMAS'        
        elif self.texto == 'UMAS':
            self.texto = 'UNS'        

    def numero (self) :
        if self.texto == 'UM':
            self.texto = 'UNS'
        elif self.texto == 'UMA':
            self.texto = 'UMAS'        
        elif self.texto == 'UMAS':
            self.texto = 'UMA'        
        elif self.texto == 'UNS':
            self.texto = 'UM'        


class Verbo (Palavra) :
    def __init__ (self, verb):
        Palavra.__init__ (self, verb)

class Pri_Conj (Verbo) :
    def __init__ (self, verbo_ar):
        Verbo.__init__ (self, verbo_ar)

    def numero (self) :
        if self.texto[-1] == 'A':
            self.texto += 'M'
        elif self.texto[-1] == 'M':
            self.texto = self.texto[:-2] + 'A'
       
class Seg_Conj (Verbo) :
    def __init__ (self, verbo_er):
        Verbo.__init__ (self, verbo_er)

    def numero (self) :
        if self.texto[-1] == 'E':
            self.texto += 'M'
        elif self.texto[-1] == 'M':
            self.texto = self.texto[:-2] + 'E'
        


class Ter_Conj (Verbo) :
    def __init__ (self, verbo_ir):
        Verbo.__init__ (self, verbo_ir)
    def numero (self) :
        if self.texto[-1] != 'M':
            self.texto = self.texto[:-1] + 'EM'
        else :
            self.texto = self.texto[:-2] + 'I'
        

class Frase :
    def __init__ (self, texto_frase) :
        import string
        lista = string.split(texto_frase)

        self.substantivo1 = Subst(lista[1])
        self.substantivo2 = Subst(lista[4])

        if lista[2][-1] == 'A':
            self.verbo = Pri_Conj (lista[2])
        elif lista[2][-1] == 'E':
            self.verbo = Seg_Conj (lista[2])
        elif lista[2][-1] == 'I':
            self.verbo = Ter_Conj (lista[2])
        
        if lista[0][0] == 'U':
            self.artigo1 = ArtigoIndefinido (lista[0])
        else :
            self.artigo1 = ArtigoDefinido (lista[0])

        if lista[3][0] == 'U':
            self.artigo2 = ArtigoIndefinido (lista[3])
        else :
            self.artigo2 = ArtigoDefinido (lista[3])

    def numero (self):
        self.verbo.numero()
        self.substantivo1.numero()
        self.substantivo2.numero()
        self.artigo2.numero()
        self.artigo1.numero()
        
    def genero (self):
        self.verbo.genero()
        self.substantivo1.genero()
        self.substantivo2.genero()
        self.artigo2.genero()
        self.artigo1.genero()

    def __str__(self):
        resultado = self.artigo1.t() + ' ' + self.substantivo1.t() + ' ' + self.verbo.t()
        resultado += ' ' + self.artigo2.t() + ' ' + self.substantivo2.t()
        return resultado
        
    def t(self):
        resultado = self.artigo1.t() + ' ' + self.substantivo1.t() + ' ' + self.verbo.t()
        resultado += ' ' + self.artigo2.t() + ' ' + self.substantivo2.t()
        return resultado

def Programa ():
    fp = open('teste.txt')

    dados = fp.readline()

    while dados != "":
        teste_frase = Frase (dados)
        print 'Frase Normal : ' + teste_frase.t()

        teste_frase.genero ()
        print 'Mudanca de Genero : ' + teste_frase.t()
        
        teste_frase.numero ()
        print 'Mudanca de Numero : ' + teste_frase.t()

        print ('\n')
        dados = fp.readline()

# ERRO 1 11 50
# ERRO 1 15 15

Programa()

# Programa não funciona
# ERRO 1 3 100
# ERRO 1 4 100
# ERRO 1 5 100
# ERRO 1 6 100
# ERRO 1 7 100
