Sergio Pavanello Rossi nº 3530035

LISTA DE EXERCICIOS  DE POO

# ERRO TOTAL 1 4
# ERRO TOTAL 1 5
1 -  i) Um construtor de objetos é usado para instanciar o objeto 
dentro de um programa . O objeto então precisa ser criado para que 
possa ser utilizado.O destrutor destroi a objeto instanciado, assim 
ele não pode ser mais utilizado.
	A criação de um objeto em Python pode ser feito o metodo 
__init__.e sua destruição pelo comando del(objeto) .
# ERRO TOTAL 1 7

ii) Não entendi a pergunta ! ...
# ERRO TOTAL 1 8

iii) Os conceitos são :
- objetos e classes
- comunicacão com mensagens
- herança
- encapsulamento
- sobrecarga e polimorfismo

# ERRO PARCIAL 1 1
iv) classes : conjuntos de atributos especificos com definicoes de 
metodos que podem ser aplicados a esses metodos .

# ERRO PARCIAL 1 2
    objeto : uma abstração de algo do mundo real para o mundo 
computacional. 

# ERRO TOTAL 1 3

# ERRO PARCIAL 1 10
v)A POO  aumenta a produividade do programadorm, facilita a manutenção
e controla a complexidade do software.


2 - class palavra:
    def __init__(self,palav):
        self.palavra = palav
    
    def conta_char(self):
        i = len(self.palavra)
        return i
        
    def conta_o_char(self,char):
        return self.palavra.count(char)        
               
      
3 - class tabela:
    
    def __init__(self):
	n1 = 0
	n2 = 0
	n3 = 0
	n4 = 0
	nmais = 0
	print 'Entre com texto (linha e branco para terminar) :\n '
	i = raw_input()
	while i != '':
	    lista = i.split(' ')
	    for pal in lista:
	        p = palavra(pal)
	        num = p.conta_char()
		if num == 1 :
		    n1 += 1
	        elif num == 2 :
		    n2 += 1
	        elif num == 3 :
		    n3 += 1 
		elif num == 4 :
		    n4 += 1
		elif num >= 5:
		    nmais +=1
	i = raw_input()	    
	print '\d Palavras com uma letra : %d'%n1
	print '\d Palavras com duas letras : %d'%n2
	print '\d Palavras com tres letras : %d'%n3
	print '\d Palavras com quatro letras : %d'%n4
	print '\d Palavras com cinco ou mais letras : %d'%nmais
	    
# ERRO PARCIAL 3 5

4 - class sentencas:

    def __init__(self):
        self.artigo = ['o','a','um','uma']
        self.subs = ['animal','motocicleta','gata','cao','cidade','carro','bicicleta']
        self.verbo = ['subiu','andou','correu','pulou','caiu']
        self.prep = ['de','sobre','sob','embaixo']
        self.cria()

    def cria(self)  :
        import random
        i = 0
        while i < 20 :
            self.frase = ''
            x1 = random.choice(self.artigo)
            y = x1.capitalize()                 
            self.frase += (y) + ' '        
            x2 = random.choice(self.subs)
            self.frase += (x2) + ' '
            x3 = random.choice(self.verbo)
            self.frase += (x3) + ' '
            x4 = random.choice(self.prep)
            self.frase += (x4) + ' '
            x5 = random.choice(self.artigo)
            self.frase += (x5) + ' '
            x6 = random.choice(self.subs)
            self.frase += (x6) + ' '
            self.frase += '.'
            print self.frase        
            i += 1    
            
# ERRO TOTAL 4 8


