Questão 1

a)O método __init__ é o construtor da classe, isto é, a função que é chamada
quando um objeto é instanciado.
Ex: def __init__(self, argumentos)
 O destrutor é o método __del__ que libera o espaço de memória ocupado
pelo objeto quando este não é mais usado. 
# ERRO TOTAL 1 5
# ERRO TOTAL 1 7
# ERRO TOTAL 1 8
b) Temos:
	c.__dict__
	c.__doc__
	c.__name__

c)1- classes e objetos
  2- sobrecarga e polimorfismo
  3- encapsulamento
  4- herança
  5- comunicação por mensagens

d) classe: É como se fosse o tipo do objeto que é instanciado. É constituida
por atributos e métodos que manipulam os objetos pertencentes a classe.
   objetos:é uma comunidade de agentes que interagem entre si. Pertencem 
a uma certa classe.
   métodos: são funções definidas dentro de uma classe que manipulam 
objetos pertencentes a esta classe.

e)Vantagens: 
 1- maior reusabilidade
 2- maior modularidade
 3- maior manteinabilidade
 4- mais próximo da resolução de problemas do mundo real (diminuição do
 gap semântico)

class palavra:
	lista = []
	def __init__(self, *palavras):
		for x in palavras:
			self.lista.append(x)
	def conta_char(self):
		for x in self.lista:
			print x
			print len(x)
	def conta_o_char(self, x):
                cont = 0
		for w in self.lista:
			for y in w:
				if y == x:
                                    cont += 1
                        print w
                        print cont
                        cont = 0

# ERRO TOTAL 3 3
                        
class palavra:
	def __init__(self, palavra):
                self.palavra = palavra		
	def conta_char(self):
		return (len(self.palavra))
	def conta_o_char(self, x):
                cont = 0
		for y in self.palavra:
		    if y == x:
                        cont += 1
                print self.palavra 
                print cont
                cont = 0
def lista33():
    lista2 = []
    lista = []
    cont = 0
    quant = 0
    i = 1
    result = ""
    s = raw_input("Digite o texto:  ")
    s += " "
    for x in s:
        if x != " ":
            result += str(x)
        else:
	    lista.append(result)
	    result = ""
    for i in range(1,20):
            for y in lista:
                c = palavra(y)
                if c.conta_char() == i:
                    quant += 1
                if (c.conta_char() == i) & (y not in lista2):
                    if cont == 0:
                        if i == 1:
                            print "Palavra(s) com %d letra: " %i
                            cont = cont + 1
                        else:
                            print "Palavra(s) com %d letras: "%i
                    print c.palavra
                    cont = cont + 1
                    lista2.append(y)
            if quant != 0:
                print "Total = %d" %quant
	    cont = 0
	    quant = 0

# ERRO PARCIAL 3 5

def lista34():
     import random
     import string
     
     tupla1 = ("o", "a","um","uma")
     tupla2 = ("gata", "cao", "cidade", "carro", "bicicleta")
     tupla3 = ("andou", "correu", "pulou","caiu")
     tupla4 = ("de", "sobre", "sob", "embaixo")
    
     n1 = len(tupla1)
     n2 = len(tupla2)
     n3 = len(tupla3)
     n4 = len(tupla4)
     result = ""

     for x in range(1,21):
        g = Random()
        num1 = g.randrange(1,n1)
        nome = string.capitalize(tupla1[num1])
        result += str(nome) + " "
        num2 = g.randrange(1,n2)
        result += str(tupla2[num2]) + " "
        num3 = g.randrange(1,n3)
        result += str(tupla3[num3]) + " "
        num4 = g.randrange(1,n4)
        result += str(tupla4[num4]) + " "
        num5 = g.randrange(1,n1)
        result += str(tupla1[num1]) + " "              
        num6 = g.randrange(1,n2)
        result += str(tupla2[num2]) + "." 

        print result
       
        result = ""
        
        
# ERRO TOTAL 4 8

            
    

       
            
