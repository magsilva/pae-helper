Lucas Shindi Shimo 3529892 lshimo@grad.icmc.usp.br
Programação Orientada à Objeto - Prof. Renata Pontin
Lista de Exercício

1.
# ERRO TOTAL 1 4
# ERRO TOTAL 1 5

a)	Construtor é o papel que a função de criação desempenha para instanciar novos objetos. Destrutor é função para apagar da memória esse objeto instanciado.

# ERRO PARCIAL 1 6
	Regras para o contrutor são:
	- nome do objeto não pode iniciar com numero ou simbolos
	- deve iniciar com letrar ou '_'
	- não deve conter caracteres não alfa-numéricos
	- não deve conter espaços
	Destrutor usa o mecanismo garbage-colector
# ERRO TOTAL 1 7
b)	Define-se uma classe por um nome, atributos e métodos.
# ERRO TOTAL 1 8
c)	Tipagem de dados, objetos, mensagens, representação e abstração
d)	Classe - Mecanismo para criar estrutura de dados e novos tipos de objetos, define métodos e um conjunto de atributos que são associados a uma coleção de objetos.
	Objeto - Instancia de uma classe, possui identidade, tipo e valor, métodos e atributos.
	Método - É um função que realiza alguma operação sobre um objeto quando o método é chamado.

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
