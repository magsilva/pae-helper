Exercício 2.1 Conjunto inteiros


#conjunto com base em listas, lista1 = cj1, lista2 = cj2

class inteiro:
    def __init__(self,lista1,lista2):

        self.aux = []
	self.aux2 = []
	self.aux3 = []
        self.lista = []
        self.lista1= lista1
        self.lista2= lista2

        tipo = type(self.lista1[0])
        tipo2 = type(self.lista2[0])
        if (tipo <> type(0)) or (tipo2 <> type(0)) :
            print "Voce entrou com um numero nao inteiro"

# ERRO 1 5
# ERRO 1 7


    #lista vazia
    def vazia(self):
        self.vazia = []

    #adiciona elemento a lista1
    def adiciona(self,num):
        self.lista1.append(num)
        print self.lista1

# ERRO 1 2
    #uniao entre lista1 e lista2
    def uniao(self,lista2):
        self.lista = self.lista1 + lista2
        print self.lista

    #faz a interseccao da lista1 com a lista2
    def interseccao(self):
        a = len(self.lista1)
        b = len(self.lista2)
        i=0
        e=0


        for i in range(0,a):
            for e in range(0,b):
                if (self.lista1[i]== self.lista2[e]):
                    self.aux.append(self.lista1[i])
        #usa algoritmo n2 para saber qual elemento é igual
        print ("A interseccao é ",self.aux)

    # metodo de subtracao, faz lista1 - lista2
    def subtracao(self):
        h  = len(self.lista1)
        g = len(self.lista2)

        for i in range(0,h):
            for e in range(0,g):
                if (self.lista1[i]== self.lista2[e]):
                    self.aux2.append(self.lista1[i]) #mesmo que interseccao


        self.aux3 = self.lista1

        j = len(self.aux2)
        print j
        for i in range(0,h):
            for e in range(0,j):
                if (self.aux3[i]== self.aux2[e]):
                    t = self.aux2[e]
                    self.aux3.remove(t) #retira os elementos de aux2 de aux3(que e igual a lista1)

        print self.aux3


        print ("A subtracao eh: ",self.aux3)
    #imprime lista 2 e lista2
    def imprime(self):
        print self.lista1
        print self.lista2

# ERRO 1 16





Exercício 2.2 ? Tags

# Le o arquivo e salva as strings em A

f = open('C:\\WINDOWS\\Desktop\\teste.txt', 'r')
a = f.readlines()

########################################################################################

class  frases:
    numero = 0
    linhas = []
    # Numero e uma variavel inteira contendo o numero de frases
    # linhas e um array com as frases
    # Entrada e um array de string (vindo de F.READLINES)

    def __init__(self,entrada):
      self.numero =  len(entrada)
      self.linhas = a

    def imprime(self):
        print("Numero de frases")
        print(self.numero)
        print("As frases sao:\n")
        for i in range(0,self.numero):
            print(self.linhas[i])

########################################################################################            

class palavras:
    numero = []
    # Numero e o numero de palavras contidas numa frase
    # Classefrase e uma instanciacao da classe frase

    def __init__(self,classefrase):
        i = 0
        while i < classefrase.numero :
            self.numero.insert(i, a[i].count(" ") + 1) 
            i += 1

  

########################################################################################

class tags:
        corretas = 0    
        erradas = 0
        inicios = []
        tages = []
        # Corretas e o numero de tags corretas da linha
        # erradas e o numero de tags erradas
        # inicios contem as localizacoes dos inicios das tags
        # tages contem as tags
        # frase e uma string a ser analisada

        def __init__(self,frase):
              self.corretas = 0    
              self.erradas = 0
              self.inicios = []
              self.tages = []
              size = len(frase)
              i = -1
              while i < size-1:
                i += 1
                if frase[i] == '>':
                    self.erradas += 1
                if frase[i] ==  '<':
                    self.inicios.append(i)
                    while i < size-1:
                      i +=1
                      if frase[i] == '>':               
                         self.corretas += 1
                         break
                      if frase[i] == '<':               
                         self.erradas += 1
                         self.inicios.pop()
                         i -= 1
                         break
              i = 0
              while i < self.corretas:
               temp = ""
               char = ""
               count = self.inicios[i]
               while char != '>':
                  char = frase[count]
                  temp += char
                  count += 1
               self.tages.append(temp)
               i += 1

    # Retorna as tags formatadas em string
        def retornatags(self):
            i = 0
            temp = ""
            for i in range(0,self.corretas):
                temp += self.tages[i]
            return temp


########################################################################################



b = frases(a)
c = palavras(b)


# arquivo de saida
r = open('C:\\WINDOWS\\Desktop\\saida.txt', 'w')

j = 0
# Istancia uma tag para cada linha
while j < b.numero:
 d = tags(a[j])
 r.write("linha ")
 r.write(str(j + 1))
 r.write(" - ")
 r.write(str(c.numero[j]))
 r.write(" palavras - ")
 r.write(str(d.corretas))
 r.write(" tags (")
 r.write((d.retornatags()))
 r.write(") - ")
 r.write(str(d.erradas))
 r.write(" tags-problema\n")
 j += 1

Arq. de entrada
Teste do uso de <tags> em POO
e processamento de <problemas com <mau> uso <de>tags?

Saída
linha 1 - 7 palavras - 1 tags (<tags>) - 0 tags-problema
linha 2 - 8 palavras - 2 tags (<mau><de>) - 1 tags-problema

# ERRO 2 23
