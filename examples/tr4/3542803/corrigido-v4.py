# Anderson S. Otuka #3542803
# Jefferson O. Kuramoto #3529760

# Observacoes de documentacao:

# Antes de cada procedimento, ha uma documentacao referente
# as variaveis de entrada de cada um deles. Os valores listados
# indicam as entradas possiveis, e o que eles fazem.

# Fornecemos um arquivo de entrada 'teste.txt' para
# se utilizar para os testes.
# O formato do arquivo de entrada sao frases,
# divididas por linhas. O programa processa todas as frases
# ate chegar ao final do arquivo.
# O uso do programa eh 'ProcessaArq(NomeArq)'.

Artigos = ['o', 'a', 'os', 'as', 'um', 'uma', 'uns', 'umas']


#------------

class Palavra:
    def __init__(self, string):
        self.conteudo = string

    def __str__(self):
        return self.conteudo

    def p_dir(self, numero):
# Retorna uma string com as 'numero' ultimas letras da Palavra.
        return self.conteudo[len(self.conteudo) - numero:len(self.conteudo)]

    def p_esq(self, numero):
# Retorna uma string com as 'numero' primeiras letras da Palavra.
# Se 'numero' for negativo, retorna uma string com a Palavra inteira
# menos as ultimas |'numero'| letras.
        if numero > 0:
            return self.conteudo[0:numero]
        elif numero < 0:
            return self.conteudo[0:len(self.conteudo) + numero]

    def string(self):
        return self.conteudo

    def genero(self, *gen):
        # gen                              #
        # 1 = converte para masculino      #
        # 2 = converte para feminino       #
        # outros valores = alterna genero  #
        if   (len(gen) > 0):
            gen = gen[0]
        if   (self.conteudo == 'um'   and (gen != 1)):
            self.conteudo = 'uma'
        elif (self.conteudo == 'uma'  and (gen != 2)):
            self.conteudo = 'um'
        elif (self.conteudo == 'uns'  and (gen != 1)):
            self.conteudo = 'umas'
        elif (self.conteudo == 'umas' and (gen != 2)):
            self.conteudo = 'uns'
        elif (self.p_dir(1) == 'o'   and (gen != 1)):
            self.conteudo = self.p_esq(-1) + 'a'
        elif (self.p_dir(1) == 'a'   and (gen != 2)):
            self.conteudo = self.p_esq(-1) + 'o'
        elif (self.p_dir(2) == 'os'  and (gen != 1)):
            self.conteudo = self.p_esq(-2) + 'as'
        elif (self.p_dir(2) == 'as'  and (gen != 2) and self.conteudo != 'umas'):
            self.conteudo = self.p_esq(-2) + 'os'
            
    def numero(self, *nro):
        # nro                                      #
        # 1 = singulariza palavra                  #
        # 2 = pluraliza palavra                    #
        # outros valores = alterna singular/plural #
        if (len(nro) > 0):
            nro = nro[0]
        if   (self.p_dir(1) == 'm'  and (nro != 1)):
            self.conteudo = self.p_esq(-1) + 'ns'
        elif (self.p_dir(2) == 'ns' and (nro != 2)):
            self.conteudo = self.p_esq(-2) + 'm'
        elif (self.p_dir(1) != 's'  and (nro != 1)):
            self.conteudo += 's'
        elif (self.p_dir(1) == 's'  and (nro != 2)):
            self.conteudo = self.p_esq(-1)


#------------

class Artigo(Palavra):
    def __init__(self, string):
        if string in Artigos:
            Palavra.__init__(self, string)
        else:
# Artigo invalido (nao eh o/a(s) nem um/a(s))
            print string + ' nao eh um artigo valido.'


#------------

class Substantivo(Palavra):
    def __init__(self, string):
        Palavra.__init__(self, string)


#------------

class Verbo(Palavra):
    def __init__(self, string):
        Palavra.__init__(self, string)               

    def numero(self, *nro):
        # nro                                      #
        # 1 = singulariza palavra                  #
        # 2 = pluraliza palavra                    #
        # outros valores = alterna singular/plural #
        if (len(nro) > 0):
            nro = nro[0]
        if   (self.p_dir(1) == 'm' and (nro != 2)):
            self.conteudo = self.p_esq(-1) + ''
        elif (self.p_dir(2) != 'm' and (nro != 1)):
            self.conteudo += 'm'

    def genero(self, *qualquer):
        pass


#------------

class Frase:
    def __init__(self, frase):
        self.ListaPalavras = frase.split()
        self.Palavra1 = Artigo(self.ListaPalavras[0])
        self.Palavra2 = Substantivo(self.ListaPalavras[1])
        self.Palavra3 = Verbo(self.ListaPalavras[2])
        self.Palavra4 = Artigo(self.ListaPalavras[3])
        self.Palavra5 = Substantivo(self.ListaPalavras[4])

    def __str__(self):
        return self.Palavra1.string() + ' ' + self.Palavra2.string() + ' ' + self.Palavra3.string() + ' ' + self.Palavra4.string() + ' ' + self.Palavra5.string()

    def string(self):
        return self.Palavra1.string() + ' ' + self.Palavra2.string() + ' ' + self.Palavra3.string() + ' ' + self.Palavra4.string() + ' ' + self.Palavra5.string()

    def genero(self):
# Altera todos os generos da frase
        self.Palavra1.genero();
        self.Palavra2.genero();
        self.Palavra4.genero();
        self.Palavra5.genero();

    def genero1(self):
# Altera os generos relacionados ao primeiro substantivo
        self.Palavra1.genero();
        self.Palavra2.genero();

    def genero2(self):
# Altera os generos relacionados ao segundo substantivo
        self.Palavra4.genero();
        self.Palavra5.genero();
        
    def numero(self):
# Altera o numero de todas as palavras da frase
        self.Palavra1.numero();
        self.Palavra2.numero();
        self.Palavra3.numero();
        self.Palavra4.numero();
        self.Palavra5.numero();

    def numero1(self):
# Altera os numeros relacionados ao primeiro substantivo        
        self.Palavra1.numero();
        self.Palavra2.numero();
        self.Palavra3.numero();

    def numero2(self):
# Altera os numeros relacionados ao segundo substantivo        
        self.Palavra4.numero();
        self.Palavra5.numero();


#------------

def ProcessaArq(NomeArq):
    fp = open(NomeArq, 'r')
 
    lin = fp.readline()
    while (lin != ""):
        f = Frase(lin)
        
        print
        print('Frase original ............... ' + f.string())
        f.genero()
        print('Frase com generos alterados .. ' + f.string())
        f.genero2()
        print('Frase com genero 1 alterado .. ' + f.string())
        f.genero1()
        f.genero2()
        print('Frase com genero 2 alterado .. ' + f.string())
        f.genero2()

        f.numero()
        print('Frase com numeros alterados .. ' + f.string())
        f.numero2()
        print('Frase com numero 1 alterado .. ' + f.string())
        f.numero1()
        f.numero2()
        print('Frase com numero 2 alterado .. ' + f.string())
        f.numero1()
        f.genero()
        print('Frase com tudo alterado ...... ' + f.string())
        
        lin = fp.readline()
        
    fp.close()

ProcessaArq( "teste.txt" )

# ERRO 1 11 50
# ERRO 1 12 100
# ERRO 1 14 25

# Programa não funciona
# ERRO 1 3 100
# ERRO 1 4 100
# ERRO 1 5 100
# ERRO 1 6 100
# ERRO 1 7 100
