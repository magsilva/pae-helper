3-a Lista de Exerc�cios Pr�ticos de POO
=======================================

Alunos:
Stanislaw Y. Pusep, #3309142
Diego Augusto Negrelli Gomes, #3309055


1)
# ERRO TOTAL 1 4
# ERRO TOTAL 1 5
  * Construtor � m�todo especial utilizado para instanciar objetos novos.
    Destrutor remove os objetos da mem�ria operacional. Para criar um
    construtor em Python deve-se definir o m�todo '__init__' na classe
    desejada com par�metro 'self':

	class Teste:
	def __init__(self):
		pass
# ERRO TOTAL 1 7
    O destrutor empregado em Python � autom�tico; quando n�o h�
    refer�ncias para um dado objeto ele � removido pelo pr�prio
    Python.

  * Utilizam-se m�todos especializados para ler e escrever vari�veis
    da classe e ocasionalmente m�todos interntos ao Python como
    __getattr__ e __setattr__

# ERRO TOTAL 1 8

  * Polimorfismo, Heran�a, Encapsulamento, Sobrecarga, Instancia��o

# ERRO PARCIAL 1 9

# ERRO TOTAL 1 1
  * Classe � uma forma de instanciar estruturas de dados.
    Objetos s�o inst�ncias de uma classe.
    M�todos de uma classe servem para ler e escrever atributos de objetos
    e classes.
  * A vantagem principal � redu��o do "gap sem�ntico". Outra vantagem
    � que em v�rios problemas a t�cnica de abstrair objetos aumenta a
    flexibilidade e compreensibilidade do c�digo.

2)

import string

class Palavras:
    def __init__(self, str):
        self.string = str

    def Conta_char(self):
        return len(self.string)

    def Conta_o_char(self, chr):
        return string.count(self.string, chr)

# 3)

import string

class Palavras:
    def __init__(self, str):
        self.string = str

    def Conta_char(self):
        return len(self.string)

    def Conta_o_char(self, chr):
        return string.count(self.string, chr)

conta = {}

while (1):
    linha = raw_input("entre com linha (<ENTER> sai): ")
    if linha == '':
        break
    palavras = string.split(linha)
    for palavra in palavras:
        a = Palavras(palavra)
        n = a.Conta_char()
        if not conta.has_key(n):
            conta[n] = 1
        else:
            conta[n] += 1

for i in conta.keys():
    print i, conta[i]

# ERRO TOTAL 3 3
# ERRO TOTAL 3 5

# 4)

import random

art = ('o', 'a', 'um', 'uma')
sub = ('gata', 'cao', 'cidade', 'carro', 'bicicleta')
ver = ('andou', 'correu', 'pulou', 'caiu')
prp = ('de', 'sobre', 'sob', 'embaixo')

def rnd(t):
    return random.choice(t)

for i in range(1, 20):
    print rnd(art)+' '+rnd(sub)+' '+rnd(ver)+' '+rnd(prp)+' '+rnd(art)+' '+rnd
(sub)

# ERRO TOTAL 4 6
# ERRO TOTAL 4 7
# ERRO TOTAL 4 8
