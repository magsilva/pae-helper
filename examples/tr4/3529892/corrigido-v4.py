#Lucas Shindi Shimo 3529892
#Lista de POO Heranca
#Prof. Renata

class Frases:
    def __init__(self,filename):
        fp = open (filename)
        rd = fp.readlines()
        self.frases = []
        for aux in rd:
            aux=aux[:-1]
            self.frases.append(aux)
            

    def genero(self):
        for frase in self.frases:
            aux = Frase(frase)
            print aux.genero()

    def numero(self):
        for frase in self.frases:
            aux = Frase(frase)
            print aux.numero()            

class Frase:
    def __init__(self,frase):
        self.frase=frase.split(" ")
    def genero(self):
        i=1
        out=[]
        ret=""
        for palavra in self.frase:
            if ( (i==1)or(i==4) ):
                if (palavra in ['o','a','os','as']) :
                    aux=ArtigoDefinido(palavra)
                    out.append(aux.genero() )
                else:
                    aux=ArtigoIndefinido(palavra)
                    out.append(aux.genero() )
            elif(i==2)or(i==5):
                aux=Substantivo(palavra)
                out.append(aux.genero() )
            elif(i==3):
                if(palavra[-1]== 'm'):
                    if(palavra[-2]=='a'):
                        aux=Conj1(palavra)
                        out.append(aux.genero() )
                    else:
                        aux=Conj2(palavra)
                        out.append(aux.genero() )
                else:
                    if(palavra[-1]=='a'):
                        aux=Conj1(palavra)
                        out.append(aux.genero() )
                    else:
                        aux=Conj2(palavra)
                        out.append(aux.genero() )
            i+=1
        for pal in out:
            ret += pal + " "
        return ret[:-1]


    def numero(self):
        i=1
        out=[]
        ret=""
        for palavra in self.frase:
            if ( (i==1)or(i==4) ):
                if (palavra in ['o','a','os','as']) :
                    aux=ArtigoDefinido(palavra)
                    out.append(aux.numero() )
                else:
                    aux=ArtigoIndefinido(palavra)
                    out.append(aux.numero() )
            elif(i==2)or(i==5):
                aux=Substantivo(palavra)
                out.append(aux.numero() )
            elif(i==3):
                if(palavra[-1]== 'm'):
                    if(palavra[-2]=='a'):
                        aux=Conj1(palavra)
                        out.append(aux.numero() )
                    else:
                        aux=Conj2(palavra)
                        out.append(aux.numero() )
                else:
                    if(palavra[-1]=='a'):
                        aux=Conj1(palavra)
                        out.append(aux.numero() )
                    else:
                        aux=Conj2(palavra)
                        out.append(aux.numero() )
            i+=1
        for pal in out:
            ret += pal + " "
        return ret[:-1]

class Palavra:
    def __init__(self,pal):
        self.palavra = pal

    def __str__(self):
        return self.palavra

class Artigo(Palavra):
    def __init__(self,art):
        Palavra.__init__(self,art)

class ArtigoDefinido(Artigo):
    def __init__(self,artd):
        Artigo.__init__(self,artd)

    def genero(self):
        if(self.palavra=='o'):
            return 'a'
        elif(self.palavra=='a'):
            return 'o'
        elif(self.palavra=='os'):
            return 'as'
        elif(self.palavra=='as'):
            return 'os'
            
    def numero(self):
        if(self.palavra=='o'):
            return 'os'
        elif(self.palavra=='os'):
            return 'o'
        elif(self.palavra=='a'):
            return 'as'
        elif(self.palavra=='as'):
            return 'a'
            
class ArtigoIndefinido(Artigo):
    def __init__(self,arti):
        Artigo.__init__(self,arti)

    def genero(self):
        if(self.palavra=='um'):
            return'uma'
        elif(self.palavra=='uma'):
            return'um'
        elif(self.palavra=='uns'):
            return 'umas'
        elif(self.palavra=='umas'):
            return 'uns'
            
    def numero(self):
        if(self.palavra=='um'):
            return'uns'
        elif(self.palavra=='uns'):
            return 'um'
        elif(self.palavra=='uma'):
            return 'umas'
        elif(self.palavra=='umas'):
            return 'uma'            

class Substantivo(Palavra):
    def __init__(self,sub):
        Palavra.__init__(self,sub)

    def genero(self):
        if(self.palavra[-1]=='o'):
            return self.palavra[:-1]+'a'
        elif(self.palavra[-1]=='a'):
            return self.palavra[:-1]+'o'
        elif(self.palavra[-2:]=='os'):
            return self.palavra[:-2]+'as'
        elif(self.palavra[-2:]=='as'):
            return self.palavra[:-2]+'os'
            
    def numero(self):
        if(self.palavra[-1]=='o'):
            return self.palavra[:-1]+'os'
        elif(self.palavra[-1]=='a'):
            return self.palavra[:-1]+'as'
        elif(self.palavra[-2:]=='as'):
            return self.palavra[:-2]+'a'
        elif(self.palavra[-2:]=='os'):
            return self.palavra[:-2]+'o'

class Verbo(Palavra):
    def __init__(self,ver):
        Palavra.__init__(self,ver)

class Conj1(Verbo):
    def __init__(self,conj1):
        Verbo.__init__(self,conj1)

    def genero(self):
        return self.palavra

    def numero(self):
        if(self.palavra[-1]=='a'):
            return self.palavra + 'm'
        else:
            return self.palavra[:-1]

class Conj2(Verbo):
    def __init__(self,conj1):
        Verbo.__init__(self,conj1)

    def genero(self):
        return self.palavra
    
    def numero(self):
        if(self.palavra[-1]=='e'):
            return self.palavra + 'm'
        else:
            return self.palavra[:-1]

# ERRO 1 11 50
# ERRO 1 15 25
a = Frases( "frases.txt" )
a.genero()
a.numero()

# Programa não funciona
# ERRO 1 3 100
# ERRO 1 4 100
# ERRO 1 5 100
# ERRO 1 6 100
# ERRO 1 7 100
