Lucas Antiqueira, 3457180

Lista de Exercícios de POO
Prof. Renata Pontin M. Fortes
08/04/2003

1)

Um construtor serve para alocar recursos para o objeto e inicializar seus atributos. Já um destrutor libera os recursos reservados para o objeto. Em Python, o construtor deve ser identificado com o nome '__init__', e deve ainda ter um parâmetro ('self'), passado implicitamente para o construtor, que indica a instância atual da classe. O mecanismo de destruição de objetos da linguagem utiliza um contador de referências para cada objeto; quando esse contador é zerado, um mecanismo de 'garbage collector' elimina o objeto da memória.
Normalmente, na definição de uma classe pode-se especificar se os atributos/métodos são públicos ou privados.
Herança, sobrecarga e polimorfismo, encapsulamento, objetos e classes, comunicação com mensagens.
Classe é a definição conceitual de um objeto; nela estão especificados os atributos e ações que um objeto dessa classe apresenta. Objeto é uma classe colocada em atividade, com valores relacionados aos seus atributos e apta a receber mensagens. Os métodos de uma classe especificam as ações que os objetos dessa classe podem executar.
Uma grande vantagem da programação orientada a objetos em relação à programação procedural é a diminuição do gap semântico. Na orientação a objetos, a representação da solução computacional está mais próxima da representação do problema. Além disso, a orientação a objetos proporciona um melhor reuso de software e facilita a manutenção.


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
