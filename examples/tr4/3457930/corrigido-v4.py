#Alunos : Alesandro G. Krempi
#         Jonatas Kerr


class Frase:
    def __init__(self):
        self.ListaF = []    #armazena frases.
        self.ListaF2=[[],[],[],[]]# 4 frases
        
    def openfile(self):
        f = open("texto.txt", "r")
        self.ListaF = f.readlines()#lista de linhas
        f.close()
        lista = []
        for i in range(len(self.ListaF)):
            linha = self.ListaF[i]+'\n'
            for j in range(len (linha)):
                if (linha[j] in [' ','\n']):
                    self.ListaF2[i].append(''.join(lista))
                    lista = []
                else: lista.append(linha[j])

class Palavra(Frase):
    def __init__(self):
        self.Masc = ['o','os','um','uns']
        self.Fem = ['a','as','uma','umas']
        self.Art = ['a','o']
        self.Ind = [0,1,2,3,4]
        self.sing = ['o','a','um','uma']
        self.pluri= ['os','as','uns','umas']
        self._3ps = ['a','e']
        Frase.__init__(self)
                
    def gen(self):
        import copy
        for i in range(len(self.ListaF)):
            l= copy.deepcopy(self.ListaF2[i])
            l[0]=l[0].lower()
            for x in [0,3]:
                if l[x] in self.Masc:
                    l[x]= self.Fem[self.Masc.index(l[x])]
                    a = list(l[x+1])
                    c = len(a)-1
                    if a[c] in self.Art:
                        a[c]= self.Art[self.Art.index(a[c])-1]
                        l[x+1]=''.join(a)
                    else:
                        a[c-1]=self.Art[self.Art.index(a[c-1])-1]
                        l[x+1]=''.join(a)
                elif l[x] in self.Fem:
                    l[x]= self.Masc[self.Fem.index(l[x])]
                    a = list(l[x+1])
                    c = len(a)-1
                    if a[c] in self.Art:
                        a[c]= self.Art[self.Art.index(a[c])-1]
                        l[x+1]=''.join(a)
                    else:
                        a[c-1]=self.Art[self.Art.index(a[c-1])-1]
                        l[x+1]=''.join(a)
            strg = self.ListaF2[i] 
            for i in self.Ind :
                strg[i]=l[i]
            strg =' '.join(strg)
            print strg.capitalize()

    def num(self):
        import copy
        for i in range(len(self.ListaF)):
            l= copy.deepcopy(self.ListaF2[i])
            l[0]=l[0].lower()
            for x in [0,3]:
                if l[x] in self.sing:
                    l[x]= self.pluri[self.sing.index(l[x])]
                    if x == 0:
                        a = list(l[x+2])
                        if a[len(a)-1] in self._3ps:
                            a.append('m')
                            l[x+2]= ''.join(a)
                    a = list(l[x+1])
                    a.append('s')
                    l[x+1]= ''.join(a)
                elif l[x] in self.pluri:
                    l[x]= self.sing[self.pluri.index(l[x])]
                    if x == 0 :
                        a = list(l[x+2])
                        if a[len(a)-2] in self._3ps:
                            a.pop()
                            l[x+2]= ''.join(a)
                    a = list(l[x+1])
                    a.pop()
                    l[x+1]= ''.join(a)
            strg = self.ListaF2[i]
            for i in self.Ind :
                strg[i]=l[i]
            strg =' '.join(strg)
            print strg.capitalize()

    def pessoa(self):
        import copy
        for i in range(len(self.ListaF)):
            l= copy.deepcopy(self.ListaF2[i])
            c = list(l[2])
            if c[len(c)-1] in self._3ps:
                c.append('m')
            elif c[len(c)-2] in self._3ps:
                c.pop()
            l[2]=''.join(c)
            strg =' '.join(l)
            print strg.capitalize()

class artigo(Palavra):  #modifica apenas art. def./indef. de uma frase
    def __init__(self):
        Palavra.__init__(self)
        self.Ind = [0,3]

class art_def(artigo):#modifica somente arts. definidos de uma frase
    def __init__(self):
        artigo.__init__(self)
        self.Masc = ['o','os']
        self.Fem = ['a','as']
        self.sing = ['o','a']
        self.pluri= ['os','as']

class art_indef(artigo):#modifica somente arts. indefinidos de uma frase
    def __init__(self):
        artigo.__init__(self)
        self.Masc = ['um','uns']
        self.Fem = ['uma','umas']
        self.sing = ['um','uma']
        self.pluri= ['uns','umas']

class subst(Palavra):#modifica apenas subst. de uma frase
    def __init__(self):
        Palavra.__init__(self)
        self.Ind = [1,4]

class verbo(Palavra):#modifica apenas a pessoa do verbo
    def __init__(self):
        Palavra.__init__(self)
        self.Ind = [2]

class conj_ar(verbo):#modifica apenas verbos da 1a conj.
    def __init__(self):
        verbo.__init__(self)
        self._3ps = ['a']

class conj_er_ir(verbo):#modifica apenas verbos da 2a e 3as conj.
    def __init__(self):
        verbo.__init__(self)
        self._3ps = ['e']
    
# Programa não funciona (ou talvez funcione, mas não se sabe bem como).
# ERRO 1 3 100
# ERRO 1 4 100
# ERRO 1 5 100
# ERRO 1 6 100
# ERRO 1 7 100

# ERRO 1 11 100
# ERRO 1 14 75
# ERRO 1 15 100
