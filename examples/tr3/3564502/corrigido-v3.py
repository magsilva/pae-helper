Programação orientada à objetos
3ª Lista de exercícios


José Arnaldo Holanda   nUSP: 3564502
Marcus Vinicius Secato nUSP: 3285140




# ERRO TOTAL 1 4
# ERRO TOTAL 1 5
# ERRO TOTAL 1 6
1) 1.1 Construtor de Objetos: é uma função-membro que cria um objeto a partir de uma classe, alocando assim, um espaço na memória para este objeto.
Destrutor de Objetos: é uma função-membro que apaga os objetos que não são mais necessários, liberando a memória utilizada.
As regras de sintaxe utilizadas na definição de um construtor em Python são as seguintes: var_objeto = tipo_classe(parametros)
O mecanismo destrutor é chamado de Garbage Collector. Toda instância possui um contador de referências. Quando este contador se torna zero, a instância é destruída.

1.2 As formas de acesso são público e privado.

1.3 Os cinco principais conceitos são: Objetos e Classes; Comunicação com Mensagens; Herança; Encapsulamento; Sobrecarga e Polimorfismo.

# ERRO PARCIAL 1 9
1.4 Objeto é uma abstração de algo cujas características e comportamentos são conhecidos, e que tem uma interface definida e restrita com entidades externas. Classes são a unidade de programação. Elas servem como "planta de projeto" de objetos. Os métodos podem ser considerados como as ações que a classe tem poder de realizar.

1.5 Vantagens das LPOOs: manutenção mais rápida e barata; processo de modelagem mais simples; projeto limpo e gerenciável.

2) Código da classe:

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



3) Para ler várias linhas do teclado é necessário especificar quantas linhas deverão ser lidas. Observe o código da classe Le_linha :

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
            print ('Número de palavras com ' + str(a) + ' letra(s): ' + str(self.dic[a]))


Os métodos, contador e monta_dic, montam um dicionário onde o número de letras em uma palavra é usado como índice e como valor, relacionado à esse índice, tem-se o número de palavras cujos número de letras é igual ao indicado pelo índice.
Veja um programa exemplo:

>>> b = Le_linha(4)
Digite Linha lista de exercicios poo
Digite Linha a prova de poo eh terca
Digite Linha hoje tem futebol
Digite Linha um dois tres quatro
>>> b.contador()
Número de palavras com 1 letra(s): 1
Número de palavras com 2 letra(s): 4
Número de palavras com 3 letra(s): 3
Número de palavras com 4 letra(s): 3
Número de palavras com 5 letra(s): 3
Número de palavras com 6 letra(s): 1
Número de palavras com 7 letra(s): 1
Número de palavras com 10 letra(s): 1

4) Foi criada uma classe Sentence, que inicia as tuplas relacionadas à artigos, substantivo, verbo e preposição.
O procedimento monta_sent usa o procedimento randint para selecionar aleatoriamente um valor de cada tupla a fim de montar a frase.
Veja o código:
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
