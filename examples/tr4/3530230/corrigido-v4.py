#Hugo Degiovanni Junior nUsp:3530230
#Chen Xu Sheng          nusp:

#Exercicio de Heranca
class Arquivo:
    def __init__(self,nomearquivo):
        f=open(nomearquivo)
        lista=f.readlines()
        self.arquivo=[]
        for a in lista:
            a=a[:-1]
            self.arquivo.append(a)
        
    def genero(self):
        for a in self.arquivo:
            frase=Frase(a)
            print frase.genero()

    def numero(self):
        for a in self.arquivo:
            frase=Frase(a)
            print frase.numero()


class Frase:
    def __init__(self,frase):
        self.frase=frase.split(" ")

    def genero(self):
        indice=1
        saida=[]
        retorno=""
        for palavra in self.frase:
            if ( (indice==1)or(indice==4)):
                if (palavra in ['o','a','os','as']):
                    outra=ArtDefinido(palavra)
                    saida.append(outra.genero())
                else:
                    outra=ArtIndefinido(palavra)
                    saida.append(outra.genero())
            elif((indice==2)or(indice==5)):
                outra=Substantivo(palavra)
                saida.append(outra.genero())
            elif(indice==3):
                if(palavra[-1]=='m'):
                    if(palavra[-2]=='a'):
                        outra=Priconj(palavra)
                        saida.append(outra.genero())
                    else:
                        outra=Segconj(palavra)
                        saida.append(aux.genero())
                else:
                    if(palavra[-1]=='a'):
                        outra=Priconj(palavra)
                        saida.append(outra.genero())
                    else:
                        outra=Segconj(palavra)
                        saida.append(outra.genero())
            i+=1
        for palavra in saida:
            retorno += palavra + " "
        return retorno[:-1]
        
    def numero(self):
        indice=1
        saida=[]
        retorno=""
        for palavra in self.Frase:
            if ( (indice==1)or(indice==4)):
                if (palavra in ['o','a','os','as']):
                    outra=ArtDefinido(palavra)
                    saida.append(outra.genero())
                else:
                    outra=ArtIndefinido(palavra)
                    saida.append(outra.genero())
            elif((indice==2)or(indice==5)):
                outra=Substantivo(palavra)
                saida.append(outra.genero())
            elif(indice==3):
                if(palavra[-1]=='m'):
                    if(palavra[-2]=='a'):
                        outra=Priconj(palavra)
                        saida.append(outra.genero())
                    else:
                        outra=Segconj(palavra)
                        saida.append(aux.genero())
                else:
                    if(palavra[-1]=='a'):
                        outra=Priconj(palavra)
                        saida.append(outra.genero())
                    else:
                        outra=Segconj(palavra)
                        saida.append(outra.genero())
            i+=1
        for palavra in saida:
            retorno += palavra + " "
        return retorno[:-1]    
class Palavra:
    def __init__(self,palavra):
        self.palavra=palavra
    def __str__(self):
        return self.palavra
class Artigo(Palavra):
    def __init__(self,artigo):
        Palavra.__init__(self.art)
class ArtDefinido(Artigo):
    def __init__(self,defi):
        Artigo.__init__(self,defi)
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
        elif(self.palavra=='a'):
            return 'as'
        elif(self.palavra=='os'):
            return 'o'
        elif(self.palavra=='as'):
            return 'a'

class ArtIndefinido(Artigo):
    def __init__(self,indefi):
        Artigo.__init__(self,indefi)
    def genero(self):
        if(self.palavra=='um'):
            return 'uma'
        elif(self.palavra=='uma'):
            return 'um'
        elif(self.palavra=='uns'):
            return 'umas'
        elif(self.palavra=='umas'):
            return 'uns'

    def numero(self):
        if(self.palavra=='um'):
            return 'uns'
        elif(self.palavra=='uma'):
            return 'umas'
        elif(self.palavra=='uns'):
            return 'um'
        elif(self.palavra=='umas'):
            return 'uma'

class Substantivo(Palavra):
    def __int__(self,sub):
        Palavra.__ini__(self,subs)
        
    def genero(self):
        if(self.palavra[-1]=='o'):
            return self.palavra[:-1]=='a'
        elif(self.palavra[-1]=='a'):
            return self.palavra[:-1]+'o'
        elif(self.palavra[-1]=='os'):
            return self.palavra[:-1]=='as'
        elif(self.palavra[-1]=='as'):
            return self.palavra[:-1]+'os'

    def numero(self):
        if(self.palavra[-1]=='o'):
            return self.palavra[:-1]=='os'
        elif(self.palavra[-1]=='a'):
            return self.palavra[:-1]+'as'
        elif(self.palavra[-1]=='os'):
            return self.palavra[:-1]=='o'
        elif(self.palavra[-1]=='as'):
            return self.palavra[:-1]+'a'

class Verbo(Palavra):
    def __init__(self,verbo):
        Palavra.__init__(self,verbo)

class Priconj(Verbo):
    def __init__(self,pricon):
        Verbo.__init__(self,pricon)

    def genero(self):
        return self.palavra
    
    def numero(self):
        if(self.palavra[-1]=='a'):
            return self.palavra + 'm'
        else:
            return self.palavra[:-1]

class Segconj(Verbo):
    def __init__(self,segcon):
        Verbo.__init__(self,segcon)

    def genero(self):
        return self.palavra
    
    def numero(self):
        if(self.palavra[-1]=='e'):
            return self.palavra + 'm'
        else:
            return self.palavra[:-1]
        

a = Arquivo( "frase.txt" )
a.genero()
a.numero()

# ERRO 1 11 50
# ERRO 1 15 25

# Programa não funciona
# ERRO 1 3 100
# ERRO 1 4 100
# ERRO 1 5 100
# ERRO 1 6 100
# ERRO 1 7 100
