#Marcelo Kenji Hotta 3460142


#2.1
class conj:
    #inicializa
    def __init__ (self, *elem):
        self.lista=[]
        for num in elem:
            self.add(num)

    #adiciona elemento na lista
    def add (self, num):
        if type(num) == int:
            if num in self.lista:
                print "Elemento jah incluido: %i" %num
            else: 
                self.lista.append(num)
                print "Elemento %i incluido" %num
        elif num.__class__ == conj:
            for x in num.lista:
                self.add(x)
        else:
            print "Elemento invalido: %s" %num


    #remove elemento da lista
    def rem (self, num):
        if num in self.lista:
            self.lista.remove(num)
            print "Elemento %s removido" %num
        else:
            print "Elemento %s nao encontrado" %num

    #conj+conj=uniao
    def __add__(self, elem):
        import copy
        uniao=copy.deepcopy(self.lista)
        for num in elem.lista:
            if num not in uniao:
                uniao.append(num)
        return uniao
            
    #conj/conj=interseccao
    def __div__(self, elem):
        inter=[]
        for num in self.lista:
            if num in elem.lista:
                inter.append(num)
        return inter

    #conj-conj=subtracao
    def __sub__(self, elem):
        import copy
        sub=copy.deepcopy(self.lista)
        for num in elem.lista:
            if num in sub:
                sub.remove(num)
        return sub
            
    #imprime os elementos da lista
    def imprime (self):
        print self.lista
        



#----------------------------------------------------
#Marcelo Kenji Hotta 3460142

# ERRO 2 23

#2.2
class frases: #pega as frases do arquivo (lista de frases)
    def __init__(self, FName):
        try:
            f = open(FName, "r")
            self.cont = f.readlines()
            f.close()
        except:
            print "Arquivo", FName, "nao encontrado"

    def qtde(self):
        return len(self.cont)

class palavras: #pega palavras da frase (lista de palavras)
    def __init__(self, Frase):
        self.cont = []
        ini = 0
        fim = 0
        for n in range(0, len(Frase)-1):
            if Frase[n] == " " or Frase[n] == "\n":
                if ini != fim:
                    self.cont.append(Frase[ini:fim])
                ini = n
                fim = n
            else:
                if ini == fim:
                    ini = n
                fim = n+1
        if ini != fim:
            self.cont.append(Frase[ini:fim])

    def qtde(self):
        return len(self.cont)
                
class tags: #pega tags de palavra (lista de tags)
    def __init__(self, Palavra):
        self.cont0 = []
        self.cont1 = []
        for n in range(0, len(Palavra) -1):
            if Palavra[n][0] == "<":
                if Palavra[n][-1] == ">":
                    self.cont1.append(Palavra[n])
                else:
                    self.cont0.append(Palavra[n])
            elif Palavra[n][-1] == ">":
                self.cont0.append(Palavra[n])

    def qtde0(self):
        return len(self.cont0)

    def qtde1(self):
        return len(self.cont1)

class output: #escreve no arquivo de saida
    def __init__(self, NomeArq):
        f = open(NomeArq, 'w')
        for n in range(0, frase.qtde()):
            nlinha = n+1
            npalavra = palavra[n].qtde()
            ntag1 = tag[n].qtde1()
            cont1 = tag[n].cont1
            ntag0 = tag[n].qtde0()
            cont0 = tag[n].cont0
            f.write("linha %i - " %nlinha)
            f.write("%i palavras - "  %npalavra)
            f.write("%i tags "  %ntag1)
            f.write("%s - "  %tag[n].cont1)
            f.write("%i tags-defeito "  %ntag0)
            f.write("%s\n"  %tag[n].cont0)
        f.close()

#---------------------------------------
#k = 'c:\download\poo\in.txt'
#y = 'c:\download\poo\out.txt'
#arqin = k
#arqout = y
#testes

        
print "Nome do Arquivo de entrada (sem aspas): "
arqin = str(raw_input())

frase = frases(arqin)
palavra = []
tag = []
for n in range(0, frase.qtde()):
    palavra.append(palavras(frase.cont[n]))
    tag.append(tags(palavra[n].cont))


print frase.qtde(), "Frases: %s\n" %frase.cont

for n in range(0, frase.qtde()):
    print palavra[n].qtde(), "Palavras da frase %i" %n, palavra[n].cont, "\n"
    
for n in range(0, frase.qtde()):
    print tag[n].qtde0(), "Tags defeituosas da frase %i:" %n, tag[n].cont0, "\n"
    print tag[n].qtde1(), "Tags corretas da frase %i:" %n, tag[n].cont1, "\n"

print "Nome do Arquivo de saida (sem aspas): "
arqout = str(raw_input())

output(arqout)
