# ERRO 1 16 50
# ERRO 1 12 100
# ERRO 1 11 50

class frase:
    def __init__(self, frase_x = ""):   
        self.palavra_atual = frase_x.split(' ')
        
    def genero (self):
        if self.palavra_atual[0][0] == 'O' or self.palavra_atual[0][0] == 'A' or self.palavra_atual[0][0] == 'a' or self.palavra_atual[0][0] == 'o':
            artigo = artigo_Definido (self.palavra_atual[0])
            artigo.altera_genero() 
            temp = artigo.art_def + ' '
        else:
            artigo = artigo_Indefinido (self.palavra_atual[0])
            artigo.altera_genero() 
            temp = artigo.art_indef + ' '

        subs = substantivo(self.palavra_atual[1])
        subs.altera_genero()
        temp += subs.substantivo + ' ' + self.palavra_atual[2] + ' '

        if self.palavra_atual[3][0] == 'O' or self.palavra_atual[3][0] == 'A' or self.palavra_atual[3][0] == 'o' or self.palavra_atual[3][0] == 'a':
            artigo = artigo_Definido (self.palavra_atual[3])
            artigo.altera_genero() 
            temp += artigo.art_def + ' '
        else:
            artigo = artigo_Indefinido (self.palavra_atual[3])
            artigo.altera_genero()
            temp += artigo.art_indef + ' '

        subs = substantivo(self.palavra_atual[4])
        subs.altera_genero()
        temp += subs.substantivo

        return temp


    def numero (self):
        if self.palavra_atual[0][0].upper() == 'O' or self.palavra_atual[0][0].upper() == 'A':
            artigo = artigo_Definido (self.palavra_atual[0])
            artigo.altera_numero() 
            temp = artigo.art_def + ' '
        else:
            artigo = artigo_Indefinido (self.palavra_atual[0])
            artigo.altera_numero() 
            temp = artigo.art_indef + ' '

        subs = substantivo(self.palavra_atual[1])
        subs.altera_numero()
        temp += subs.substantivo + ' '

        vrb = verbo(self.palavra_atual[2])
        vrb.altera_numero()
        temp += vrb.verb + ' '

        if self.palavra_atual[3].upper() == 'O' or self.palavra_atual[3].upper() == 'A':
            artigo = artigo_Definido (self.palavra_atual[3])
            artigo.altera_numero() 
            temp += artigo.art_def + ' '
        else:
            artigo = artigo_Indefinido (self.palavra_atual[3])
            artigo.altera_numero()
            temp += artigo.art_indef + ' '

        subs = substantivo(self.palavra_atual[4])
        subs.altera_numero()
        temp += subs.substantivo

        return temp
    
        
class palavra (object):
    def __init__(self, x = ''):
        self.palavra = x

    def altera_numero (self):
        pass

    def altera_genero (self):
        pass


class artigo (palavra):
    def __init__(self, art = ''):
        self.artigo = art

    def altera_numero (self):
        pass

    def altera_genero (self):
        pass
    
class artigo_Definido (artigo):
    def __init__(self, x_artigo = ''):
        self.art_def = x_artigo
        
    def altera_numero (self):
        if self.art_def == 'O':
            self.art_def = "Os"
        elif self.art_def == 'A':
            self.art_def = "As"
        if self.art_def == "a":
            self.art_def = "as"
        elif self.art_def == "o":
            self.art_def = "os"

    def altera_genero (self):
       if self.art_def[0] == 'O':
	    self.art_def = 'A'
       elif self.art_def[0] == 'o':
           self.art_def = 'a'
       elif self.art_def[0] == 'A':
           self.art_def = 'O'
       elif self.art_def[0] == 'a':
           self.art_def = 'o'
            
class artigo_Indefinido (artigo):
    def __init__(self, x_artigo = ''):
            self.art_indef = x_artigo

    def altera_numero (self):
        if self.art_indef == 'um':
            self.art_indef = 'uns'
        if self.art_indef == 'uma':
            self.art_indef = 'umas'
        if self.art_indef == 'Um':
            self.art_indef = 'Uns'
        if self.art_indef == 'Uma':
            self.art_indef = 'Umas'       
         
    def altera_genero (self):
        if self.art_indef == 'Um': 
            self.art_indef = self.art_indef + 'a'
        elif self.art_indef == 'Uns':
            self.art.indef = self.art_indef[:-2] + 'mas'
        elif self.art_indef == 'Uma':
            self.art_indef = self.art_indef[:-1]
        elif self.art_indef == 'Umas':
            self.art_indef = self.art_indef[:-3] + 'ns'
        elif self.art_indef == 'um':
            self.art_indef = self.art_indef + 'a'
        elif self.art_indef == 'uns':
            self.art.indef = self.art_indef[:-2] + 'mas'
        elif self.art_indef == 'uma':
            self.art_indef = self.art_indef[:-1]
        elif self.art_indef == 'umas':
            self.art_indef = self.art_indef[:-3] + 'ns'

class substantivo (palavra):
    def __init__(self, sub = ''):
        self.substantivo = sub

    def altera_numero (self):
        self.substantivo = self.substantivo + 's'
        
    def altera_genero (self):
        if self.substantivo[-1] == "a":
            a = len(self.substantivo)
            self.substantivo = self.substantivo[0:a-1] + "o"
        elif self.substantivo[-1] == "o":
            a = len(self.substantivo)
            self.substantivo = self.substantivo[0:a-1] + "a"        

class verbo (palavra):
    def __init__(self, verb = ''):
        self.verb = verb

    def altera_numero (self):
        self.verb = self.verb + 'm'


    def altera_genero (self):
        pass

class primeira_Conjugacao (verbo):
    def __init__(self, pri = ''):
        self.pri = pri

class segunda_Conjugacao (verbo):
    def __init__(self, seg = ''):
        self.seg = seg

class terceira_Conjugacao (verbo):
    def __init__(self, ter = ''):
        self.ter = ter
            
fd = open("frases.txt")
frases = fd.read().split('\n')
for i in range(0, len(frases)):
    f = frase (frases[i])
    print 'Frase com numero alterado: ' + f.numero()
    print 'Frase com genero alterado: ' + f.genero()
