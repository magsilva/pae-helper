# SCE-213 Programacao Orientada a Objeto
# Profa. Renata M. Fortes
# 
# Exercicio sobre Heranca
# 
# Alunos: Joao Paulo Scardua Coelho  nUSP 3560630   jpcoelho@grad.icmc.usp.br
# 	Marco Aurelio Roncati	   nUSP 3455855   marcor@grad.icmc.usp.br
# 
# -----------------------------------------------------------------------------------------
# item 1) Arquivo com as frases utilizado como entrada:
# 
# O rato esconde uma rata
# Os gatos comem uns ratos
# Uma menina lava um pato
# O menino leva a menina
# As meninas amam os meninos
# A professora proibe o aluno
# Uns patos bicam o pescador
# As garotas beijam o cantor

# -----------------------------------------------------------------------------------------
# item 2) Codigo fonte da definicao das classes:

class Palavra:
  
    def __init__(self, pal):
        self.palavra = pal  
   
class Artigo(Palavra):
    def __init__(self, pal):
        Palavra.__init__(self,pal)

    #lista_in eh a lista de artigos definidos ou indefinidos
    #lista_out eh a lista de artigos com o numero ou o genero alterados que sera retornada 
    def altera(self, lista_in, lista_out):
        return lista_out[lista_in.index(self.palavra)]
 
class Artigo_Definido(Artigo):

    def __init__(self, pal):
        Artigo.__init__(self,pal)
        self.lista_in = ["o","a","os","as","O","A","Os","As"]
        self.lista_out_num = ["os","as","o","a","Os","As","O","A"]
        self.lista_out_gen = ["a","o","as","os","A","O","As","Os"]

    def altera_numero(self):
        return self.altera(self.lista_in, self.lista_out_num)

    def altera_genero(self):
        return self.altera(self.lista_in, self.lista_out_gen)

class Artigo_Indefinido(Artigo):
    def __init__(self, pal):
	Artigo.__init__(self,pal)
        self.lista_in = ["um","uma","uns","umas","Um","Uma","Uns","Umas"]
        self.lista_out_num = ["uns","umas","um","uma","Uns","Umas","Um","Uma"]
        self.lista_out_gen = ["uma","um","umas","uns","Uma","Um","Umas","Uns"]

    def altera_numero(self):
        return self.altera(self.lista_in, self.lista_out_num)

    def altera_genero(self):
        return self.altera(self.lista_in, self.lista_out_gen) 

class Substantivo(Palavra):
    def __init__(self, pal):
        Palavra.__init__(self,pal)

    def altera_numero(self):
        if self.palavra[-1] == "s":
            return self.palavra[0:-1]
	    #somente retira o 's' da palavra
	elif self.palavra[-2:] == "or":
	#por exemplo: cantor, professor, nadador
	    return self.palavra + "es"
        else:#palavra termina em 'a' ou 'o'
            return self.palavra + "s"

    def altera_genero(self):
        if self.palavra[-1] == "s":
            if self.palavra[-2] == "o":
		#palavra terminada em 'os'
                return self.palavra[0:-2] + "as"
		#tira-se o 'os'e acrescenta 'as'
            else:#self.palavra[-2] == "a"
		#palavra terminada em 'as'
                return self.palavra[0:-2] + "os"
        
        elif self.palavra[-1] == "o":
            return self.palavra[0:-1] + "a"
        elif self.palavra[-1] == "r":
	#por exemplo: cantor, pintor
             return self.palavra + "a"
        elif self.palavra[-2:] == "ra":
	#por exemplo: cantora, pintora
            return self.palavra[0:-1]
        elif self.palavra[-1] == "a":
            return self.palavra[0:-1] + "o"

	
class Verbo(Palavra):
    def __init__(self, pal):
        Palavra.__init__(self,pal)

class Prim_Conjugacao(Verbo): 
    def __init__(self, pal):
        Verbo.__init__(self,pal)

    #como pela estrutura das frases do arquivo de entrada
    #os verbos estarao somente na segunda pessoa do singular
    #ou segunda do plural basta fazer os testes que foram feitos abaixo
    def altera(self):
        if self.palavra[-1] == "a":
            return self.palavra + "m" 
        else:#palavra termina em 'am'
            return self.palavra[0:-1]

#como os verbos estao conjugados no presente do indicativo
#a forma da segunda conjugacao e da terceira se tornam
#semelhantes, sendo necessario apenas uma classe para representa-las    
class Seg_Ter_Conjugacao(Verbo):
    def __init__(self, pal):
        Verbo.__init__(self,pal)

    def altera(self):
        if self.palavra[-1] == "e":
            return self.palavra + "m" 
        else:#palavra termina em "em"
            return self.palavra[0:-1]

# -----------------------------------------------------------------------------------------
# item 3) Codigo fonte do programa que utiliza as classes declaradas
#	no item 2 e manipula o arquivo de entrada:

class Frases:
    def __init__(self,arquivo):
        file = open(arquivo,'r')
        self.frases = file.readlines()
        #self.frases recebe todas as frases do arquivo
        file.close()
 
    def resolve(self):
        for i in self.frases:
            #i recebe cada frase inteira	            
	    lista_numero = ['','','','','']
            lista_genero = ['','','','','']
            #listas utilizadas para armazenar os valores das alteracoes
	    #feitas nas palavras
	    i = i[:-1]#eliminar o '\n'do final de cada frase
            lista = i.split(" ")
            #Artigo(primeira palavra)
	    #se palavra eh artigo indefinido
            if lista[0][0] == 'u' or lista[0][0] == 'U':
                art_ind = Artigo_Indefinido(lista[0])
                lista_numero[0] = art_ind.altera_numero()
                lista_genero[0] = art_ind.altera_genero()
            else:# palavra eh artigo definido
                art_def = Artigo_Definido(lista[0])
                lista_numero[0] = art_def.altera_numero()
                lista_genero[0] = art_def.altera_genero()

            #substantivo (segunda palavra)
            subs = Substantivo(lista[1])
            lista_numero[1] = subs.altera_numero()
            lista_genero[1] = subs.altera_genero()
            
            #verbo (terceira palavra)
            #se o verbo eh de Primeira Conjugacao
            if lista[2][-2:] == 'am' or lista[2][-1] == 'a':
                verbo_1conj = Prim_Conjugacao(lista[2])
                lista_numero[2] = verbo_1conj.altera()
                lista_genero[2] = lista[2]

            #se o verbo eh de Segunda ou Terceira Conjugacao
            if lista[2][-2:] == 'em' or lista[2][-1] == 'e':         
                verbo_2_3_conj = Seg_Ter_Conjugacao(lista[2])
                lista_numero[2] = verbo_2_3_conj.altera()
                lista_genero[2] = lista[2]

            #artigo (quarta palavra)
            if lista[3][0] == 'u':#palavra eh artigo indefinido
                art_ind = Artigo_Indefinido(lista[3])
                lista_numero[3] = art_ind.altera_numero()
                lista_genero[3] = art_ind.altera_genero()
            else:# palavra eh artigo definido
                art_def = Artigo_Definido(lista[3])
                lista_numero[3] = art_def.altera_numero()
                lista_genero[3] = art_def.altera_genero()

            #substantivo (quinta palavra)
            subs = Substantivo(lista[4])
            lista_numero[4] = subs.altera_numero()
            lista_genero[4] = subs.altera_genero()

	    #impresao dos resultados
            print lista
            print lista_numero
            print lista_genero
            print

a = Frases( "teste.txt" )
a.resolve()

# ERRO 1 11 50
# ERRO 1 15 50
