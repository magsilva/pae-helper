#######################################################
#   Lista 4
#   Alunos:
#       Rafael Henrique Manoel
#       Sergio Pavanello Rossi
#######################################################

class Frase:

    def __init__(self, sTexto=""):
        self.texto = sTexto
        self.tamanho = len(sTexto)
        self.Art1=""
        self.Subs1=""
        self.Verbo=""
        self.Art2=""
        self.Subs2=""
        self.ListaTexto = []

    def AnaliseSintatica(self):
        #cada frase eh da seguinte forma:
        #artigo, substantivo, verbo, artigo e substantivo
        inicio = 0
        fim = self.texto.find(' ')

        #primeiro artigo
        buffer = self.texto[inicio:fim]
        if buffer in ["os", "as", "o", "a"]:
            self.Art1 = ArtigoDefinido(buffer)
        else:
            self.Art1 = ArtigoIndefinido(buffer)
        self.ListaTexto.append(self.Art1)
            
        #primeiro substantivo
        inicio = fim+1
        fim = self.texto.find(' ',inicio)
        self.Subs1 = Substantivo(self.texto[inicio:fim])
        self.ListaTexto.append(self.Subs1)

        #verbo
        inicio = fim+1        
        fim = self.texto.find(' ',inicio)
        self.Verbo = Verbo(self.texto[inicio:fim])
        self.ListaTexto.append(self.Verbo)

        #segundo artigo
        inicio = fim+1
        fim = self.texto.find(' ',inicio)
        buffer = self.texto[inicio:fim]
        if buffer in ("os", "as", "o", "a"):
            self.Art2 = ArtigoDefinido(buffer)
        else:
            self.Art2 = ArtigoIndefinido(buffer)
        self.ListaTexto.append(self.Art2)

        #segundo substantivo
        inicio = fim+1
        self.Subs2 = Palavra(self.texto[inicio:self.tamanho])
        self.ListaTexto.append(self.Subs2)


    def alterar_genero(self):
        i = 0
        fim = len(self.ListaTexto)
        while i < fim:
            self.ListaTexto[i].alterar_genero()
            i+=1

    def alterar_numero(self):
        i = 0
        fim = len(self.ListaTexto)
        while i < fim:
            self.ListaTexto[i].alterar_numero()
            i+=1        
            

    def __str__(self):
        return "Artigo: " + str(self.Art1) + " | Substantivo: " + str(self.Subs1) + " | Verbo: " + str(self.Verbo) + " | Artigo: " + str(self.Art2) + " | Substantivo: " + str(self.Subs2) 
        
        

class Palavra:

    def __init__(self, sTexto = ""):
        self.texto = sTexto
        self.tamanho = len(sTexto)

    def set_palavra(self, sTexto):
        self.texto = sTexto

    def __str__(self):
        return str(self.texto)

    #----------------------------------#
    def alterar_genero(self):
        fem = 'a'
        masc = 'o'
        tamanho = len(self.texto) - 1
        if self.texto[tamanho] == 's':
            tamanho -= 1
            fem += 's'
            masc += 's'
            
        if self.texto[tamanho] == 'a':
            self.texto = self.texto[0:tamanho] + masc
        elif self.texto[tamanho] == 'o':
            self.texto = self.texto[0:tamanho] + fem

    def alterar_numero(self):
        self.texto += 's'
    #----------------------------------#

class ArtigoIndefinido(Palavra):
    #alterando o comportamento de algumas funcoes
    
    def alterar_numero(self):
        tamanho = len(self.texto) - 1
        if self.texto[tamanho] == "m":
            self.texto = self.texto[0:tamanho] + "ns"
        elif self.texto[tamanho] == 'a':
            self.texto += 's'

    def alterar_genero(self):
        tamanho = len(self.texto) - 1
        if self.texto[tamanho] == "s":
            if self.texto[tamanho-1] == "n":
                self.texto = self.texto[0:tamanho-2] + "mas"
            else:
                self.texto = self.texto[0:tamanho-2] + "ns"
        else:
            if self.texto[tamanho] == "m":
                self.texto += "a"
            elif self.texto[tamanho] == "a":
                print "aqui"
                self.texto = self.texto[0:tamanho]            

            


class ArtigoDefinido(Palavra):
    #Possui o mesmo comportamento da classe palavra
    def __init__(self, sTexto=''):
        Palavra.__init__(self, sTexto)
    
        

class Substantivo(Palavra):
    #Possui o mesmo comportamento da classe palavra
    def __init__(self, sTexto=''):
        Palavra.__init__(self, sTexto)

class Verbo(Palavra):
    def __init__(self, sTexto=''):
        Palavra.__init__(self, sTexto)

    #Verbo naum muda de genero
    def alterar_genero(self):
        self.texto = self.texto

    def alterar_numero(self):
        tamanho = self.tamanho-1
        if self.texto[tamanho] in ["a", "e", "i"]:
            #esta no singular
            self.texto += "m"
        else:
            self.texto = self.texto[0:tamanho-1]
    





    

    







f = Frase('um gato engole o rato')
f.AnaliseSintatica()
print f
f.alterar_genero()
print f
f.alterar_numero()
print f

# ERRO 1 2 100
# ERRO 1 12 100
