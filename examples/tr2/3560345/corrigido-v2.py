#Exercicio 2.1

#Nomes:
# Cleber Castro Hage ........... No USP: 3560345
# Glauco Becaro ................ No USP: ???????

#Este programa executa todos os passos do exercicio.

#Classe Conjunto de Inteiros
class Conjunto_Inteiros:
    def __init__(self, *Param):  #Pode-se colocar vários parametros , Numeros Inteiros e Objetos do Tipo Classe Conjunto_
		         #Inteiros
        self.List = []   #Guardarei tudo nesta Lista
        for i in Param:    # Verificando se os parametros sao numeros inteiros ou objetos do tipo classe Conjunto_Inteiros
            if type(i) == type(0):
                self.Adicao(i)   # Adicionar o elemento a List
            if type(i) == type(self):
                self.Uniao(i)  # Adicionar o objeto a List
     
#Adicao de elementos numeros inteiros
    def Adicao(self, Read):
        if Read not in self.List:  #Verificando se jah nao existe armazenado
            self.List.append(Read)
            
# Uniao de Listas
    def Uniao(self, Read):
        if Read not in self.List:   # Verificando se jah nao existe
            self.List += Read.List

#Remocao de elementos numeros inteiros ou de objetos do tipo inteiro
    def RemocaoInt(self, Read):
        if Read in self.List:
            self.List.remove(Read)

#Subtracao: List - Subconjunto da List
    def Subtracao(self, Read):
        Lista_Subtracao = self.List
        for i in self.List:
            for j in Read.List:
                if i == j:
                    Lista_Subtracao.remove(j)  
        print(Lista_Subtracao)

#Interseccao de List com uma lista passada como parametro
    def Interseccao(self, Read):
        Lista_Interseccao = []
        for i in self.List:
            for j in Read.List:
                if i == j:
                    Lista_Interseccao.append(j)
        print(Lista_Interseccao)

#Impressao de elementos numeros inteiros ou de objetos do tipo inteiro da List
    def Imprima_Conjunto(self):
        print(self.List)
    
#Nomes:
# Cleber Castro Hage ........... No USP: 3560345
# Glauco Becaro ................ No USP: ???????

#Exercicio 2.2

#Este Programa foi escrito baseado no texto do exercicio. Ele foi feito seguindo exatamente o que
#foi pedido.
#Mas a observacao que estava no final nao foi percebida.
#Portanto, nao ha classes para cada classificacao(Palavra, Frase, Tag) e, sim, tudo implementado
#como se fossem atributos.

#OBSERVACAO: para se terminar uma frase deve-se terminar com '.'. E para se terminar palavras deve-
#se usar ' '

# ERRO 2 23
# ERRO 2 25

import string

class a:
    #Inicializacao. Deve-se passar um Nome de Arquivo como parametro para a instancia da classe
    def __init__(self, File_Name):
        f = open(File_Name, 'r')
	self.Read = str(f.readlines())
	f.close
        i = 0
        j = 0
        self.Word = [] #Palavra
        self.Phrase = [] #Frase
        lim = self.Read.find(' ', i) #lim é a primeira posicao onde se encontra ' '
        while lim != -1:  #quando ainda existe ' '     
            self.Word += ([self.Read[i: lim]]) #une a palavra a uma lista de palavras
            i = lim + 1
            lim = self.Read.find(' ', i) #procurar por outro ' '
            
        i=0 # reinicializar para poder comecar a procurar por "frases"
        lim2 = self.Read.find('.', i)
        while lim2 != -1: #segue do mesmo modo que se fez para palavras
            
            self.Phrase += ([self.Read[i: lim2]])
            i = lim2 + 1
            lim2 = self.Read.find('.', i)
        
        i=0 # reinicializar para poder comecar a procurar por "Tags"
        j=0
        self.Tag = []
        self.NTagsCProb = 0
        lim3 = self.Read.find('<', i)
        lim4 = self.Read.find('>', j)
        lim3a = self.Read.find('<', (lim3+1)) #lim3a para saber se existe algum '<' a mais que
        #o '<' anterior antes de '>'
        lim4a = self.Read.find('<', (lim4+1)) #lim4a para saber se existe algum '>' a mais que
        #o '>' anterior antes de '<'
        while ((lim3) != -1): 
            if (lim3 < lim4) and (lim4 != -1): #Tudo certo para armazenar Tag
                self.Tag += ([self.Read[(lim3+1): lim4]])
                i = lim3 + 1
                j = lim4 + 1
                lim3 = self.Read.find('<', i)
                lim4 = self.Read.find('>', j)
            if (lim3a > lim4) and (lim4 == -1): # Problema: tem '<' a mais antes de '>'
                self.NTagsCProb += 1
                i = lim3 + 1
                lim3 = self.Read.find('<', i)
            if (lim4a < lim3a) and (lim3 != -1): # Problema: tem '>' a mais antes de '<'
                self.NTagsCProb += 1
                j = lim4 + 1
                lim4 = self.Read.find('>', j)
        N=1   # Para numeracao de frases
        k=0   # Para ir de 0 ateh numero de frases
        LWord = len(self.Word)   # Para salvar o numero de palavras
        LPhrase = len(self.Phrase)   # Para salvar o numero de frases
        LTag = len(self.Tag)# Para salvar o numero de tags
        print('Escolha um nome para o arquivo de saida desejado')
        self.File_Name_Out = raw_input()
        Out = open(self.File_Name_Out, 'w')
        while k < LPhrase:
            print >>Out, "frase %d - %d palavras - %d tags (%s) - %d tags-problema)" %(N, LWord, LTag, self.Tag, self.NTagsCProb)
            N += 1
            k += 1
        Out.close()
        
