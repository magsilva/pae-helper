class frase:

    def __init__ (self, *palavras):
        self.artigo1 = palavras[0]
        self.substantivo1 = palavras[1]
        self.verbo = palavras[2]
        self.artigo2 = palavras[3]
        self.substantivo2 = palavras[4]

    def alteraNumero(self):
        self.artigo1.alteraNumero()
        self.substantivo1.alteraNumero()
        self.verbo.alteraNumero()
        self.artigo2.alteraNumero()
        self.substantivo2.alteraNumero()

    def alteraGenero(self):
        self.artigo1.alteraGenero()
        self.substantivo1.alteraGenero()
        self.verbo.alteraGenero()
        self.artigo2.alteraGenero()
        self.substantivo2.alteraGenero()

    def imprimeFrase(self):
        print self.artigo1.conteudo + ' ' + self.substantivo1.conteudo + ' ' +\
              self.verbo.conteudo + ' ' + self.artigo2.conteudo + ' ' +\
              self.substantivo2.conteudo + '.'

class palavra:
    def __init__ (self, valor):
        self.conteudo = valor

    def imprime(self):
        print(self.conteudo)

    def alteraNumero(self):
        return

    def alteraGenero(self):
        return

class artigo(palavra):

    def alteraNumero(self):
        pass
    def alteraGenero(self):
        pass

class substantivo(palavra):

    def alteraNumero(self):
        if self.conteudo.endswith('s'):
            temp = ""
            for i in range(0,len(self.conteudo)-1):
                temp = temp+self.conteudo[i]
            self.conteudo = temp
        else:
            self.conteudo = self.conteudo + 's'

    def alteraGenero(self):
        if self.conteudo.endswith('s'):
            if self.conteudo[len(self.conteudo)-2] == 'o':
                temp = ""
                for i in range(0,len(self.conteudo)-2):
                    temp = temp+self.conteudo[i]
                self.conteudo = temp + 'as'
            else:
                temp = ""
                for i in range(0,len(self.conteudo)-2):
                    temp = temp+self.conteudo[i]
                self.conteudo = temp + 'os'
        else:
            if self.conteudo.endswith('o'):
                temp = ""
                for i in range(0,len(self.conteudo)-1):
                    temp = temp+self.conteudo[i]
                self.conteudo = temp + 'a'
            else:
                temp = ""
                for i in range(0,len(self.conteudo)-1):
                    temp = temp+self.conteudo[i]
                self.conteudo = temp + 'o'

class verbo(palavra):

    def alteraNumero(self):
        if self.conteudo.endswith('m'):
            temp = ""
            for i in range(0,len(self.conteudo)-1):
                temp = temp+self.conteudo[i]
            self.conteudo = temp
        else:
            self.conteudo = self.conteudo + 'm'

    def alteraGenero(self):
        return

class artigoDefinido(artigo):

    def alteraNumero(self):
        sing = ['o', 'a', 'O', 'A']
        plural = ['os', 'as', 'Os', 'As']
        if self.conteudo in sing:
            self.conteudo = plural[sing.index(self.conteudo)]
        else:
            self.conteudo = sing[plural.index(self.conteudo)]

    def alteraGenero(self):
        masc = ['o', 'os', 'O', 'Os']
        fem = ['a', 'as', 'A', 'As']
        if self.conteudo in masc:
            self.conteudo = fem[masc.index(self.conteudo)]
        else:
            self.conteudo = masc[fem.index(self.conteudo)]

class artigoIndefinido(artigo):

    def alteraNumero(self):
        sing = ['um', 'uma', 'Um', 'Uma']
        plural = ['uns', 'umas', 'Uns', 'Umas']
        if self.conteudo in sing:
            self.conteudo = plural[sing.index(self.conteudo)]
        else:
            self.conteudo = sing[plural.index(self.conteudo)]

    def alteraGenero(self):
        masc = ['um', 'uns', 'Um', 'Uns']
        fem = ['uma', 'umas', 'Uma', 'Umas']
        if self.conteudo in masc:
            self.conteudo = fem[masc.index(self.conteudo)]
        else:
            self.conteudo = masc[fem.index(self.conteudo)]

class primeiraConjugacao(verbo):
    pass

class segundaConjugacao(verbo):
    pass

class terceiraConjugacao(verbo):
    pass

nomearquivo = raw_input('Digite nome do arquivo com frases: ')
arquivo = file(nomearquivo, 'r')

conteudoarquivo = arquivo.read()
lconteudoarquivo = conteudoarquivo.splitlines()

frases = []

for linha in lconteudoarquivo:
    lpalavra = linha.split(' ')
    if lpalavra[0] in ['o', 'a', 'O', 'A']:
        palavra1 = artigoDefinido(lpalavra[0])
    else:
        palavra1 = artigoIndefinido(lpalavra[0])
    palavra2 = substantivo(lpalavra[1])
    palavra3 = verbo(lpalavra[2])
    if lpalavra[3] in ['o', 'a', 'O', 'A']:
        palavra4 = artigoDefinido(lpalavra[3])
    else:
        palavra4 = artigoIndefinido(lpalavra[3])
    if lpalavra[4].endswith('.'):
        temp = ""
        for i in range(0,len(lpalavra[4])-1):
            temp = temp+lpalavra[4][i]
        lpalavra[4] = temp
        del temp
    palavra5 = substantivo(lpalavra[4])
    frases.append(frase(palavra1, palavra2, palavra3, palavra4, palavra5))

print 'Frases originais:'
print
for cadafrase in frases:
    cadafrase.imprimeFrase()

opcao = '4'

while opcao != '3':
   
    print
    print '1 - Mudar genero'
    print '2 - Mudar numero'
    print '3 - Sair'
    print
    opcao = raw_input('Escolha opcao: ')
    if opcao == '1':
        for cadafrase in frases:
            cadafrase.alteraGenero()
            cadafrase.imprimeFrase()

    if opcao == '2':
        for cadafrase in frases:
            cadafrase.alteraNumero()
            cadafrase.imprimeFrase()


# ERRO 1 11 50
# ERRO 1 12 100
# ERRO 1 14 15
# ERRO 1 15 50
