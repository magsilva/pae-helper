#Marcelo Kenji Hotta 3460142    kenji@grad.icmc.usp.br

# ERRO TOTAL 1 1
# ERRO TOTAL 1 2
# ERRO TOTAL 1 3
# ERRO TOTAL 1 4
# ERRO TOTAL 1 5
# ERRO TOTAL 1 6
# ERRO TOTAL 1 7
# ERRO TOTAL 1 8
# ERRO TOTAL 1 9
# ERRO TOTAL 1 10

#2----------------------------------------------------------------------
class Palavras:
    def __init__(self, frase):
        self.list = []
        while frase.count(" "):
                while frase[0] == " ":
                    frase = frase[1:]
                self.list.append(frase[:frase.index(" ")])
                frase = frase[frase.index(" ") + 1:]
        self.list.append(frase)
    def Conta_char(self):
        result = []
        for x in self.list:
            print x, len(x), "letras"
    def Conta_o_char(self, char):
        print "Ocorrencias da letra", char, "\n"
        for x in self.list:
            cont = 0
            for y in range(len(x)):
                if x[y] == char:
                    cont = cont + 1
            print x,": ", cont

#3---------------------------------------------------------------------------
class Frases:
    def __init__(self):
        self.list = []
        self.Le_frases()
    def Le_frases(self):
        print "Escreva o texto, <ENTER> para terminar"
        linha = raw_input()
        while linha != "":
            self.list.append(linha)
            linha = raw_input()

def E3():  #para executar faca E3()
    Input = Frases()
    total = []
    for f in Input.list:
        tmp = Palavras(f)
        total.extend(tmp.list)
    print total
    maxlen = -1
    for p in total:
        if len(p) > maxlen:
            maxlen = len(p)
    while maxlen > 0:
        count = 0
        for p in total:
            if len(p) == maxlen:
                count += 1
        if count:
            print count, "palavras de", maxlen, "letras"
        maxlen -= 1

#4-------------------------------------------------------------------------
import random
def E4(): #para executar basta fazer:   E4()
    artigo = ("o", "a", "um", "uma")
    substantivo = ("gata", "cao", "cidade", "carro", "bicicleta")
    verbo = ("andou", "correu", "pulou", "caiu")
    preposicao = ("de", "sobre", "sob", "embaixo")
    
    for n in range(1, 20):
        temp = random.choice(artigo) + " " + random.choice(substantivo) + " " + random.choice(verbo) + " " + random.choice(preposicao) + " " + random.choice(artigo) + " " + random.choice(substantivo) + "."
#temp = artigo[int(random.random()*len(artigo))]    (ex: usando numero randomico)
        temp = temp.capitalize()
        print temp

# ERRO TOTAL 4 8
