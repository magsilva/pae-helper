class conj:
    def __init__(self,*z):
        #inicializa o objeto com parametros arbitrarios
        self.lista=[]
        for j in z:
            if type(j) ==int:
                self.push(j)
            elif j.__class__ == conj:
                self.lista.extend(j.lista)
                print "Objeto Inserido"
            else:
                print "Parametro Invalido"
            
    def push(self,x):
        #insere elemento x no objeto
        if (type(x)==int):
            if self.lista.count(x) < 1 :
                self.lista.append(x)
                print "Numero %d Inserido"%x
            else:
                print "Numero Repetido"
        else:
            print "Somente Numeros Inteiros"

    def pop(self,x):
        #remove elemento x do objeto
        if x in self.lista:
            self.lista.remove(x)
            print "Elemento removido"
        else:
            print "O elemento nao esta na lista"

    def imprime(self):
        #imprime a lista do objeto
        print self.lista

# ERRO 1 2

    def __add__(self,obj2):
        #retorna uniao de dois objetos
        import copy
        laux=copy.deepcopy(self.lista)
        for aux in obj2.lista:
            if aux not in laux:
                laux.append(aux)
        return laux

    def __div__(self,obj2):
        #retorna interseccao de dois obejtos
        laux=[]
        for aux in obj2.lista:
            if aux in self.lista:
                laux.append(aux)
        return laux
    
    def __sub__(self,obj2):
        #retorna subtracao de dois objetos
        laux=self.lista
        for aux in obj2.lista:
            if aux in laux:
                laux.remove(aux)
        return laux

#--------------------------FIM CLASSE CONJ--------------
import copy

class tag_analyser:
    def __init__(self,nomearq):
        aux=0
        self.log=[]
        self.frases=frases(nomearq)

        while aux < self.frases.nfrase:
            self.palavras=palavras(self.frases.frase[aux])
            self.tags=tags(self.palavras.palavra)
            self.log.append("linha %d - %d palavras - %d tags %s - %d tags-problemas"
                  %(aux+1,self.palavras.npalavra,self.tags.ntag,
                    self.tags.tag,self.tags.etag) )
            aux += 1

    def save_log(self,nomearq):
        f=open(nomearq,"w")
        aux=0
        while aux < self.frases.nfrase:
            f.write("%s \n"%self.log[aux])
            aux += 1


class frases:
    def __init__(self,filename):
        f=open(filename,'r')
        self.frase=f.readlines()
        self.nfrase=len(self.frase)
        f.close()

        
class palavras:
    def __init__(self,frase): #frase eh apenas uma frase a ser analisada
        aux=copy.deepcopy(frase)
        self.palavra=[]
        
        while aux.find(" ")>0:
            j=aux.find(" ")
            self.palavra.append(aux[:j])
            aux=aux[j+1:]

        self.palavra.append(aux)
        self.npalavra=len(self.palavra)
        
        
class tags:
    def __init__(self,entrada): #entrada eh lista de palavras
        self.tag=[]
        self.ntag=0
        self.etag=0
        
        for aux in entrada:
            if aux[0]=='<' and aux[-1]=='>':
                self.tag.append(aux)
            elif aux[0]=='<' or aux[-1]=='>':
                self.etag += 1

        self.ntag= len(self.tag)

# erro 2 23
