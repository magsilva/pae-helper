Lista  de exerc�cios de POO
Prof. Renata Pontin M. Fortes
Aluno: Jo�o Paulo Scardua Coelho 3560630
jpcoelho@grad.icmc.usp.br

# ERRO TOTAL 1 4
# ERRO TOTAL 1 5
1) 	a) Construtor � um m�todo de uma classe que cria um objeto (aloca o objeto num espa�o de mem�ria) para que ele possa ser utilizado e manipulado. 
	Destrutor � um m�todo que apaga da mem�ria um objeto previamente alocado quando este n�o � mais necess�rio. Em Python o m�todo destrutor n�o precisa estar expl�cito na declara��o da classe. Python emprega automaticamente este m�todo quando o objeto n�o est� mais sendo referenciado. Toda inst�ncia em Python possui um contador de refer�ncias. Quando este contador se torna zero a inst�ncia � destruida (garbage collected).
	Para ambos os m�todos, assim para outros m�todos especiais, deve-se, em Python, utilizar nas suas defini��es em duplo underscore (__) antes e depois de seu nome.
# ERRO TOTAL 1 6

b) Formas de acessoutilizadas na defini��o de classes:
Privado: os atributos e m�todos definidos desta maneira somente podem ser acessados pela pr�pria classe.
P�blico: qualquer inst�ncia (objeto) da classe pode acessar os m�todos e atributos p�blicos.
Protegido.

c) Os cinco conceitos suportados por LPOO s�o
1. Classes e Objetos
2. Troca de Mensagens
3. Heran�a
4. Encapsulamento
5. Sobrecarga e Polimorfismo

d) 	Objeto � uma representa��o de uma entidade do mundo real, possui caracter�sticas e comportamento conhecidos. � uma inst�ncia de uma classe.
	Classe � uma especifica��o (Tipo abstrato de dado � TAD mais suas opera��es) ue define as vari�veis e fun��es comuns a todos os objetos de um certo tipo.
	M�todos de uma classe definem as opera��es que s�o poss�veis de se realizar com o objeto caracterizado por aquela classe.

e) O paradigma das LPOO s�o de mais f�cil abstra��o pelo desenvolvedor. O gap sem�ntico � diminuido.A modulariza��o, o encapsulamento e ocultamneto das informa��es, facilitam muito a reuzabilidade e a manutenibilidade do c�digo.









2) Defini��o da classe palavras com o m�todo para contar caracteres e a ocrr�ncia de um determinado caracter.


class palavras:

    def __init__(self):
        self.pal = ""

    def conta_char(self, x):
        self.pal = str(x)
        num_char = 0
        for i in self.pal:
            num_char +=1
        return num_char

    def conta_o_char(self, x, y):
        self.pal = str(x)
        caracter = str(y)
        num_do_char = 0
        for i in self.pal:
            if (i == caracter):
                num_do_char +=1
        return num_do_char

3) Utilizando a classe definida no exerc�cio enterior receber um texto do teclado e contar o n�mero de palavras com 1 caracter, com 2 caracteres, com 3 e assim por diante.

# ERRO TOTAL 3 3

pal = palavras()
texto = raw_input()
a = texto.split()  #a eh uma lista com todas as palavras digitadas
lista = []
for i in a:
    tam = pal.conta_char(i)
    lista.append(tam)  #lista eh uma lista com o tamanho de cada palavra
for j in lista:
    num = lista.count(j) #num eh o numero de palavras do tamanho j
    if num > 1:
        k = 1
        print "Palavras com " + str(j) + " caracteres = " + str(num) 
        while k < num:
            lista.remove(j)
            k +=1
    elif num == 1:
        print "Palavras com " + str(j) + " caracteres = " + str(num) 
    


4) Programa que gera frases com o uso de um gerador de n�meros rand�micos. � definido uma classe frases.

from random import choice
from string import capitalize
class frases:
    def __init__(self,a=(),b=(),c=(),d=()):
        self.artigo = a
        self.substantivo = b
        self.verbo = c
        self.preposicao = d
    def monta_sentenca(self):
        sentenca = ""
        for i in range(0,20):
            a = choice(self.artigo)
            b = choice(self.substantivo)
            c = choice(self.verbo)
            d = choice(self.preposicao)
            e = choice(self.artigo)
            f = choice(self.substantivo)
            sentenca = a + " " + b + " " + c + " " + d + " " + e + " " + f + "."
            sentenca = sentenca.capitalize()
            print sentenca
            sentenca = []

# ERRO TOTAL 4 8

#instanciacoes
artigo = ("a","o","um","uma")
substantivo = ("pao","comida","aula","carro","cidade","sol","cachorro","porco")
verbo = ("comeu","caiu","correu","falou","pulou")
preposicao = ("de","sobre","sob","embaixo","em")
teste = frases(artigo,substantivo,verbo,preposicao)
teste.monta_sentenca()
