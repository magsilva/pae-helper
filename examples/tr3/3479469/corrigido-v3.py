ICMC-USP
Lista de Exerc�cios - Resolu��o

Daniel C�rnio Junqueira - 3479469

1.a)
# ERRO TOTAL 1 5
# ERRO TOTAL 1 7
# ERRO TOTAL 1 6
"Construtor" � um m�todo especial executado quando �
criado um novo objeto (ou seja, quando uma classe
� instanciada). "Destrutor" � o m�todo que consiste na
destrui��o de uma inst�ncia.

1.b)
# ERRO TOTAL 1 8
Uma classe pode ser chamada com passagem de par�metros, quando seu construtor permite ou exige que se passem par�metros ao instanciar os objetos, ou sem a passagem de par�metros.

1.c)
Os cinco principais conceitos que se consolidaram no paradigma de "Orienta��o a Objetos" e que est�o dispon�veis na maioria das LPOO s�o: objetos e classes, mensagens para comunica��o, heran�a, encapsulamento, sobrecarga e polimorfismo.

1.d)
Uma classe � a estrutura b�sica que cont�m m�todos e atributos espec�ficos, que devem ser incorporados �s inst�ncias dessa classe - os objetos. Os m�todos s�o fun��es que os objetos dessa classe ter�o, ou seja, opera��es que poder�o ser feitas com estes objetos.

1.e)
As linguagens de programa��o orientada a objetos possuem a vantagem
de se poder fazer uma modelagem quase real do problema, criando-se
classes, objetos, que por suas vezes possuem m�todos e atributos,
como se fossem objetos reais.

2.
# ERRO PARCIAL 2 1
class Palavras:
    def __init__ (self palavra):
        self.conteudo = palavra

    def Conta_char (self):
        return len(self.conteudo)

    def Conta_o_char (self, caracter):
        num = 0
        for i in range(0, len(self.conteudo)):
            if self.conteudo[i] == caracter:
                num += 1
        return num

3.

# ERRO TOTAL 3 3

class Palavras:
    def __init__ (self, palavra):
        self.conteudo = palavra

    def Conta_char (self):
        return len(self.conteudo)

    def Conta_o_char (self, caracter):
        num = 0
        for i in range(0, len(self.conteudo)):
            if self.conteudo[i] == caracter:
                num += 1
        return num

linha = ""
nro_caracteres = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
array_palavras = []
i = 1
while linha != "\n":  #linha em branco para finalizar
    linha = raw_input("Digite a linha %d: " % i)
    palavras = linha.split(" ")
    for palavra in palavras:
        array_palavras.append(Palavras(palavra))
        nro_caracteres[array_palavras[i-1].Conta_char() - 1] += 1

for i in range(0,20):
    print "Palavras com %d letras: %d" % i+1, nro_caracteres[i]

# ERRO PARCIAL 3 5

4.
from random import random

artigo = ("o", "a", "um", "uma")
substantivo = ("gata", "cao", "cidade", "carro", "bicicleta")
verbo = ("andou", "correu", "pulou", "caiu")
preposicao = ("de", "sobre", "sob", "embaixo")

sentencas = []

for i in range(0,20):
    num = int(random() * 100) % 4
    sentencas.append(artigo[num].capitalize())
    sentencas[i] += " "
    num = int(random() * 100) % 5
    sentencas[i] += substantivo[num]
    sentencas[i] += " "
    num = int(random() * 100) % 4
    sentencas[i] += verbo[num]
    sentencas[i] += " "
    num = int(random() * 100) % 4
    sentencas[i] += preposicao[num]
    sentencas[i] += " "
    num = int(random() * 100) % 4
    sentencas[i] += artigo[num]
    sentencas[i] += " "
    num = int(random() * 100) % 5
    sentencas[i] += substantivo[num]
    sentencas[i] += "."

print sentencas
