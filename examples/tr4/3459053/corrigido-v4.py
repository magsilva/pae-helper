# Alunos : Alessandra Kelli Barbato          no. USP: 3459053
#          Marcos Fabio Martins              no. USP: 3458100
#          Ottone Alexandre Traldi           no. USP: 3457749

class Frase:
    def __init__(self, xfrase = ""):   
        if type(xfrase) is type(""): 
            self.frase = xfrase.split(' ')
        else:
            self.frase = []

    def Genero (self):
        if self.frase[0][0].upper() == 'O' or self.frase[0][0].upper() == 'A':
            artigo = Artigo_Definido (self.frase[0])
            artigo.altera_genero() 
            temp = artigo.art_def + ' '
        else:
            artigo = Artigo_Indefinido (self.frase[0])
            artigo.altera_genero() 
            temp = artigo.art_indef + ' '

        subs = Substantivo(self.frase[1])
        subs.altera_genero()
        temp += subs.substantivo + ' ' + self.frase[2] + ' '

        if self.frase[3][0].upper() == 'O' or self.frase[3][0].upper() == 'A':
            artigo = Artigo_Definido (self.frase[3])
            artigo.altera_genero() 
            temp += artigo.art_def + ' '
        else:
            artigo = Artigo_Indefinido (self.frase[3])
            artigo.altera_genero()
            temp += artigo.art_indef + ' '

        subs = Substantivo(self.frase[4])
        subs.altera_genero()
        temp += subs.substantivo

        return temp


    def Numero (self):
        if self.frase[0][0].upper() == 'O' or self.frase[0][0].upper() == 'A':
            artigo = Artigo_Definido (self.frase[0])
            artigo.altera_numero() 
            temp = artigo.art_def + ' '
        else:
            artigo = Artigo_Indefinido (self.frase[0])
            artigo.altera_numero() 
            temp = artigo.art_indef + ' '

        subs = Substantivo(self.frase[1])
        subs.altera_numero()
        temp += subs.substantivo + ' '

        vrb = Verbo (self.frase[2])
        vrb.altera_numero()
        temp += vrb.verbo + ' '

        if self.frase[3][0].upper() == 'O' or self.frase[3][0].upper() == 'A':
            artigo = Artigo_Definido (self.frase[3])
            artigo.altera_numero() 
            temp += artigo.art_def + ' '
        else:
            artigo = Artigo_Indefinido (self.frase[3])
            artigo.altera_numero()
            temp += artigo.art_indef + ' '

        subs = Substantivo(self.frase[4])
        subs.altera_numero()
        temp += subs.substantivo

        return temp
    
        
class Palavra (object):
    def __init__(self, x_plv = ''):
        self.palavra = x_plv

    def altera_numero (self):
        pass

    def altera_genero (self):
        pass


class Artigo (Palavra):
    def __init__(self, x_art = ''):
        self.artigo = x_art

    def altera_numero (self):
        pass

    def altera_genero (self):
        pass


class Substantivo (Palavra):
    def __init__(self, x_sub = ''):
        self.substantivo = x_sub

    def altera_numero (self):
        if self.substantivo[-1:].upper() == 'S':
            self.substantivo = self.substantivo[:-1]
        else:
            self.substantivo = self.substantivo + 's'
        
    def altera_genero (self):
        if self.substantivo[-1:].upper() == 'O':
            self.substantivo = self.substantivo[:-1] + 'a'
        elif self.substantivo[-1:].upper() == 'A':    
            self.substantivo = self.substantivo[:-1] + 'o'
        elif self.substantivo[-2:].upper() == 'OS':        
            self.substantivo = self.substantivo[:-2] + 'as'
        elif self.substantivo[-2:].upper() == 'AS':    
            self.substantivo = self.substantivo[:-2] + 'os'
        

class Verbo (Palavra):
    def __init__(self, x_vrb = ''):
        self.verbo = x_vrb

    def altera_numero (self):
        if self.verbo[-1:].upper() == 'M':
            self.verbo = self.verbo[:-1]
        else:
            self.verbo = self.verbo + 'm'


    def altera_genero (self):
        pass

            

class Artigo_Definido (Artigo):
    def __init__(self, x_artigo = ''):
        if str.upper(x_artigo) == 'O' or str.upper(x_artigo) == 'A' or str.upper(x_artigo) == 'OS' or str.upper(x_artigo) == 'AS':
            self.art_def = x_artigo
        else:
            self.art_def = ''

    def altera_numero (self):
        if str.upper(self.art_def) == 'O' or str.upper(self.art_def) == 'A':
            self.art_def = self.art_def + 's'
        else:
            self.art_def = self.art_def[:-1]

    def altera_genero (self):
        if self.art_def[0] == 'O':
	    self.art_def = 'A' + self.art_def[1:]
        elif  self.art_def[0] == 'o':
	    self.art_def = 'a' + self.art_def[1:]
        elif self.art_def[0] == 'A':
	    self.art_def = 'O' + self.art_def[1:]
        elif self.art_def[0] == 'a':
	    self.art_def = 'o' + self.art_def[1:]



class Artigo_Indefinido (Artigo):
    def __init__(self, x_artigo = ''):
        if str.upper(x_artigo) == 'UM' or str.upper(x_artigo) == 'UMA' or str.upper(x_artigo) == 'UNS' or str.upper(x_artigo) == 'UMAS':
            self.art_indef = x_artigo
        else:
            self.art_indef = ''

    def altera_numero (self):
        if self.art_indef.upper() == 'UM':
            self.art_indef = self.art_indef[0] + 'ns'
        elif self.art_indef.upper() == 'UMA':
            self.art_indef = self.art_indef + 's'
        elif self.art_indef.upper() == 'UNS':
            self.art_indef = self.art_indef[0] + 'm' 
        elif self.art_indef.upper() == 'UMA':
            self.art_indef = self.art_indef[:-1]
            
    def altera_genero (self):
        if self.art_indef.upper() == 'UM': 
            self.art_indef = self.art_indef + 'a'
        elif self.art_indef.upper() == 'UNS':
            self.art.indef = self.art_indef[:-2] + 'mas'
        elif self.art_indef.upper() == 'UMA':
            self.art_indef = self.art_indef[:-1]
        elif self.art_indef.upper() == 'UMAS':
            self.art_indef = self.art_indef[:-3] + 'ns'

class Primeira_Conjugacao (Verbo):
    def __init__(self, x_pri = ''):
        self.pri = x_pri

class Segunda_Conjugacao (Verbo):
    def __init__(self, x_seg = ''):
        self.seg = x_seg

class Terceira_Conjugacao (Verbo):
    def __init__(self, x_ter = ''):
        self.ter = x_ter

nome_arquivo = raw_input ("Nome do arquivo de entrada: ")
file_in = file(nome_arquivo,'r')
frases = file_in.read().split('\n')
file_in.close()

for i in range(0, len(frases)):
    f = Frase (frases[i])
    temp = ''
    for i in range(0, len(f.frase)):
        temp += f.frase[i] + ' '

    print '\nFrase original: '+ temp
    print 'Frase com numero alterado: ' + f.Numero()
    print 'Frase com genero alterado: ' + f.Genero()

# ERRO 1 9 5
# ERRO 1 11 50
# ERRO 1 14 15
# ERRO 1 15 50
