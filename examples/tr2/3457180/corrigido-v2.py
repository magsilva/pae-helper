Programa��o Orientada � Objetos

2� Lista de exerc�cios - 2� parte (Classes)

Lucas Antiqueira --- 3457180
Marcus Secato --- 3285140



1- 

	Para criar um conjunto vazio, basta utilizar o construtor da classe sem par�metros. Para inicializar o objeto com n�meros inteiros ou objetos dessa mesma classe, � necess�rio coloc�-los como par�metro do construtor, todos dentro de uma lista. N�meros repetidos e valores n�o inteiros n�o s�o inseridos no conjunto. O conjunto de n�meros inteiros � representado internamente como uma lista.
	Os m�todos para uni�o, intersec��o e subtra��o de conjuntos s�o implementados utilizando sobrecarga de operadores ('+', '*', e '-', respectivamente). A diferen�a entre o m�todo 'agrega' e o m�todo '__add__' reside no fato de que o m�todo 'agrega' realiza uma uni�o de conjuntos in loco (o objeto self � alterado, ao inv�s de retornar um novo objeto) a fim de utiliz�-lo no construtor da classe.

Exemplo de execu��o:

>>> um = ConjuntoInteiros([4,'lixo',6,4,8,3,5,7,6])
>>> um.escreve()
[4, 6, 8, 3, 5, 7]
>>> dois = ConjuntoInteiros([30,8,10,4,98,6,um])
>>> dois.escreve()
[30, 8, 10, 4, 98, 6, 3, 5, 7]
>>> dois.remocao(6)
>>> dois.remocao(8)
>>> dois.escreve()
[30, 10, 4, 98, 3, 5, 7]
>>> tres = um * dois
>>> tres.escreve()
[4, 3, 5, 7]


C�digo da classe:

# ERRO 1 3 Pode adicionar objetos que n�o s�o n�meros inteiros se eles estiverem numa lista.
class ConjuntoInteiros:
    def __init__(self, lista=[]):
        i=0
        self.conjunto = []
        while i < len(lista):
            if type(lista[i]) is int:
                if self.conjunto.count(lista[i]) == 0:
                    self.conjunto.append(lista[i])
            if type(lista[i]) is type(self):
                self.agrega(lista[i])
            i=i+1

    def agrega(self, operando):
        i=0
        while i < len(operando.conjunto):
            if self.conjunto.count(operando.conjunto[i]) == 0:
                self.conjunto.append(operando.conjunto[i])
            i=i+1

    def __add__(self, operando):
        i=0
        aux = copy.deepcopy(self)
        while i < len(operando.conjunto):
            if aux.conjunto.count(operando.conjunto[i]) == 0:
                aux.conjunto.append(operando.conjunto[i])
            i=i+1
        return aux

    def __mul__(self, operando):
        i=0
        aux = ConjuntoInteiros()
        while i < len(self.conjunto):
            if operando.conjunto.count(self.conjunto[i]) > 0:
                aux.conjunto.append(self.conjunto[i])
            i=i+1
        return aux

    def __sub__(self, operando):
        i=0
        aux = copy.deepcopy(self)
        while i < len(operando.conjunto):
            if aux.conjunto.count(operando.conjunto[i]) > 0:
                aux.conjunto.remove(operando.conjunto[i])
            i=i+1
        return aux

    def adicao(self, elemento):
        if type(elemento) is int:
            if self.conjunto.count(elemento) == 0:
                self.conjunto.append(elemento)

    def remocao(self, elemento):
        self.conjunto.remove(elemento)

    def escreve(self):
        print(self.conjunto)



# ERRO 2 23

2- O programa possui tr�s classes.  A classe Frases realiza a abertura do arquivo fornecido pelo usu�rio, conta o n�mero de linhas e escreve em um arquivo de sa�da o n�mero de linhas, palavras e tags, defeituosas ou n�o, pois Frases utiliza m�todos de outras classes. A classe Palavras possui m�todo para contar o n�mero de palavras em uma linha e a classe Tags possui m�todos para contar tanto tags v�lidas como tags defeituosas. O m�todo display da classe Tags armazena as tags consideradas v�lidas para depois serem escritas no arquivo pela classe Frases.
Abaixo o c�digo do programa:

class Frases:
�� �def __init__(self, filein, fileout):
�� � � �self.fin = open(filein, 'r')
�� � � �self.fout = open(fileout, 'w')
�� �def avalia(self):
�� � � �words = Palavras()
�� � � �tags = Tags()
�� � � �self.numlines = 0
�� � � �line = self.fin.readline() � � � �
�� � � �while line != '':
�� � � � � �self.numlines = self.numlines+1
�� � � � � �self.fout.write('Linha: ' + str(self.numlines) + ' - ' + str(words.total(line)) + ' palavras - ' + str(tags.total(line)) + ' tags (' + tags.display(line) + ') - ' + str(tags.erros(line)) + ' tags problema\n')
�� � � � � �line = self.fin.readline()
�� � � �self.fin.close()
�� � � �self.fout.close()

class Palavras:
�� �def total(self, frase):
�� � � �numwords = 0
�� � � �inword = 0
�� � � �i = 0
�� � � �while i < len(frase):
�� � � � � �if not frase[i].isspace():
�� � � � � � � �if not inword:
�� � � � � � � � � �inword = 1
�� � � � � � � � � �numwords = numwords + 1
�� � � � � �else:
�� � � � � � � �if inword:
�� � � � � � � � � �inword = 0
�� � � � � �i = i + 1
�� � � �return numwords

class Tags:
�� �def total(self, frase):
�� � � �numtags = 0
�� � � �intag = 0
�� � � �i = 0
�� � � �while i < len(frase):
�� � � � � �if frase[i] == '<':
�� � � � � � � �if not intag:
�� � � � � � � � � �intag = 1
�� � � � � �elif frase[i] == '>':
�� � � � � � � �if intag:
�� � � � � � � � � �intag = 0
�� � � � � � � � � �numtags = numtags + 1
�� � � � � �i = i + 1
�� � � �return numtags

�� �def erros(self, frase):
�� � � �numerros = 0
�� � � �intag = 0
�� � � �i = 0
�� � � �while i < len(frase):
�� � � � � �if frase[i] == '<':
�� � � � � � � �if intag:
�� � � � � � � � � �numerros = numerros + 1
�� � � � � � � �intag = 1
�� � � � � �elif frase[i] == '>':
�� � � � � � � �if not intag:
�� � � � � � � � � �numerros = numerros + 1
�� � � � � � � �intag = 0
�� � � � � �i = i + 1
�� � � �if intag:
�� � � � � �numerros = numerros + 1
�� � � �return numerros

�� �def display(self, frase):
�� � � �intag = 0
�� � � �i = 0
�� � � �str = ''
�� � � �aux = ''
�� � � �while i < len(frase):
�� � � � � �if frase[i] == '<':
�� � � � � � � �if intag:
�� � � � � � � � � �aux = ''
�� � � � � � � �intag = 1
�� � � � � �elif frase[i] == '>':
�� � � � � � � �if intag:
�� � � � � � � � � �str += aux + '>'
�� � � � � � � � � �aux = ''
�� � � � � � � �intag = 0

�� � � � � �if intag:
�� � � � � � � �aux += frase[i]

�� � � � � �i = i + 1
�� � � �return str;




