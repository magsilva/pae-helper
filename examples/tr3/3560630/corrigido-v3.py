Lista  de exercícios de POO
Prof. Renata Pontin M. Fortes
Aluno: João Paulo Scardua Coelho 3560630
jpcoelho@grad.icmc.usp.br

# ERRO TOTAL 1 4
# ERRO TOTAL 1 5
1) 	a) Construtor é um método de uma classe que cria um objeto (aloca o objeto num espaço de memória) para que ele possa ser utilizado e manipulado. 
	Destrutor é um método que apaga da memória um objeto previamente alocado quando este não é mais necessário. Em Python o método destrutor não precisa estar explícito na declaração da classe. Python emprega automaticamente este método quando o objeto não está mais sendo referenciado. Toda instância em Python possui um contador de referências. Quando este contador se torna zero a instância é destruida (garbage collected).
	Para ambos os métodos, assim para outros métodos especiais, deve-se, em Python, utilizar nas suas definições em duplo underscore (__) antes e depois de seu nome.
# ERRO TOTAL 1 6

b) Formas de acessoutilizadas na definição de classes:
Privado: os atributos e métodos definidos desta maneira somente podem ser acessados pela própria classe.
Público: qualquer instância (objeto) da classe pode acessar os métodos e atributos públicos.
Protegido.

c) Os cinco conceitos suportados por LPOO são
1. Classes e Objetos
2. Troca de Mensagens
3. Herança
4. Encapsulamento
5. Sobrecarga e Polimorfismo

d) 	Objeto é uma representação de uma entidade do mundo real, possui características e comportamento conhecidos. É uma instância de uma classe.
	Classe é uma especificação (Tipo abstrato de dado – TAD mais suas operações) ue define as variáveis e funções comuns a todos os objetos de um certo tipo.
	Métodos de uma classe definem as operações que são possíveis de se realizar com o objeto caracterizado por aquela classe.

e) O paradigma das LPOO são de mais fácil abstração pelo desenvolvedor. O gap semântico é diminuido.A modularização, o encapsulamento e ocultamneto das informações, facilitam muito a reuzabilidade e a manutenibilidade do código.









2) Definição da classe palavras com o método para contar caracteres e a ocrrência de um determinado caracter.


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

3) Utilizando a classe definida no exercício enterior receber um texto do teclado e contar o número de palavras com 1 caracter, com 2 caracteres, com 3 e assim por diante.

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
    


4) Programa que gera frases com o uso de um gerador de números randômicos. É definido uma classe frases.

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
