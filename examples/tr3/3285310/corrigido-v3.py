#   Lista de Exercicios de P.O.O
#
#   Aluno: Rafael Henrique Manoel           nro. 3285310
#
#--------------------------------------------------------/

#
#   Exercicio 1
#   ---------------
#
#   1.a) Construtor -> funcao membro responsavel por inicializar o objeto,
#        setando as variaveis inciais e alocando memoria para ele.
#        A sintaxe para definir um construtor e a seguinte:

# ERRO PARCIAL 1 4

#
#        def __init__(self):
#           <corpo da funcao>

# ERRO TOTAL 1 5

#        Destrutor -> desaloca toda a memoria usada pelo objeto. Em python,
#        o destrutor e implementado atraves de garbage colect, ou seja, e feito
#        automaticamente pelo interpretador.
#
# ERRO PARCIAL 1 7

# ERRO TOTAL 1 8

#   1.b) Nome da classe, metodos e atributos
#
#   1.c) Os 5 principais conceitos de orientacao a objetos sao:
#           Classes o Objetos
#           Comunicacao com Mensagens
#           Sobrecarga e Polimorfismo
#           Heranca
#           Encapsulamento
#
#   1.d) E basicamente uma estrutura de dados que agrega, junto a ela, funcoes
#        (metodos) que tratam seus dados. Uma instacia de uma classe recebe o
#        nome de objeto.
#   1.e) A principal vantagem em se usar linguagens OO e o fato de poder
#        reutilizar os codigos ja escritos. E tambem na facilidade de poder
#        criar softwares em equipes, pois como todo o programa e dividido em
#        objetos, cada parte da equipe pode fazer objetos diferentes, integrando
#        estes posteriormente.   
#           


#
#   Exercicio 2 -> Classe palavra
#
class Palavras:

    texto = []
    nro_char = []

    def __init__(self, nova_palavra):
        i = 0
        inicio = 0
        self.maior = 0
        while 1:
            fim = nova_palavra.find(" ",inicio)
            if fim < 0:
                self.texto.append(nova_palavra[inicio:len(nova_palavra)])
                self.nro_char.append(len(self.texto[i]))
                if self.nro_char[i] > self.maior:
                    self.maior = self.nro_char[i]
                break
            else:
                self.texto.append(nova_palavra[inicio:fim])
                self.nro_char.append(len(self.texto[i]))
                if self.nro_char[i] > self.maior:
                    self.maior = self.nro_char[i]                
                inicio = fim+1
            i+=1
        
    def Maior_palavra(self):
        return self.maior

            
    def Conta_char(self, indice):
        return self.nro_char[indice]

    def Conta_o_char(self, indice, char):
        return self.texto[indice].count(char)

    def __str__(self):
        return str(self.texto)

    def __len__(self):
        return len(self.texto)
    

#
#   Exercicio 3
#

# ERRO PARCIAL 3 3

frase = Palavras(raw_input("Digite o texto :\n"))
i = 1
tam = len(frase)
while i <= frase.Maior_palavra():
    nro_palavra = 0
    j = 0
    while j < tam:
        if frase.Conta_char(j) == i:
            nro_palavra +=1
        j += 1
    print "numero de palavras com ",i," letra(s)..: ", nro_palavra    
    i+=1


#
#   Exercicio 4
#
import random

artigo = ("o","a","um","uma")
substantivo = ("gata","cao","cidade","carro","bicicleta")
verbo = ("andou","correu","pulou","caiu")
prep = ("de","sobre","sob","embaixo")

frase = []

i = 0
while i < 20:
    a1 = random.choice(artigo).capitalize()

    s1 = random.choice(substantivo)
    v = random.choice(verbo)
    p = random.choice(prep)
    a2 = random.choice(artigo)
    s2 = random.choice(substantivo)

    frase.append(a1 + " " + s1 + " " + v +" "+ p +" "+ a2 +" "+ s2 + ".")
    print frase[i]
    i+=1    
