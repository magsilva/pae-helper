#Marcelo Kenji Hotta    3460142 kenji@grad.icmc.usp.br
#Lista 4 - POO - Renata Pontin

class Arquivo(object):
    def __init__(self, nome):
        self.lista = []
        listatmp = []
        try:
            fp = open(nome)
            temp = fp.readlines()
            for linha in temp:
                if linha[-1] == "\n":
                    listatmp.append(linha[:-1])
                else:
                    listatmp.append(linha)
        except IOError:
            print "Arquivo", nome, "nao encontrado!"

        for frase in listatmp:
            self.lista.append(Frase(frase))

    def cont(self):
        temp = ""
        for frase in self.lista:
            temp = temp + frase.cont() + "\n" 
        return temp

    def genero(self):
        for frase in self.lista:
            for palavra in frase.lista:
                palavra.genero()

    def numero(self):
        for frase in self.lista:
            for palavra in frase.lista:
                palavra.numero()
        
    def __str__(self):
        return self.cont()
    

class Frase(object):
    def __init__(self,frase):
        temp=frase.split(" ")
        self.lista = [1, 2, 3, 4, 5]
        for i in [0, 3]:
            if temp[i] in ["o", "a", "os", "as"]:
                self.lista[i] = ArtigoDefinido(temp[i])
            else:
                self.lista[i] = ArtigoIndefinido(temp[i])
        for i in [1, 4]:
            self.lista[i] = Substantivo(temp[i])
        for i in [2]:
            if temp[i][-1] == "a":
                self.lista[i] = Verbo1(temp[i])
            elif temp[i][-1] == "e":
                self.lista[i] = Verbo2(temp[i])
            else:
                self.lista[i] = Verbo3(temp[i])

    def cont(self):
        temp = ""
        for x in self.lista:
            temp += x.palavra + " "
        return temp[:-1]

    def __str__(self):
        return self.cont()
        
class Palavra(object):
    def __init__(self, palavra):
        self.palavra = palavra

    def __str__(self):
        return self.palavra

class Artigo(Palavra):
    def __init__(self, art):
        Palavra.__init__(self, art)

class ArtigoDefinido(Artigo):
    def __init__(self, artd):
        Artigo.__init__(self, artd)

    def genero(self):
        if(self.palavra=='o'):
            self.palavra = 'a'
        elif(self.palavra=='a'):
            self.palavra =  'o'
        elif(self.palavra=='os'):
            self.palavra =  'as'
        elif(self.palavra=='as'):
            self.palavra =  'os'
            
    def numero(self):
        if(self.palavra=='o'):
            self.palavra =  'os'
        elif(self.palavra=='os'):
            self.palavra =  'o'
        elif(self.palavra=='a'):
            self.palavra =  'as'
        elif(self.palavra=='as'):
            self.palavra =  'a'

class ArtigoIndefinido(Artigo):
    def __init__(self,arti):
        Artigo.__init__(self,arti)

    def genero(self):
        if(self.palavra=='um'):
            self.palavra = 'uma'
        elif(self.palavra=='uma'):
            self.palavra = 'um'
        elif(self.palavra=='uns'):
            self.palavra =  'umas'
        elif(self.palavra=='umas'):
            self.palavra =  'uns'
            
    def numero(self):
        if(self.palavra=='um'):
            self.palavra = 'uns'
        elif(self.palavra=='uns'):
            self.palavra =  'um'
        elif(self.palavra=='uma'):
            self.palavra =  'umas'
        elif(self.palavra=='umas'):
            self.palavra =  'uma'            

class Substantivo(Palavra):
    def __init__(self, sub):
        Palavra.__init__(self, sub)

    def genero(self):
        if(self.palavra[-1]=='o'):
            self.palavra =  self.palavra[:-1]+'a'
        elif(self.palavra[-1]=='a'):
            self.palavra =  self.palavra[:-1]+'o'
        elif(self.palavra[-2:]=='os'):
            self.palavra =  self.palavra[:-2]+'as'
        elif(self.palavra[-2:]=='as'):
            self.palavra =  self.palavra[:-2]+'os'
            
    def numero(self):
        if(self.palavra[-1]=='o'):
            self.palavra =  self.palavra[:-1]+'os'
        elif(self.palavra[-1]=='a'):
            self.palavra =  self.palavra[:-1]+'as'
        elif(self.palavra[-2:]=='as'):
            self.palavra =  self.palavra[:-2]+'a'
        elif(self.palavra[-2:]=='os'):
            self.palavra =  self.palavra[:-2]+'o'

    

class Verbo(Palavra):
    def __init__(self, ver):
        Palavra.__init__(self, ver)

class Verbo1(Verbo):
    def __init__(self,conj1):
        Verbo.__init__(self,conj1)

    def genero(self):
        return self.palavra

    def numero(self):
        if(self.palavra[-1]=='a'):
            self.palavra =  self.palavra + 'm'
        else:
            self.palavra =  self.palavra[:-1]

class Verbo2(Verbo):
    def __init__(self,conj2):
        Verbo.__init__(self,conj2)

    def genero(self):
        return self.palavra
    
    def numero(self):
        if(self.palavra[-1]=='e'):
            self.palavra =  self.palavra + 'm'
        else:
            self.palavra =  self.palavra[:-1]

class Verbo3(Verbo):
    def __init__(self,conj3):
        Verbo.__init__(self,conj3)

    def genero(self):
        return self.palavra
    
    def numero(self):
        if(self.palavra[-1]=='i'):
            self.palavra =  self.palavra + 'm'
        else:
            self.palavra =  self.palavra[:-1]


#exec
a = Arquivo("frase.txt")#endereco do arquivo
print "--------------------------------------------"
print "Frases originais:\n"
print a

print "Mudando o genero:\n"
a.genero()
print a

print "Mudando o numero:\n"
a.numero()
print a

# ERRO 1 9 5
