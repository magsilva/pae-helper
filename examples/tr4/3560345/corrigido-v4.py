#Lista 4 - Herança
#Nomes:
#Cleber Castro Hage ....... número USP: 3560345
#Glauco Becaro ............... número USP: ????????
#Observação:
#A mudança de número acontece assim:
#Você escolhe se tudo se transforma para o PLURAL, SINGULAR ou o GÊNERO.
#É só chamar o s métodos. E *** O arquivo em TXT deve conter as frases separadas somente por espaço (' ')

import string #Biblioteca para manipulação de Strings
class Palavras: #Armazena todos os artigos, substantivos e verbos em uma lista de artigos, substantivos e verbos em ordem. #1o: Artigo 2o: Substantivo 3o: Verbo 4o:Artigo 5o:Substantivo
    def __init__(self): #Listas para todo o arquivo lido, artigos, substantivos, e verbos
        self.line = []
        self.artigos = []
        self.substantivos = []
        self.verbos = []
    def Leia(self):  #Ler o arquivo e colocar tudo em uma lista.
        i = 0  #Este e os outros indices são para achar os ' '
        t = 0
        Cont=0  # Para que quando chegue em 5 a frase já foi detectada.
        w=0
        k=0
        j= 0
        f = open ('teste.txt')
        self.line = str(f.read())   # Ler o arquivo inteiro
        f.close()
        while j != -1:
            if k == 0:
                i = self.line.find(' ',0)   #Artigo
                self.artigos.append(self.line[w:i])
                Cont+=1
                j = self.line.find(' ',i+1) #Substantivo
                if j != -1:
                    self.substantivos.append(self.line[i+1:j])
                    Cont+=1
                    if Cont != 5:
                        k = self.line.find(' ',j+1)  #Verbo
                        self.verbos.append(self.line[j+1:k])
                        Cont+=1
                    if Cont ==5:
                        Cont =0
            if k != 0:
                w = k +1
                i = self.line.find(' ',w)  #Artigo
                self.artigos.append(self.line[w:i])
                Cont+=1
                j = self.line.find(' ',i+1)  #Substantivo
                self.substantivos.append(self.line[i+1:j])
                Cont+=1
                if Cont != 5: #Se ainda não chegou ao fim da frase.
                    k = self.line.find(' ',j+1)
                    self.verbos.append(self.line[j+1:k])
                    Cont+=1
                if Cont ==5:  #Se já chegou ao fim da frase.
                    Cont =0
                    k= j
    def NumeroPLURAL(self):  # Transforma todos em PLURAL
        self.artigosPLURAL = []
        self.verbosPLURAL = []
        self.substantivosPLURAL = []
        p='a'
        for p in self.artigos:
            p = p + 's'
            self.artigosPLURAL.append(p)
        for p2 in self.verbos:
            p2 = p2 + 'm'
            self.verbosPLURAL.append(p2)
        for p3 in self.substantivos:
            p3 = p3 + 's'
            self.substantivosPLURAL.append(p3)
    def NumeroSINGULAR(self):  # Transforma todos em SINGULAR
        self.artigosSINGULAR = []
        self.verbosSINGULAR = []
        self.substantivosSINGULAR = []
        p='a'
        self.artigosA = str(self.artigos)
        self.verbosA = str(self.verbos)
        self.substantivosA = str(self.substantivos)
        for p in self.artigosA:
            self.artigosA.replace('s', '')
            self.artigosSINGULAR.append(p)
        for p2 in self.verbos:
            self.verbosA.replace('s', '')
            self.verbosSINGULAR.append(p2)
        for p3 in self.verbos:
            self.substantivosA.replace('s', '')
            self.substantivosSINGULAR.append(p3)
    def Genero(self):  # Transforma todos em seus GÊNEROS invertidos
        self.artigosGF = []
        self.substantivosGF = []
        self.artigosG = str(self.artigos)
        self.substantivosG = str(self.substantivos)
        for p1 in self.artigosG:
            l =  self.artigosG.rfind('o')
            self.artigosG[l].replace('o', 'a')
            self.artigosGF.append(p1)
        for p2 in self.artigosG:
            m =  self.substantivosG.rfind('o')
            self.substantivosG[m].replace('a', '')
            self.substantivosGF.append(p2)
        for p3 in self.artigosG:
            n =  self.substantivosG.rfind('o')
            self.substantivosG[n].replace('o', '')
        for p4 in self.artigosG:
            k =  self.substantivosG.rfind('a')
            self.substantivosG[k].replace('a', '')

class Artigo(Palavras):  #Derivada da classe Palavras e utiliza os métodos dela
    def NumeroSINGULAR(self):
        p='a'
        for p in self.artigosA:
            self.artigosA.replace('s', '')
            self.artigosSINGULAR.append(p)
        for p2 in self.verbos:
            self.verbosA.replace('s', '')
            self.verbosSINGULAR.append(p2)
        for p3 in self.verbos:
            self.substantivosA.replace('s', '')
            self.substantivosSINGULAR.append(p3)
    def NumeroPLURAL(self):
        p='a'
        for p in self.artigos:
            p = p + 's'
            self.artigosPLURAL.append(p)
        for p2 in self.verbos:
            p2 = p2 + 'm'
            self.verbosPLURAL.append(p2)
        for p3 in self.substantivos:
            p3 = p3 + 's'
            self.substantivosPLURAL.append(p3)
    def Genero(self):
        for p1 in self.artigosG:
            l =  self.artigosG.rfind('o')
            self.artigosG[l].replace('o', 'a')
            self.artigosGF.append(p1)
        for p2 in self.artigosG:
            m =  self.substantivosG.rfind('o')
            self.substantivosG[m].replace('a', '')
            self.substantivosGF.append(p2)
        for p3 in self.artigosG:
            n =  self.substantivosG.rfind('o')
            self.substantivosG[n].replace('o', '')
        for p4 in self.artigosG:
            k =  self.substantivosG.rfind('a')
            self.substantivosG[k].replace('a', '')
class Substantivo(Palavras):  #Derivada da classe Palavras e utiliza os métodos dela
    def NumeroSINGULAR(self):
        p='a'
        for p in self.artigosA:
            self.artigosA.replace('s', '')
            self.artigosSINGULAR.append(p)
        for p2 in self.verbos:
            self.verbosA.replace('s', '')
            self.verbosSINGULAR.append(p2)
        for p3 in self.verbos:
            self.substantivosA.replace('s', '')
            self.substantivosSINGULAR.append(p3)
    def NumeroPLURAL(self):
        p='a'
        for p in self.artigos:
            p = p + 's'
            self.artigosPLURAL.append(p)
        for p2 in self.verbos:
            p2 = p2 + 'm'
            self.verbosPLURAL.append(p2)
        for p3 in self.substantivos:
            p3 = p3 + 's'
            self.substantivosPLURAL.append(p3)
    def Genero(self):
        for p1 in self.artigosG:
            l =  self.artigosG.rfind('o')
            self.artigosG[l].replace('o', 'a')
            self.artigosGF.append(p1)
        for p2 in self.artigosG:
            m =  self.substantivosG.rfind('o')
            self.substantivosG[m].replace('a', '')
            self.substantivosGF.append(p2)
        for p3 in self.artigosG:
            n =  self.substantivosG.rfind('o')
            self.substantivosG[n].replace('o', '')
        for p4 in self.artigosG:
            k =  self.substantivosG.rfind('a')
            self.substantivosG[k].replace('a', '')
class Verbo(Palavras):  #Derivada da classe Palavras e utiliza os métodos dela
    def NumeroSINGULAR(self):
        p='a'
        for p in self.artigosA:
            self.artigosA.replace('s', '')
            self.artigosSINGULAR.append(p)
        for p2 in self.verbos:
            self.verbosA.replace('s', '')
            self.verbosSINGULAR.append(p2)
        for p3 in self.verbos:
            self.substantivosA.replace('s', '')
            self.substantivosSINGULAR.append(p3)
    def NumeroPLURAL(self):
        p='a'
        for p in self.artigos:
            p = p + 's'
            self.artigosPLURAL.append(p)
        for p2 in self.verbos:
            p2 = p2 + 'm'
            self.verbosPLURAL.append(p2)
        for p3 in self.substantivos:
            p3 = p3 + 's'
            self.substantivosPLURAL.append(p3)
    def Genero(self):
        for p1 in self.artigosG:
            l =  self.artigosG.rfind('o')
            self.artigosG[l].replace('o', 'a')
            self.artigosGF.append(p1)
        for p2 in self.artigosG:
            m =  self.substantivosG.rfind('o')
            self.substantivosG[m].replace('a', '')
            self.substantivosGF.append(p2)
        for p3 in self.artigosG:
            n =  self.substantivosG.rfind('o')
            self.substantivosG[n].replace('o', '')
        for p4 in self.artigosG:
            k =  self.substantivosG.rfind('a')
            self.substantivosG[k].replace('a', '')

# ERRO 1 11 100
# ERRO 1 12 100
# ERRO 1 14 50
# ERRO 1 15 100
a = Palavras()
a.Leia()
print a.NumeroPLURAL

# Programa não funciona
# ERRO 1 3 100
# ERRO 1 4 100
# ERRO 1 5 100
# ERRO 1 6 100
# ERRO 1 7 100
