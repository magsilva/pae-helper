# Alunos Koji E. Sasaoka 3560665
#        Chen Xu Sheng   3456310
#
#
# Lista de Exercicios

# ERRO PARCIAL 1 5
# Exercicio 1
#   a) Construtor e a funcao chamada ao criar uma nova instancia da classe,
# e o destrutor e chamado ao final do bloco em que a instancia foi declarada,
# onde o objeto sera "destruido". Para declararmos o construtor, escrevemos
# uma funcao do seguinte modo def __init__ () :, e inicializamos os dados da
# classe. O destrutor e chamado com o garbage colector, declarado como :
# def __del__ ():.

# ERRO TOTAL 1 7

#   b) Publica, privada e protegida.
#
#   c) Objetos e classes, heranca, polimorfismo e sobrecarga, troca de men-
# sagens e encapsulamento.
#
#   d) Classe e uma definicao de uma "estrutura" que contem dados e metodos.
# Objeto e uma instancia de uma classe. Metodos de uma classe sao funcoes que
# a classe executa para manipular seus dados ou trabalhar com outras classes.
#
#
#   e) Alta reusabilidade, alta manutenibilidade, maior modularizacao e
# consequentemente independencia entre os modulos, possibilitando a
# implementacao em grupo mais facil e acaba sendo mais facil de programar
# devido a proximidade dos objetos com o raciocinio humano.
#
#
#
#
#


# Exercicio 2

class Palavra :
    def __init__ (self):
        self.texto = ""

    def Atribui (self, val):
        if type(val) == str :
            self.texto = val
        
    def Conta_Char (self):
        return len(self.texto)
    
    def Conta_o_Char (self, qual):
        import string
        return string.count(self.texto, qual)
        
# ERRO TOTAL 3 3
#Exercicio 3
    import string
    texto = raw_input('Digite as palavras :  ')
    
    lista = string.split (texto)
    maior = 0
    for procura in lista :
        if len(procura) > maior :
            maior = len(procura)

    contadores = []
    for valor in range(0, maior) :
        contadores.append (0)

    for pal in lista :
        temp = Palavra()
        temp.Atribui (pal)
        contadores[temp.Conta_Char() - 1] += 1

    indice = 0
    for valor in contadores :
        indice += 1
        print "Palavras com %2d Letras : %2d ." % (indice, valor)

#Exercicio 4
    def Indice (lista) :
        import random
        valor = int(random.random() * len(lista))
        return valor
        
    artigos = ["o", "a", "um", "uma"]
    substantivos = ["gata", "cao", "cidade", "carro", "bicicleta"]
    verbos = ["andou", "correu", "pulou", "caiu"]
    preposicoes = ["de", "sobre", "sob", "embaixo"]

    import string
    import random
    
    for contador in range(1, 20):
        texto = ""

        indice = 0
        for letra in artigos[Indice(artigos)]:
            if indice == 0 :
                texto += string.upper(letra)
            else :
                texto += letra
            indice += 1
            
        texto += " "

        texto += substantivos[Indice(substantivos)] + " "

        texto += verbos[Indice(verbos)] + " "

        texto += preposicoes[Indice(preposicoes)] + " "

        texto += artigos[Indice(artigos)] + " "

        texto += substantivos[Indice(substantivos)] + ". \n"

        print texto

# ERRO TOTAL 4 8
