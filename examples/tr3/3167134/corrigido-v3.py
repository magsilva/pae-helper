Resolucao da terceira lista de exercicios de Programacao Orientada a Objetos

Prof Dra. Renata Pontin M. Fortes




(1)-Resposta-



O construtor é utilizado para criar um Objeto de uma classe da mesma forma que uma variável precisa ser criada antes de ser utilizada e o destrutor apaga um objeto da memória quando este não é mais necessário liberando esta para uso.
Na sintaxe de python para criamos um construtor devemos utilizar:  def_ _init_ _(self [,args])  e para utilizarmos o destrutor podemos ter: def_ _del_ _(self) ou deixarmos que o interpretador o utilize por si so.

Podemos utilizar forma especiais de acesso aos atributor de uma classe, sao eles: def_ _getattr_ _(self, name), def
_ _setattr_ _(self,name,value) e def
_ _delattr_ _(self, name).

Os 5 principais conceitos  que consolidam o paradigma de ?Orientação a Objetos? são: 

- Tudo é um objeto
- Um programa é formado por um grupo de objetos que dizem a cada um o que fazer através de mensagens/métodos
- Cada objeto tem sua própria memória 
 	Pode ser formada por outros objetos
- Todo objeto tem uma classe (?tipo?)
- Todos os objetos de uma mesma classe podem receber as mesmas mensagens/ ser chamados pelos mesmos métodos
Podemos definir uma classe como:  É o principal mecanismo para se criar estruturas de dados e novos tipos de objetos.  Um Objeto pode ser definido como: Sao  os tipos de dados fundamentais tais como string, inteiros, listas etc e cada objeto possui uma identidade um tipo e um valor.
Um método é uma função que realiza alguma operação sobre um objetos quando o método é chamado.

As vantagens de se programar orientado a objetos são: Aumentar a produtividade do programador, maior expansibilidade e reuso do software e também controlar sua complexidade e seu custo de manutenção.



(2)- Resposta-



class Palavras:

    def __init__(self):

        self.string = palavra

    def Conta_char(self):

        return len(self.string)

    def Conta_o_char(self, palavra):

        return self.palavra.count(palavra)



(3)- Resposta-




class Palavras:

    def __init__(self, palavra=?  ?):

        self.string = palavra

    def Conta_char(self):

        return len(self.string)

    def Conta_o_char(self, palavra):

        return self.palavra.count(palavra)


str1=raw_input()

vetorpalavra = []
vetornumero = []
str2=""

tamanho = Palavras.Conta_char(str1)

i = 0

while i<tamanho:

    if str[i]<>" ":
        str2 = str2 + str[i]
    else
        vetorpalavra[i]=str2
        str2=""

    i= i+1

i=0
while vetorpalavra<>"":
    vetornumero[0]

]

(4)- Resposta-



def palavras:
    artigo=["o","a","os","as","um","uma"]
    substantivo=["gata","cao","cidade","carro","bicicleta"]
    verbo=["andou","pulou","correu","caiu","fugiu","lutou"]
    preposicao=["de","sobre","sob","embaixo"]

    indiceart=0
    indicesub=0
    indiceverb=0
    indiceprep=0
    indiceart=0
    indicesub=0

    while(indiceart<6):
        while(indicesub<5):
            while(indiceverb<6):
                while(indiceprep<4):
                    while(indiceart<6):
                        while(indicesub<5):
                            vetorfinal=[[artigo[indiceart]],[substantivo[indicesub]],[verbo[indiceverb]], [preposicao[indiceprep]],[artigo[indiceart]],[subtantivo[indicesub]]]
                            indicesub+=indicesub
                        indiceart+=indiceart
                    indiceprep+=indiceprep
                indiceverb+=indiceverb
            indicesub+=indicesub
        indiceart+=indiceart


















class Palavras:

    def __init__(self):

        self.string = palavra

    def Conta_char(self):

        return len(self.string)

    def Conta_o_char(self, palavra):

        return self.palavra.count(palavra)


str1=raw_input()
print str1




    
class Palavras:

    def __init__(self):

        self.string = palavra

    def Conta_char(self):

        return len(self.string)

    def Conta_o_char(self, palavra):

        return self.palavra.count(palavra)


str1=raw_input()

vetorpalavra = []
vetornumero = []
str2=""

tamanho = Palavras.Conta_char(str1)

i = 0

while i<tamanho:

    if str[i]<>" ":
        str2 = str2 + str[i]
    else
        vetorpalavra[i]=str2
        str2=""

    i= i+1

i=0
while vetorpalavra<>"":
    vetornumero[0]
    



    
def palavras:
    artigo=["o","a","os","as","um","uma"]
    substantivo=["gata","cao","cidade","carro","bicicleta"]
    verbo=["andou","pulou","correu","caiu","fugiu","lutou"]
    preposicao=["de","sobre","sob","embaixo"]

    indiceart=0
    indicesub=0
    indiceverb=0
    indiceprep=0
    indiceart=0
    indicesub=0

    while(indiceart<6):
        while(indicesub<5):
            while(indiceverb<6):
                while(indiceprep<4):
                    while(indiceart<6):
                        while(indicesub<5):
                            vetorfinal=[[artigo[indiceart]],[substantivo[indicesub]],[verbo[indiceverb]], [preposicao[indiceprep]],[artigo[indiceart]],[subtantivo[indicesub]]]
                            indicesub+=indicesub
                        indiceart+=indiceart
                    indiceprep+=indiceprep
                indiceverb+=indiceverb
            indicesub+=indicesub
        indiceart+=indiceart

        
# ERRO TOTAL 1 4
# ERRO TOTAL 1 5
# ERRO TOTAL 1 8
# ERRO PARCIAL 1 9
# ERRO TOTAL 1 1
# ERRO TOTAL 1 2
# ERRO TOTAL 1 7
# ERRO TOTAL 1 6

# ERRO TOTAL 2 1

# ERRO TOTAL 3 1
# ERRO TOTAL 3 3
# ERRO TOTAL 3 5

# ERRO TOTAL 4 1
# ERRO TOTAL 4 4
# ERRO TOTAL 4 6
# ERRO TOTAL 4 7
# ERRO TOTAL 4 8
