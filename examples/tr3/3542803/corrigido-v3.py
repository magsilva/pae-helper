Programa  o Orientada a Objetos
Bacharelado em Ci ncias de Computa  o
Professora Renata Pontin de Mattos Fortes

S o Carlos, 8 de Abril de 2003.
Anderson Sumitomo Otuka	3542803

Lista de Exerc�cios

1.	Objeto � a instancia��o de uma classe. Uma classe � a abstra��o de algo do mundo real, constitu�do por TADs b�sicos que descrevem os atributos da classe e m�todos que s�o fun��es que podem ser invocadas externamente ou atrav�s de outros objetos.

# ERRO TOTAL 1 5
O construtor de objetos � o que inicializa um objeto: a partir de uma classe, um novo objeto � instanciado. Em Python, o m�todo construtor de objetos � o __init__. O destrutor de objetos os elminina e libera a mem�ria utilizada por estes, quando n�o h� mais refer�ncias aos mesmos. Em Python, quando n�o existem mais refer�ncias a um objeto, este � automaticamente eliminado, ou garbage-collected. 

Os 5 principais conceitos do paradigma de Orienta��o a Objetos s�o:
1.Objetos e Classes (descritos anteriormente);
2.Comunica��o com Mensagens: objetos comunicam-se atrav�s de mensagens enviadas a m�todos;
3.Heran�a: capacidade de se criar classes contendo outras classes, onde a subclasse criada herda os m�todos e propriedades da classe superior;
4.Encapsulamento: os m�todos e atributos s�o pr�prios de cada m�todo;
5.Sobrecarga e Polimorfismo.

A principal vantagem da utiliza��o de Linguagens Orientadas Objetos em rela��o a Linguagens Procedimentais � que a primeira aproxima-se mais das abstra��es que temos do mundo real, que � constitu�do de entidades, propriedades e a��es. O prop�sito das L.O.O. � reduzir o gap sem�ntico existente entre o Dom�nio de Problemas (Mundo Real) e o Dom�nio de Solu��es (Abstra��es).


2.	class Palavras:
    def __init__ (self, Entrada):
        self.ListPal = Entrada.split(" ")
    def Conta_palavras (self):
        return len(self.ListPal)    
    def Conta_char (self, NumPalavra):
        return len(self.ListPal[NumPalavra])
    def Conta_o_char (self, Char, NumPalavra):
        return self.ListPal[NumPalavra].count(Char)

Exemplo:
>>> x = Palavras("Aqui temos quatro palavras!")
>>> x.Conta_char(0)
4
>>> x.Conta_char(1)
5
>>> x.Conta_char(2)
6
>>> x.Conta_char(3)
9
>>> x.Conta_o_char("a", 3)
3


3.	class ProcessaTexto:
    def __init__ (self):
        print 'Entre com o texto. (use ".<ENTER>" em uma linha vazia para finalizar)'
        self.Buf = ""
        self.Entr = ""
        while self.Entr != ".":
            self.Buf += self.Entr + " "
            self.Entr = raw_input('>> ')
        self.Texto = Palavras(self.Buf)
        del self.Buf
        del self.Entr

        self.MinChar = 0
        self.NovoMinChar = 0
        self.TotPalavras = self.Texto.Conta_palavras()

        while (self.NovoMinChar != 9999):
            self.Ocorrencias = 0
            self.PalavraAtual = 0
            self.NovoMinChar = 9999
            for self.PalavraAtual in range(0, self.TotPalavras):
                if (self.Texto.Conta_char(self.PalavraAtual) == self.NovoMinChar):
                    self.Ocorrencias += 1
                elif ((self.Texto.Conta_char(self.PalavraAtual) < self.NovoMinChar) and
                      (self.Texto.Conta_char(self.PalavraAtual) > self.MinChar)):
                    self.NovoMinChar = self.Texto.Conta_char(self.PalavraAtual)
                    self.Ocorrencias = 1
            self.MinChar = self.NovoMinChar
            if (self.MinChar != 9999):
                print 'Total de palavras com %d caracteres: %d' % (self.MinChar, self.Ocorrencias)

        del self.MinChar
        del self.NovoMinChar
        del self.TotPalavras
        del self.Ocorrencias
        del self.PalavraAtual


# ERRO PARCIAL 3 5

Exemplo:
>>> ProcessaTexto()
Entre com o texto. (use ".<ENTER>" em uma linha vazia para finalizar)
>> Esse eh um texto
>> de teste para ver
>> se tudo estah funcionando
>> da maneira como
>> tem que ser
>> .
Total de palavras com 2 caracteres: 5
Total de palavras com 3 caracteres: 4
Total de palavras com 4 caracteres: 4
Total de palavras com 5 caracteres: 3
Total de palavras com 7 caracteres: 1
Total de palavras com 11 caracteres: 1
<__main__.ProcessaTexto instance at 0x01832E08>


4.	import random

class Sentenca:
    def __init__ (self, tupla_artigo, tupla_subst, tupla_verbo, tupla_prep):
        self.tx = ""
        for self.i in range(0, 6):
            if (self.i == 0) or (self.i == 4):
                self.tx += tupla_artigo[int(random.random() * len(tupla_artigo))] + " "
            if (self.i == 1) or (self.i == 5):
                self.tx += tupla_subst[int(random.random() * len(tupla_subst))] + " "
            if (self.i == 2):
                self.tx += tupla_verbo[int(random.random() * len(tupla_verbo))] + " "
            if (self.i == 3):
                self.tx += tupla_prep[int(random.random() * len(tupla_prep))] + " "
        self.tx = self.tx.capitalize()
        self.tx = self.tx.strip() + "."

    def __str__ (self):
        return self.tx

Exemplos:
>>> art = ["o", "a", "um", "uma"]
>>> sub = ["gata", "cao", "cidade", "barro", "bicicleta"]
>>> ver = ["andou", "correu", "pulou", "caiu"]
>>> pre = ["de", "sobre", "sob", "embaixo"]
>>> x = Sentenca(art, sub, ver, pre)
>>> print x
Uma barro correu de o bicicleta.
>>> x = Sentenca(art, sub, ver, pre)
>>> print x
O bicicleta andou de o gata.
>>> x = Sentenca(art, sub, ver, pre)
>>> print x
Um gata pulou sob a cidade.
>>> x = Sentenca(art, sub, ver, pre)
>>> print x
O cao correu embaixo um cao.
>>> x = Sentenca(art, sub, ver, pre)
>>> print x
O barro correu sob a cao.
>>> x = Sentenca(art, sub, ver, pre)
>>> print x
Um cidade correu de o cidade.
>>> x = Sentenca(art, sub, ver, pre)
>>> print x
A cao caiu sob uma bicicleta.
>>> x = Sentenca(art, sub, ver, pre)
>>> print x
O bicicleta correu sobre um cidade.

# ERRO TOTAL 4 8

5.	import math

class quadrilatero:
    # O quadrilatero formado eh sempre da forma P1, P2, P3, P4, P1.
    def __init__(self, x1, y1, x2, y2, x3, y3, x4, y4):
        self.x1 = float(x1)
        self.x2 = float(x2)
        self.x3 = float(x3)
        self.x4 = float(x4)
        self.y1 = float(y1)
        self.y2 = float(y2)
        self.y3 = float(y3)
        self.y4 = float(y4)
    def __str__(self):
        return "(" + str(self.x1) + "," + str(self.y1) + ")," + "(" + str(self.x2) + "," + str(self.y2) + ")," + "(" + str(self.x3) + "," + str(self.y3) + ")," + "(" + str(self.x4) + "," + str(self.y4) + ")"

class trapezio(quadrilatero):
    # P2-P3 eh sempre paralelo a P1-P4
    # d23 = dist P2-P3
    # (x23, y23) = vetor unitario na direcao P2-P3
    # x23 = (x2-x3) / d23
    # y23 = (y2-y3) / d23
    # P4 = P1 + d14 * (x23, y23)
    def __init__ (self, x1, y1, x2, y2, x3, y3, d14):
        self.d23 = math.sqrt(float((x3-x2)*(x3-x2)+(y3-y2)*(y3-y2)))
        self.x23 = (x3-x2) / self.d23
        self.y23 = (y3-y2) / self.d23
        self.x4 = x1 + d14 * self.x23
        self.y4 = y1 + d14 * self.y23
        quadrilatero.__init__(self, x1, y1, x2, y2, x3, y3, self.x4, self.y4)
        del self.d23
        del self.x23
        del self.y23

class paralelograma(trapezio):
    # x3-x2 = x4-x1 ==> x4 = x3-x2+x1
    # y3-y2 = y4-y1 ==> y4 = y3-y2+y1
    def __init__ (self, x1, y1, x2, y2, x3, y3):
        self.x4 = x3-x2+x1
        self.y4 = y3-y2+y1
        self.d14 = math.sqrt( ((self.x4-x1)*(self.x4-x1)) + ((self.y4-y1)*(self.y4-y1)) )
        trapezio.__init__(self, x1, y1, x2, y2, x3, y3, self.d14)
        del self.d14

class retangulo(paralelograma):
    # O retangulo eh construido no sentido horario, P1-P2-P3-P4-P1
    # (x12, y12) = vetor V unitario na direcao P1-P2
    # (x23, y23) = V rotacionado 90 graus = (y12, -x12)
    def __init__ (self, x1, y1, x2, y2, d23):
        self.d12 = math.sqrt( ((x2-x1)*(x2-x1)) + ((y2-y1)*(y2-y1)) )
        self.x12 = (x2-x1) / self.d12
        self.y12 = (y2-y1) / self.d12
        self.x23 = d23 * self.y12
        self.y23 = - d23 * self.x12
        x3 = x2 + self.x23
        y3 = y2 + self.y23
        del self.d12
        del self.x12
        del self.y12
        del self.x23
        del self.y23
        paralelograma.__init__(self, x1, y1, x2, y2, x3, y3)
        
class quadrado(retangulo):
    # O quadrado eh construido no sentido horario, P1-P2-P3-P4-P1
    def __init__ (self, x1, y1, x2, y2):
        self.d31 = math.sqrt( ((x2-x1)*(x2-x1)) + ((y2-y1)*(y2-y1)) )
        retangulo.__init__(self, x1, y1, x2, y2, self.d31)
        del self.d31

Exemplos:
>>> quad1 = quadrilatero(1, 2, 2, 3, 1, 3, 0, 1)
>>> quad2 = trapezio(0, 0, 1, 1, 2, 1, 3)
>>> quad3 = paralelograma(0, 0, 7, 3, 8, 4)
>>> quad4 = retangulo(0, 0, 2, 2, 6 * math.sqrt(2))
>>> quad5 = quadrado(7, 7, 9, 9)
>>> print quad1
(1.0,2.0),(2.0,3.0),(1.0,3.0),(0.0,1.0)
>>> print quad2
(0.0,0.0),(1.0,1.0),(2.0,1.0),(3.0,0.0)
>>> print quad3
(0.0,0.0),(7.0,3.0),(8.0,4.0),(1.0,1.0)
>>> print quad4
(0.0,0.0),(2.0,2.0),(8.0,-4.0),(6.0,-6.0)
>>> print quad5
(7.0,7.0),(9.0,9.0),(11.0,7.0),(9.0,5.0)
>>> quad4 = retangulo(0, 0, 2, 2, 6 * sqrt(2))
>>> quad1.__dict__
{'y1': 2.0, 'y2': 3.0, 'x2': 2.0, 'x3': 1.0, 'y3': 3.0, 'x1': 1.0, 'y4': 1.0, 'x4': 0.0}
>>> quad2.__dict__
{'y4': 0.0, 'x2': 1.0, 'x4': 3.0, 'y1': 0.0, 'x3': 2.0, 'y3': 1.0, 'y2': 1.0, 'x1': 0.0}
>>> quad3.__dict__
{'y2': 3.0, 'x2': 7.0, 'x4': 1.0, 'y1': 0.0, 'x3': 8.0, 'y3': 4.0, 'x1': 0.0, 'y4': 1.0}
>>> quad4.__dict__
{'y2': 2.0, 'x2': 2.0, 'x4': 6.0, 'y1': 0.0, 'x3': 8.0, 'y3': -4.0, 'x1': 0.0, 'y4': -6.0}
>>> quad5.__dict__
{'y2': 9.0, 'y1': 7.0, 'x4': 9.0, 'x2': 9.0, 'x3': 11.0, 'y3': 7.0, 'x1': 7.0, 'y4': 5.0}
