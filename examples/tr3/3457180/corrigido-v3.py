Lucas Antiqueira, 3457180

Lista de Exerc�cios de POO
Prof. Renata Pontin M. Fortes
08/04/2003

1)

Um construtor serve para alocar recursos para o objeto e inicializar seus atributos. J� um destrutor libera os recursos reservados para o objeto. Em Python, o construtor deve ser identificado com o nome '__init__', e deve ainda ter um par�metro ('self'), passado implicitamente para o construtor, que indica a inst�ncia atual da classe. O mecanismo de destrui��o de objetos da linguagem utiliza um contador de refer�ncias para cada objeto; quando esse contador � zerado, um mecanismo de 'garbage collector' elimina o objeto da mem�ria.
Normalmente, na defini��o de uma classe pode-se especificar se os atributos/m�todos s�o p�blicos ou privados.
Heran�a, sobrecarga e polimorfismo, encapsulamento, objetos e classes, comunica��o com mensagens.
Classe � a defini��o conceitual de um objeto; nela est�o especificados os atributos e a��es que um objeto dessa classe apresenta. Objeto � uma classe colocada em atividade, com valores relacionados aos seus atributos e apta a receber mensagens. Os m�todos de uma classe especificam as a��es que os objetos dessa classe podem executar.
Uma grande vantagem da programa��o orientada a objetos em rela��o � programa��o procedural � a diminui��o do gap sem�ntico. Na orienta��o a objetos, a representa��o da solu��o computacional est� mais pr�xima da representa��o do problema. Al�m disso, a orienta��o a objetos proporciona um melhor reuso de software e facilita a manuten��o.


2)

class Palavras:
    def __init__(self, palavra_inicial = ""):
        self.palavra = list(palavra_inicial)
    
    def Conta_char(self):
        return len(self.palavra)

    def Conta_o_char(self, char):
        return self.palavra.count(char)

    def Muda_palavra(self, nova_palavra):
        self.palavra = list(nova_palavra)


3)

inword = 0
aux_palavra = ""
palavra = Palavras()
contagem = []
for i in range(15):
    contagem.append(0)

texto_inicial = raw_input()
texto_inicial += ' '                  #Usado contar a ultima palavra
texto = list(texto_inicial)
    
for i in range(len(texto)):
#As palavras sao delimitadas por qualquer caractere nao alfa-numerico
    if not inword:
        if texto[i].isalnum():
            inword = 1
            aux_palavra += texto[i]
    else:
        if texto[i].isalnum():
            aux_palavra += texto[i]
        else:
            inword = 0
            palavra.Muda_palavra(aux_palavra)
            count = palavra.Conta_char()
            if count >= 15:
                contagem[14] += 1
            else:
                contagem[count - 1] += 1
            aux_palavra = ""

for i in range(15):
    if i < 14:
        print 'Palavras com', i+1, 'letras:', contagem[i]
    else:
        print 'Palavras com', 15, 'letras (ou mais):', contagem[14]

# ERRO PARCIAL 3 5

4)

from random import Random

artigo = ('o', 'a', 'um', 'uma')
substantivo = ('gata', 'cao', 'cidade', 'carro', 'bicicleta')
verbo = ('andou', 'correu', 'pulou', 'caiu')
preposicao = ('de', 'sobre', 'sob', 'embaixo')

r = Random()
for i in range(20):
    print artigo[int(r.uniform(0, len(artigo)))].capitalize() + ' ' + substantivo[int(r.uniform(0, len(substantivo)))] + ' ' + verbo[int(r.uniform(0, len(verbo)))] + ' ' + preposicao[int(r.uniform(0, len(preposicao)))] + ' ' + artigo[int(r.uniform(0, len(artigo)))] + ' ' + substantivo[int(r.uniform(0, len(substantivo)))] + '.'

# ERRO TOTAL 4 8
