 ###########################################################
#                                                          #
# Guilherme de Almeida Cordeiro  -  3456690  -  08/04/2003 #
#                                                          #
###########################################################


[1.1]

# ERRO TOTAL 1 4
# ERRO TOTAL 1 5
   Construtor é um método que instancia um objeto da classe na qual foi
definido. Destrutor é um método que remove da memória um objeto que não
está mais sendo utilizado.
   Em Phyton, utiliza-se a seguinte sintáxe para
para definir um método construtor:

	def __init__(self,[,param1,param2,..]):
		<def1>
		<def2>

		<....>

# ERRO TOTAL 1 7
   Definir um método destrutor é desnecessário, pois toda instância tem
associado a ela um contador de referências. Quando não há mais nenhuma
referência a instância, ela é destruida.



[1.2]
# ERRO TOTAL 1 8
   Chamada de métodos que acessem e manipulem os atributos da classe.



[1.3]
# ERRO PARCIAL 1 9

1) Objetos e classes
2) Mensagens
3) Encapsulamento
4) Sobrecarga e polimorfismo



[1.4]


   Uma classe é a definição de um tipo abstrato de dados juntamente com
todos os métodos que o manipulam.
   Um objeto é a representação de uma entidade real através da instância
de uma classe.
   Métodos são rotinas que acessam, manipulam e operam sobre os atributos
(TAD) de uma classe.



[1.5]

  Linguagens orientadas a objetos facilitam a representação de problemas reais
e tornam sua abstração mais simples. Além disso, tornam o código mais modularizado,
estruturado e portável.




[2.0]

# ERRO PARCIAL 1 3 Não é para restringir os caracteres possíveis da palavra.
>>> class palavra:
    def __init__(self, *instr): # O metodo de inicializacao ignora caracteres qu nao
        self.word = ""          # sejam letras. As letras sao guardadas em minusculas.
        for x in instr[:]:
            if ((x >= 'a') and (x <= 'z')) or ((x >= 'A') and (x <= 'Z')):
                self.word += x.lower()

    def conta_char(self):
        return len(self.word)

    def conta_o_char(self, ch): # Maiusculas e minusculas sao consideradas iguais.
        contador = 0
        if ((ch >= 'a') and (ch <= 'z')) or ((ch >= 'A') and (ch <= 'Z')):
            contador = self.word.count(ch.lower())
        return contador

>>> q = palavra("qwerty")
>>> q.conta_char()
6
>>> q.conta_o_char(0)
0
>>> q.conta_o_char('q')
1
>>> q = palavra('banana')
>>> q.conta_char()
6
>>> q.conta_o_char('a')
3
>>> q.conta_o_char('A')
3


 
[3.0]

# ERRO TOTAL 3 3

>>> def conta_palavras(): # Considera palavras substrings compostas apenas de letras e limitadas
                      # por espacos em branco. Demais caracteres sao ignorados.
    lista = []     # Lista de palavras validas.
    size_list = [] # Lista de tamanhos das palavras.
    frase = raw_input()
    while (frase != ''):
        word = ''
        s = 0 # Eh setado em 1 quando uma palavra esta sendo analizada.
        tam = len(frase)
        i = 0
        while (i < tam):
            if (frase[i] == ' ') and s:
                    lista += [palavra(word)]
                    word = ''
                    s = 0
            elif ((frase[i] >= 'a') and (frase[i] <= 'z')) or ((frase[i] >= 'A') and (frase[i] <= 'Z')):
                s = 1
                word += frase[i]
            i += 1
        if s:
            lista = lista + [palavra(word)]
        frase = raw_input()
    if (lista == []):
        print "Nao houveram entradas"
    else:
        for pal in lista[:]:
            size_list += [pal.conta_char()]
        size_list.sort()
        i = size_list[0]
        c = 0
        for x in size_list[:]:
            if (x == i):
                c += 1
            else:
                print "Haviam", c, "palavras com", i, "letras;"
                i = x
                c = 1
        print "Haviam", c, "palavras com", i, "letras."

        
>>> conta_palavras()
uma frase de    pouquissimas  p a lav r as.... 

Haviam 3 palavras com 1 letras;
Haviam 2 palavras com 2 letras;
Haviam 2 palavras com 3 letras;
Haviam 1 palavras com 5 letras;
Haviam 1 palavras com 12 letras.
>>> conta_palavras()
texto
com
muitas
linhas
 e
palavras
graaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaandes!!@*&
:P

Haviam 2 palavras com 1 letras;
Haviam 1 palavras com 3 letras;
Haviam 1 palavras com 5 letras;
Haviam 2 palavras com 6 letras;
Haviam 1 palavras com 8 letras;
Haviam 1 palavras com 54 letras.
>>> conta_palavras()
...

Nao houveram entradas
>>> conta_palavras()

Nao houveram entradas





[4.0]

>>> class base:
    def __init__(self, *input):
        self.list = input

    def show_i(self, i):
        return self.list[i]

    def size(self):
        return len(self.list)

>>> art = base('o','a','um','uma')
>>> sub = base('gata','cao','cidade','carro','bicicleta')
>>> ver = base('andou','correu','pulou','caiu')
>>> pre = base('de','sobre','sob','embaixo')
>>> from random import randint
>>> def random_sentence(art, sub, ver, pre):
    i = randint(0,art.size()-1)
    w1 = art.show_i(i)
    w1.capitalize()
    i = randint(0,art.size()-1)
    w5 = art.show_i(i)
    i = randint(0,sub.size()-1)
    w2 = sub.show_i(i)
    i = randint(0,sub.size()-1)
    w6 = sub.show_i(i)
    i = randint(0,ver.size()-1)
    w3 = ver.show_i(i)
    i = randint(0,pre.size()-1)
    w4 = pre.show_i(i)
    print w1, ' ', w2, ' ', w3, ' ', w4, ' ', w5, ' ', w6, '.'

>>> from random import randint
>>> def random_sentence(art, sub, ver, pre):
    i = randint(0,art.size()-1)
    frase = art.show_i(i) + ' '
    frase.capitalize()
    i = randint(0,sub.size()-1)
    frase += sub.show_i(i) + ' '
    i = randint(0,ver.size()-1)
    frase += ver.show_i(i) + ' '
    i = randint(0,pre.size()-1)
    frase += pre.show_i(i) + ' '
    i = randint(0,art.size()-1)
    frase += art.show_i(i) + ' '
    i = randint(0,sub.size()-1)
    frase += sub.show_i(i) + '.'
    print frase

    
>>> i = 20
>>> while i:
	random_sentence(art,sub,ver,pre)
	i -= 1

# ERRO TOTAL 4 8
a cidade andou de um bicicleta.
uma gata andou de o cao.
o bicicleta correu embaixo o carro.
uma carro correu de uma gata.
uma cao correu de um carro.
o gata pulou sobre uma carro.
a cao caiu de o cidade.
a bicicleta caiu sobre a carro.
uma carro correu embaixo um bicicleta.
a cidade correu de uma cidade.
a cao caiu sob uma bicicleta.
um cidade caiu sob o carro.
um bicicleta caiu sob uma cidade.
um cidade andou sob a cidade.
um gata andou de uma cidade.
um carro andou embaixo o cao.
o cidade caiu sobre a cidade.
uma carro caiu de o gata.
uma cao andou sobre uma carro.
a bicicleta pulou de um carro.


    


[5.0]

>>> import copy

>>> class ponto:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

>>> class quadrilatero:
    def __init__(self, p1, p2, p3, p4):
        self.psw = copy.deepcopy(p1) # psw eh o inferior esquerdo
        self.pse = copy.deepcopy(p2) # pse eh o inferior direito
        self.pne = copy.deepcopy(p3) # pne eh o superior direito
        self.pnw = copy.deepcopy(p4) # pnw eh o superior esquerdo

    def show_points(self):
        print "(", self.psw.x, ",", self.psw.y, "),"
        print "(", self.pse.x, ",", self.pse.y, "),"
        print "(", self.pne.x, ",", self.pne.y, "),"
        print "(", self.pnw.x, ",", self.pnw.y, ")."
 
>>> p1 = ponto(1,1)
>>> p2 = ponto(3,1)
>>> p3 = ponto(3,3)
>>> p4 = ponto(1,3)
>>> q1 = quadrilatero(p1,p2,p3,p4)
>>> q1.show_points()
( 1 , 1 ),
( 3 , 1 ),
( 3 , 3 ),
( 1 , 3 ).

>>> class retangulo(quadrilatero):
    def __init__(self, p1, height, width):
        self.psw    = copy.deepcopy(p1) # psw eh o inferior esquerdo
        self.pse    = copy.deepcopy(p1) # psw eh o inferior direito
        self.pse.x += width
        self.pne    = copy.deepcopy(p1) # psw eh o superior direito
        self.pne.x += width
        self.pne.y += height
        self.pnw    = copy.deepcopy(p1) # psw eh o superior esquerdo
        self.pnw.y += height

    def show_dimensions(self):
        print "Heigth:", self.pnw.y - self.psw.y
        print "Width:" , self.pse.x - self.psw.x
        
>>> q2 = retangulo(p1,3,5)
>>> q2.show_points()
( 1 , 1 ),
( 6 , 1 ),
( 6 , 4 ),
( 1 , 4 ).
>>> q2.show_dimensions()
Heigth: 3
Width: 5

>>> class quadrado(retangulo):
    def __init__(self, p1, side):
        self.psw    = copy.deepcopy(p1) # psw eh o inferior esquerdo
        self.pse    = copy.deepcopy(p1) # psw eh o inferior direito
        self.pse.x += side
        self.pne    = copy.deepcopy(p1) # psw eh o superior direito
        self.pne.x += side
        self.pne.y += side
        self.pnw    = copy.deepcopy(p1) # psw eh o superior esquerdo
        self.pnw.y += side

    def show_side(self):
        print "Side:", self.pse.x - self.psw.x

        
>>> q3 = quadrado(p1,9)
>>> q3.show_points()
( 1 , 1 ),
( 10 , 1 ),
( 10 , 10 ),
( 1 , 10 ).
>>> q3.show_dimensions()
Heigth: 9
Width: 9
>>> q3.show_side()
Side: 9

>>> class trapezio(quadrilatero):
    def is_trapezio(self):
        if ((self.psw.x <= self.pnw.x) and (self.pse.x >= self.pne.x) and ((self.pne.x - self.pnw.x) < (self.pse.x - self.psw.x))):
            print "Eh trapezio."
        else:
            print "Naum eh trapezio."

            
>>> p1 = ponto(1,1)
>>> p2 = ponto(10,1)
>>> p3 = ponto(8,5)
>>> p4 = ponto(5,11)
>>> t1 = trapezio(p1,p2,p3,p4)
>>> t1.is_trapezio()
Eh trapezio.
>>> t1.pne.x = 11
>>> t1.is_trapezio()
Naum eh trapezio.
>>> t1.pne.x = 10
>>> t1.is_trapezio()
Eh trapezio.
>>> class paralelogramo(quadrilatero):
    def is_paralelogramo(self):
        if (((self.pne.x - self.pnw.x) == (self.pse.x - self.psw.x)) and ((self.pnw.y - self.psw.x) == (self.pne.y - self.pse.y))):
            print "Eh paralelogramo."
        else:
            print "Naum eh paralelogramo."

            
>>> p1 = ponto(1,1)
>>> p2 = ponto(3,1)
>>> p3 = ponto(4,2)
>>> p4 = ponto(2,2)
>>> pa = paralelogramo(p1,p2,p3,p4)
>>> pa.is_paralelogramo()
Eh paralelogramo.
>>> pa.psw.x = 2
>>> pa.is_paralelogramo()
Naum eh paralelogramo.
