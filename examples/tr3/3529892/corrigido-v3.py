Lucas Shindi Shimo 3529892 lshimo@grad.icmc.usp.br
Programa��o Orientada � Objeto - Prof. Renata Pontin
Lista de Exerc�cio

1.
# ERRO TOTAL 1 4
# ERRO TOTAL 1 5

a)	Construtor � o papel que a fun��o de cria��o desempenha para instanciar novos objetos. Destrutor � fun��o para apagar da mem�ria esse objeto instanciado.

# ERRO PARCIAL 1 6
	Regras para o contrutor s�o:
	- nome do objeto n�o pode iniciar com numero ou simbolos
	- deve iniciar com letrar ou '_'
	- n�o deve conter caracteres n�o alfa-num�ricos
	- n�o deve conter espa�os
	Destrutor usa o mecanismo garbage-colector
# ERRO TOTAL 1 7
b)	Define-se uma classe por um nome, atributos e m�todos.
# ERRO TOTAL 1 8
c)	Tipagem de dados, objetos, mensagens, representa��o e abstra��o
d)	Classe - Mecanismo para criar estrutura de dados e novos tipos de objetos, define m�todos e um conjunto de atributos que s�o associados a uma cole��o de objetos.
	Objeto - Instancia de uma classe, possui identidade, tipo e valor, m�todos e atributos.
	M�todo - � um fun��o que realiza alguma opera��o sobre um objeto quando o m�todo � chamado.

e)	Evitar o gap se
# ERRO TOTAL 1 10
-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


#EXERCICIO 2
class Palavra:
    def __init__ (self,pal):
        self.palavra=pal
    def conta_char(self):
        return len(self.palavra)
    def conta_o_char(self,car):
        return self.palavra.count(car)
#-------------fim exercicio 2---------


#EXERCICIO 3
class npal:
    def __init__ (self):
        self.frase= raw_input("Entre com a frase: ")
    def conta(self):
        self.nletra=[]
        aux=self.frase
        pos=aux.find(" ")
        while( pos > 0 ):
            bla=Palavra(aux[:pos])
            self.nletra.append( bla.conta_char() )
            aux=aux[pos+1:]
            pos=aux.find(" ")
        bla=Palavra(aux)
        self.nletra.append( bla.conta_char() )
        for aux in self.nletra:
            count=self.nletra.count(aux)
            if(count > 1):
                i=1
                while(i< count):
                    self.nletra.remove(aux)
                    i += 1
            print "%d palavras de %d-letras"%(count,aux)
#------------------fim exercicio 3-------------------------


#EXERCICIO 4
def gerar():
    artigo=("o","a","um" ,"uma")
    subs=("gata","cao","cidade","carro","bicicleta")
    verbo=("andou","correu","pulou","caiu")
    prepo=("de","sobre","sob","embaixo")
    palavra=""

    from random import choice
    i=0
    while(i<20):
        palavra = palavra + choice(artigo)
        palavra = palavra + " " + choice(subs)
        palavra = palavra + " " + choice(verbo)
        palavra = palavra + " " + choice(prepo)
        palavra = palavra + " " + choice(artigo)
        palavra = palavra + " " + choice(subs) + "."
        i+=1
        aux = palavra[:1]
        aux = aux.upper()
        palavra= aux+palavra[1:]
        print palavra
        palavra=""

# ERRO TOTAL 4 8
# ERRO PARCIAL 4 6
