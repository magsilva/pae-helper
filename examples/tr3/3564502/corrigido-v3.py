Programa��o orientada � objetos
3� Lista de exerc�cios


Jos� Arnaldo Holanda   nUSP: 3564502
Marcus Vinicius Secato nUSP: 3285140




# ERRO TOTAL 1 4
# ERRO TOTAL 1 5
# ERRO TOTAL 1 6
1) 1.1 Construtor de Objetos: � uma fun��o-membro que cria um objeto a partir de uma classe, alocando assim, um espa�o na mem�ria para este objeto.
Destrutor de Objetos: � uma fun��o-membro que apaga os objetos que n�o s�o mais necess�rios, liberando a mem�ria utilizada.
As regras de sintaxe utilizadas na defini��o de um construtor em Python s�o as seguintes: var_objeto = tipo_classe(parametros)
O mecanismo destrutor � chamado de Garbage Collector. Toda inst�ncia possui um contador de refer�ncias. Quando este contador se torna zero, a inst�ncia � destru�da.

1.2 As formas de acesso s�o p�blico e privado.

1.3 Os cinco principais conceitos s�o: Objetos e Classes; Comunica��o com Mensagens; Heran�a; Encapsulamento; Sobrecarga e Polimorfismo.

# ERRO PARCIAL 1 9
1.4 Objeto � uma abstra��o de algo cujas caracter�sticas e comportamentos s�o conhecidos, e que tem uma interface definida e restrita com entidades externas. Classes s�o a unidade de programa��o. Elas servem como "planta de projeto" de objetos. Os m�todos podem ser considerados como as a��es que a classe tem poder de realizar.

1.5 Vantagens das LPOOs: manuten��o mais r�pida e barata; processo de modelagem mais simples; projeto limpo e gerenci�vel.

2) C�digo da classe:

class Palavra:
    def __init__(self, word=""):
        self.palavra = word

    def Conta_char(self):
        return len(self.palavra)

    def Conta_o_char(self, letra):
        return self.palavra.count(letra)



Veja alguns testes com a classe Palavra:

>>> 
a = Palavra()
>>> a.palavra
''
>>> a.palavra = 'teste'
>>> a.palavra
'teste'
>>> a.Conta_char()
5
>>> a.Conta_o_char('e')
2



3) Para ler v�rias linhas do teclado � necess�rio especificar quantas linhas dever�o ser lidas. Observe o c�digo da classe Le_linha :

class Le_linha:
    def __init__(self, nline= 0):
        i = 0
        self.lista = []
        self.dic = {}
        aux= ''
        while i < nline:
            a= raw_input("Digite Linha ")
            aux = a + '\n'
            self.lista.append(aux)
            i += 1


    def contador(self):
        aux_palavra = 0
        aux_str = ''
        for a in self.lista:
            for b in a:
                if b != ' ' and b != '\n':
                    aux_str += b
                else:
                    palavra = Palavra(aux_str)
                    aux_palavra = palavra.Conta_char()
                    aux_str = ''
                    self.monta_dic(aux_palavra)
        self.print_table()

    def monta_dic(self, indice):
        if indice in self.dic.keys():
            self.dic[indice] += 1
        else:
            self.dic.__setitem__(indice, 1)

    def print_table(self):
        for a in self.dic.keys():
            print ('N�mero de palavras com ' + str(a) + ' letra(s): ' + str(self.dic[a]))


Os m�todos, contador e monta_dic, montam um dicion�rio onde o n�mero de letras em uma palavra � usado como �ndice e como valor, relacionado � esse �ndice, tem-se o n�mero de palavras cujos n�mero de letras � igual ao indicado pelo �ndice.
Veja um programa exemplo:

>>> b = Le_linha(4)
Digite Linha lista de exercicios poo
Digite Linha a prova de poo eh terca
Digite Linha hoje tem futebol
Digite Linha um dois tres quatro
>>> b.contador()
N�mero de palavras com 1 letra(s): 1
N�mero de palavras com 2 letra(s): 4
N�mero de palavras com 3 letra(s): 3
N�mero de palavras com 4 letra(s): 3
N�mero de palavras com 5 letra(s): 3
N�mero de palavras com 6 letra(s): 1
N�mero de palavras com 7 letra(s): 1
N�mero de palavras com 10 letra(s): 1

4) Foi criada uma classe Sentence, que inicia as tuplas relacionadas � artigos, substantivo, verbo e preposi��o.
O procedimento monta_sent usa o procedimento randint para selecionar aleatoriamente um valor de cada tupla a fim de montar a frase.
Veja o c�digo:
class Sentence:
    def __init__(self):
        self.artigo = ('o','a','um','uma')
        self.substantivo = ('gata','cao','cidade','carro','bicicleta')
        self.verbo = ('andou','correu','pulou','caiu')
        self.preposicao = ('de','sobre','sob', 'embaixo de')

    def monta_sent(self):
        import math
        i = 0
        indice = 0
        frase = ''
        while i < 20:
            indice = randint(0, (len(self.artigo) - 1))
            frase += self.artigo[indice] + ' '
            indice = randint(0, (len(self.substantivo) - 1))
            frase += self.substantivo[indice]+ ' '
            indice = randint(0, (len(self.verbo) - 1))
            frase += self.verbo[indice]+ ' '
            indice = randint(0, (len(self.preposicao) - 1))
            frase += self.preposicao[indice]+ ' '
            indice = randint(0, (len(self.artigo) - 1))
            frase += self.artigo[indice]+ ' '
            indice = randint(0, (len(self.substantivo) - 1))
            frase += self.substantivo[indice]
            frase += '.'
            frase = frase.capitalize()
            print frase
            i += 1
            frase = '';

# ERRO TOTAL 4 8

Exemplo de programa usando a classe Sentence:
>>> 
a = Sentence()
>>> a.monta_sent()
Uma cao pulou de o gata.
Um gata correu sobre o bicicleta.
Uma gata caiu sob o carro.
Uma cidade correu sobre uma gata.
A cao caiu sob a cidade.
O carro correu de a cidade.
Uma cao andou sob uma cao.
O cao pulou sobre o gata.
Um bicicleta correu sob a bicicleta.
A cidade pulou sob uma cidade.
Um gata andou sob uma cao.
A carro caiu sobre um cidade.
A bicicleta pulou embaixo de uma cidade.
A gata pulou de um gata.
Uma carro caiu sob uma carro.
O bicicleta caiu sobre um carro.
Um gata correu sobre uma cidade.
Uma bicicleta pulou embaixo de o gata.
A carro pulou embaixo de a gata.
Um gata caiu sobre um gata.
