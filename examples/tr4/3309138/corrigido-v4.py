class Artigo_def:
    def __init__(self, ad):
        self.ad = ad


class Artigo_indef:
    def __init__(self, ai):
        self.ai = ai


class Primeira_conj:
    def __init__(self, v):
        self.v = v


class Segunda_conj:
    def __init__(self, v):
        self.v = v


class Terceira_conj:
    def __init__(self, v):
        self.v = v


class Substantivo:
    def __init__(self, s):
        self.s = s

    def plural2 (self, s):
        i = len (s)
        if (((s[i-1])<>"s")and((s[i-1])<>"S")):
            aux = "s"
            self.s = s + aux
        else:
            self.s = s
        return (self.s)

    def alt_genero2 (self, s):
        i = len(s)
        aux = s [0:i-1]
        if ((s[i-1])=="o"):
            aux = aux + "a"
        elif ((s[i-1])=="O"):
            aux = aux + "A"
        elif ((s[i-1])=="s"):    
            if ((s[i-2])=="o"):
                aux = s[0:i-2]
                aux = aux + "as"
            elif ((s[i-2])=="a"):
                aux = s[0:i-2]
                aux = aux + "os"
            else:
                aux = s
        elif ((s[i-1])=="S"):    
            if ((s[i-2])=="O"):
                aux = s[0:i-2]
                aux = aux + "AS"
            elif ((s[i-2])=="A"):
                aux = s[0:i-2]
                aux = aux + "OS"
            else:
                aux = s
        elif ((s[i-1])=="a"):
            aux = aux + "o"
        elif ((s[i-1])=="A"):
            aux = aux + "O"
        else:
            aux = s
        self.s = aux
        return (self.s)

class Artigo (Artigo_def, Artigo_indef):
    def __init__ (self, art):        
        if ((art == "a")or(art=="o")or(art=="os")or(art=="as")or(art == "A")or(art=="O")or(art=="OS")or(art=="AS")):
            Artigo_def.__init__(self, art)
        if ((art == "um")or(art=="uma")or(art=="uns")or(art=="umas")or(art == "UM")or(art=="UMA")or(art=="UNS")or(art=="UMAS")):
            Artigo_indef.__init__(self, art)

    def alt_genero1 (self, a):
        i = len(a)
        if (i == 1):
            if (a=="o"):
                self.a = "a"
            elif (a=="O"):
                self.a = "A"
            elif (a=="A"):
                self.a = "O"
            else:
                self.a="o"
        else:
            if (a=="um"):
                self.a = "uma"
            elif (a=="Um"):
                self.a = "Uma"
            elif (a=="UM"):
                self.a = "UMA"
            elif (a=="UMA"):
                self.a = "UM"
            elif (a=="Uma"):
                self.a = "Um"
            else:
                self.a="um"
        return (self.a)

    def plural1 (self, ai):
        i = len (ai)
        if (i==1):
            self.ai = ai + "s"
        else:
            aux = "s"
            if (ai == "um"):
                ai = "un"
            elif (ai == "Um"):
                ai = "Un"
            elif (ai == "UM"):
                ai = "UN"
                aux = "S"
            self.ai = ai + aux
        return (self.ai)

class Verbo (Primeira_conj, Segunda_conj, Terceira_conj):
    def __init__(self, verb):
        aux = len(verb)
        letra1 = verb[aux-2]
        letra2 = verb[aux-1]
        if ((((letra1=="a") and (letra2=="m"))or(letra2=="a"))or(((letra1=="A") and (letra2=="M"))or(letra2=="A"))):
            Primeira_conj.__init__(self, verb)
        elif ((((letra1=="e") and (letra2=="m"))or(letra2=="e"))or(((letra1=="E") and (letra2=="M"))or(letra2=="E"))):
            Segunda_conj.__init__(self, verb) 
        elif ((((letra1=="i") and (letra2=="m"))or(letra2=="i"))or(((letra1=="I") and (letra2=="M"))or(letra2=="I"))):
            Terceira_conj.__init__(self, verb)

    def plural3 (self, v):
        i = len (v)
        if ((v[i-1])=="i"):
            aux = v[0:i-1]
            v = aux + "e"
        elif ((v[i-1])=="I"):
            aux = v[0:i-1]
            v = aux + "E"
        aux = "m"
        self.v = v + aux
        return (self.v)

    def alt_genero3 (self, verb):
        return (verb)

class Palavra (Artigo, Substantivo, Verbo):
    def __init__(self, pal, pos):
        if ((pos==1)or(pos==4)):
            Artigo.__init__(self, pal)
        elif ((pos==2)or(pos==5)):
            Substantivo.__init__(self, pal)
        elif (pos==3):
            Verbo.__init__(self, pal)

class Frase (Palavra):
    def __init__(self, pal1, pal2, pal3, pal4, pal5):
        Palavra (pal1, 1)
        Palavra (pal2, 2)
        Palavra (pal3, 3)
        Palavra (pal4, 4)
        Palavra (pal5, 5)

    def numero (self):
        pala1 = self.plural1(pal1)
        pala2 = self.plural2(pal2)
        pala3 = self.plural3(pal3)
        pala4 = self.plural1(pal4)
        pala5 = self.plural2(pal5)
        fr = pala1 + " " + pala2 + " " + pala3 + " " + pala4 + " " + pala5
        print (fr)

    def alt_genero (self):
        pala1 = self.alt_genero1(pal1)
        pala2 = self.alt_genero2(pal2)
        pala3 = self.alt_genero3(pal3)
        pala4 = self.alt_genero1(pal4)
        pala5 = self.alt_genero2(pal5)
        fr = pala1 + " " + pala2 + " " + pala3 + " " + pala4 + " " + pala5
        print (fr)

f = open ("frases.txt", "r")
linha = f.readline()
while linha:
    i=0
    j=0
    k=0
    pal = ""
    while ((linha[j]<>" ")and(linha[j]<>"\n")):
        j = j+1
        k = k+1
    while (k>i):
       k = k-1
    j = j+1
    i = j
    pal = linha[k:j-1]
    k = j
    pal1 = pal
    while ((linha[j]<>" ")and(linha[j]<>"\n")):
        j = j+1
        k = k+1
    while (k>i):
       k = k-1
    j = j+1
    i = j
    pal = linha[k:j-1]
    k = j
    pal2 = pal
    while ((linha[j]<>" ")and(linha[j]<>"\n")):
        j = j+1
        k = k+1
    while (k>i):
       k = k-1
    j = j+1
    i = j
    pal = linha[k:j-1]
    k = j
    pal3 = pal
    while ((linha[j]<>" ")and(linha[j]<>"\n")):
        j = j+1
        k = k+1
    while (k>i):
       k = k-1
    j = j+1
    i = j
    pal = linha[k:j-1]
    k = j
    pal4 = pal
    while ((linha[j]<>" ")and(linha[j]<>"\n")):
        j = j+1
        k = k+1
    while (k>i):
       k = k-1
    j = j+1
    i = j
    pal = linha[k:j-1]
    k = j
    pal5 = pal
    frase1 = Frase (pal1, pal2, pal3, pal4, pal5)
    print "A seguinte frase foi lida do arquivo:"
    print linha
    print "Modificando o gênero da frase:"
    frase1.alt_genero()
    print ""
    print "Passando a frase para o plural:"
    frase1.numero()
    print "\n"
    linha = f.readline()
f.close()

# ERRO 1 10 50
# ERRO 1 11 100
# ERRO 1 14 75
