################# Frase #################
class Frase:
    def __init__(self, path):
        arq = open(path,'r')
        linha = arq.readline()

        while linha:

            ### Separa cada palavra da frase
            palavras = linha.split(' ')
            artdef = Artigo_Definido(palavras[0])
            sub1 = Substantivo(palavras[1])
            verbo = Verbo(palavras[2])
            artindef = Artigo_Indefinido(palavras[3])
            sub_aux = palavras[4].rstrip('\n')
            sub2 = Substantivo(sub_aux)

            ### Altera numero e genero
            
            print 'Frase original: '
            print linha.capitalize()
            print '\n'
            self.altera_genero(artdef, sub1, verbo, artindef, sub2)
            self.altera_numero(artdef, sub1, verbo, artindef, sub2)

            ## Le nova linha
            linha = arq.readline()

    def altera_numero(self, artdef, sub1, verbo, artindef, sub2):

        ### Altera cada elemento em sua respectiva classe

        new_artdef = artdef.altera_numero().capitalize()
        new_sub1 = sub1.altera_numero()
        new_verbo = verbo.altera_numero()
        new_artindef = artindef.altera_numero()
        new_sub2 = sub2.altera_numero()

        new_frase = str(new_artdef) + ' ' + str(new_sub1) + ' ' + str(new_verbo) + ' ' + str(new_artindef) + ' ' + str(new_sub2) + '.'

        print 'Frase com o numero alterado: '
        print new_frase
        print '\n'
          
    def altera_genero(self, artdef, sub1, verbo, artindef, sub2):

        ### Altera cada elemento em sua respectiva classe

        new_artdef = artdef.altera_genero().capitalize()
        new_sub1 = sub1.altera_genero()
        new_verbo = verbo.word
        new_artindef = artindef.altera_genero()
        new_sub2 = sub2.altera_genero()

        new_frase = str(new_artdef) + ' ' + str(new_sub1) + ' ' + str(new_verbo) + ' ' + str(new_artindef) + ' ' + str(new_sub2) + '.'

        print 'Frase com o genero alterado: '
        print new_frase
        print '\n'

################# Palavra #################

class Palavra(Frase):        
    def __init__(self, word):
        self.word = word

    def altera_genero(self):
        new_word = self.__altera_genero__()
        return new_word

    def altera_numero(self):
        new_word = self.__altera_numero__()
        return new_word

################# Substantivo #################
class Substantivo(Palavra):
    def __init__(self, word):
        Palavra.__init__(self, word)
        self.numero = self.get_numero()
        self.genero = self.get_genero()

    def get_numero(self):
        tamanho = len(self.word)
        ultima_letra = self.word[tamanho - 1].capitalize()
        if ultima_letra == 'S':
            numero = 'plural'
        else:
            numero = 'singular'

        return numero

    def get_genero(self):
        tamanho = len(self.word)
        if self.numero == 'singular':
            ultima_letra = self.word[tamanho - 1].capitalize()
        else:
            ultima_letra = self.word[tamanho - 2].capitalize()
        if ultima_letra == 'O':
            genero = 'masculino'
        else:
            genero = 'feminino'

        return genero

    def __altera_numero__(self):
        if self.numero == 'singular':
            new_word = self.word + 's'
        else:
            new_word = self.word.rstrip('s')

        return new_word

    def __altera_genero__(self):
        new_word = self.word
        if self.genero == 'masculino':
            if self.numero == 'singular':
                new_word2 = self.word.rstrip('o')
                new_word = new_word2 + 'a'
            else:
                new_word2 = self.word.rstrip('os')
                new_word = new_word2 + 'as'
        else:
            if self.numero == 'singular':
                new_word2 = self.word.rstrip('a')
                new_word = new_word2 + 'o'
            else:
                new_word2 = self.word.rstrip('as')
                new_word = new_word2 + 'os'

        return new_word
            
################# Artigo Definido #################

class Artigo_Definido(Substantivo):
    def __init__(self, word):
        Substantivo.__init__(self, word)

################# Artigo Indefinido #################

class Artigo_Indefinido(Palavra):
    def __init__(self, word):
        Palavra.__init__(self, word)
        self.numero = self.get_numero()
        self.genero = self.get_genero()

    def get_numero(self):
        tamanho = len(self.word)
        ultima_letra = self.word[tamanho - 1].capitalize()
        if ultima_letra ==  'S':
            numero = 'plural'
        else:
            numero = 'singular'

        return numero

    def get_genero(self):
        tamanho = len(self.word)
        if self.numero == 'singular':
            ultima_letra = self.word[tamanho - 1].capitalize()
        else:
            ultima_letra = self.word[tamanho - 2].capitalize()
        if ultima_letra == 'A':
            genero = 'feminino'
        else:
            genero = 'masculino'

        return genero

    def __altera_numero__(self):
        if self.numero == 'singular':
            if self.genero == 'feminino':
                new_word = self.word + 's'
            else:
                new_word2 = self.word.rstrip('m')
                new_word = new_word2 + 'ns'
        else:
            if self.genero == 'feminino':
                new_word = self.word.rstrip('s')
            else:
                new_word2 = self.word.rstrip('ns')
                new_word = new_word2 + 'm'

        return new_word

    def __altera_genero__(self):
        if self.genero == 'feminino':
            if self.numero == 'singular':
                new_word = self.word.rstrip('a')
            else:
                new_word2 = self.word.rstrip('mas')
                new_word = new_word2 + 'ns'
        else:
            if self.numero == 'singular':
                new_word = self.word + 'a'
            else:
                new_word2 = self.word.rstrip('ns')
                new_word = new_word2 + 'mas'

        return new_word

################# Verbo #################
class Verbo(Palavra):
    def __init__(self, word):
        Palavra.__init__(self, word)
        self.numero = self.get_numero()

    def get_numero(self):
        tamanho = len(self.word)
        ultima_letra = self.word[tamanho - 1].capitalize()
        if ultima_letra == 'M':
            numero = 'plural'
        else:
            numero = 'singular'

        return numero

    def __altera_numero__(self):
        if self.numero == 'singular':
            new_word = self.word + 'm'
        else:
            new_word = self.word.rstrip('m')

        return new_word

################# Programa Principal #################

a = Frase('Frases.txt')

# ERRO 1 9 5
# ERRO 1 11 50
# ERRO 1 12 100
# ERRO 1 14 25
# ERRO 1 15 50
