Eduardo Alves Ferreira
Eduardo Martinelli

1) 
Construtor de um objeto � uma fun��o que � chamada toda vez que o objeto � criado, e destrutor � uma fun��o chamada quando o objeto � liberado da mem�ria ou no t�rmino do programa. O construtor � empregado sobracarregando-se a fun��o __init__(), e o destrutor, __del__

# ERRO TOTAL 1 4

Acesso p�blico (para todos os c�digos, tanto dentro e fora do escopo da classe) e privado, acess�vel somente dentro da classe.

Os cinco conceitos s�o classes, objetos, heran�a, polimorfismo e encapsulamento.

Uma classe � uma esp�cie de estrutura que � instanciada em um objeto, que executa c�digos e armazena valores. Os m�todos da classe s�o os c�digos que o objeto executa, ou seja, as fun��es.

As vantagens da programa��o orientada a objeto � que com objetos pode-se criar uma modelagem mais pr�xima do mundo real que com as linguagens procedurais, o reuso de c�digo � muito mais simples e trata-se do escopo das vari�veis com muito mais facilidade.



2 )

class palavra:
�� �def __init__(self,pal):
�� � � �self.palavra = pal
�� � � �self.caracter = 0
�� � � �self.cont = 0
�� � � �self.cont1 = 0 
�� �def conta_char(self):
�� � � �self.caracter = len(self.palavra)
�� � � �print ("O numero de caracteres da palavra eh: " , self.caracter)
�� �def conta_o_char(self, char):
�� � � �self.cont1 = self.caracter
�� � � �for i in range(0,self.cont1):
�� � � � � �if self.palavra[i] == char:
�� � � � � � � �self.cont+=1

�� � � �print self.cont


3 )

class palavra:
�� �def __init__(self,pal):
�� � � �self.palavra = pal
�� � � �self.caracter = 0
�� � � �self.cont = 0
�� � � �self.cont1 = 0
�� � � �self.frase1 = []
�� �def conta_char(self):
�� � � �self.caracter = len(self.palavra)
�� � � �return self.caracter #conta o nro de caracteres 



class npalavras:
�� �def __init__(self, frase):
�� � � �self.frase = frase
�� � � �self.cont = 0
�� � � �self.cont1 = 0
�� � � �self.var = 0
�� � � �self.vazia = []
�� � � �self.nrocar = []
�� � � �self.nrocar1 = [] #listas de auxilio
�� �def pal(self):
�� � � �self.var = len(self.frase)
�� � � �for i in range(0,self.var):
�� � � � � �if self.frase[i] == " ":
�� � � � � � � �self.cont+=1
�� � � �self.cont1 = self.cont + 1
�� � � �print self.cont1 � #funcao retorna o numero de palavras da frase

�� �def conta(self):
�� � � �for i in range(0,self.var):
�� � � � � �if self.frase[i] == " ":
�� � � � � � � �self.vazia.append(i) #guarda posicao do espaco em branco
�� � � �#aqui guarda-se a posicao do espaco em branco
�� � � 
�� � � �self.nrocar.append(palavra(self.frase[0:self.vazia[0]]).conta_char())
�� � � �#eh colocado em nrocar o numero de carac. da primeira palavra
�� � � �self.nrocar.append(palavra(self.frase[(self.vazia[-1]+1):self.var]).conta_char())
�� � � �#eh colocado em nrocar o numero de carac. da segunda palavra

�� � � �for i in range(0,len(self.vazia) -1):
�� � � � � �self.nrocar1.append(palavra(self.frase[(self.vazia[i]+1):self.vazia[i+1]]).conta_char())
�� � � � � �#for que conta o numero de carac. das palavras do meio, por isso eh chamado self.vazia[i] +1, e self.vazia[i+1]
�� � � � � �#posicao self.vazia[i+1] para a prox posicao do espago em branco


�� � � �print("O nro de caracteres das palavras i respectivamente:",self.nrocar[0],self.nrocar1,self.nrocar[1])

# ERRO TOTAL 3 4
# ERRO TOTAL 3 5


4 )

from random import randint
def frases():
�� �artigo = ("o","a","um","uma")
�� �subst = ("gata","cco","cidade","carro")
�� �verbo = ("andou","correu","pulou","caiu")
�� �prep = ("de","sobre","sob","embaixo")
�� �subst2 = ("patins","bicicleta","ponte","estrada")
�� �#definicao em tuplas, das palavras
�� �fra �= []
�� �fra2 = []
�� �fra3 = []
�� �fra4 = []
�� �fra5 = []
�� �fra6 = []
�� �#vetores necessarios
�� �

��
�� �for i in range(0,20):
�� � � �g = randint(0,3)
�� � � �fra.append(artigo[g])#acumula artigos randomicos em fra
�� � � �g1 = randint(0,3)
�� � � �fra2.append(subst[g1])#acumula substantivos randomicos em fra2
�� � � �g2 = randint(0,3)
�� � � �fra3.append(verbo[g2])#acumula verbos randomicos em fra3
�� � � �g3 = randint(0,3)
�� � � �fra4.append(prep[g3])#acumula preposigues randomicas em fra4
�� � � �g4 = randint(0,3)
�� � � �fra5.append(subst2[g4])#acumula substantivos randomicos em fra5

�� � � �fra6.append(fra[i] + (" ")+ (fra2[i]) + (" ") + fra3[i] + (" ") + �fra4[i] + (" ") + fra5[i] + ".")
�� � � �#acumula em fra6 as palavras juntas, gerando as frases


�� �for i in range(0,20):
�� � � �print fra6[i] #imprime fra6, ou seja, as frases randomicas
�� � � �

# ERRO PARCIAL 4 5 Falta o uso deo artigo depois da preposi��o.
# ERRO TOTAL 4 7
# ERRO TOTAL 4 6


�� � � �

