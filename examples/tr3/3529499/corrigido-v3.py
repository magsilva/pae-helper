Lista de exercícios 

1)

a) O construtor eh o metodo que inicializa a classe, 
ou seja, qualquer alteracao no construtor(parametro,atribuicao,etc),
sera automaticamente realizada quando a classe for chamada.

Construtor - def __init__(parametros) :

 O destrutor nao precisa ser chamado, ele eh automaticamente "feito" 
no fim da classe.

# ERRO TOTAL 1 4
b)


c) 1.Classe de objetos
2.Comunicacao por troca de mensagem
3.Heranca
4.Encapsulamento
5.Sobrecarga e Polimorfismo

# ERRO TOTAL 1 1
d)Uma classe eh um conjunto de funcoes que se aplicam 
somente a objetos daquela classe.

Um objeto eh instanciado em uma classe e pode utiliazar de seus metodos.

Um metodo eh uma funcao dentro de uma classe.

# ERRO PARCIAL 1 10

e)Varias pessoas podem trabalhar ao mesmo tempo no mesmo projeto e nao
necessariamente em conjunto. Elas podem subdividir o trabalho em classes
e objetos a serem implementados e construidos.

		#Exercicio 2
#Exemplo de chamadas :
#a = Palavras('qualquerpalavra')
#a.Conta_char()
#a.Conta_o_char('qualquerletra')

class Palavras :
    def __init__(self,word) :
        self.palavra = word

    def Conta_char(self) :
        return len(self.palavra)

    def Conta_o_char(self,char) :
        return self.palavra.count(char)
    
#Exercicio 3
#Nao precisa de chamada.
#Eh soh seguir as instrucoes que aparecerao na tela

# ERRO 3 3

texto = raw_input('Digite um texto (linha vazia+<espaco>+<enter>=sair) : ')
letra1 = 0
letra2 = 0
letra3 = 0
letra4 = 0
letra5mais = 0
while texto != ' ' :
    palavras = texto.split(' ')
    for i in palavras :
        obj = Palavras(i)
        count = obj.Conta_char()
        if count == 1 :
            letra1 += 1
        elif count == 2 :
            letra2 += 1
        elif count == 3 :
            letra3 += 1
        elif count == 4 :
            letra4 += 1
        else :
            letra5mais += 1
    texto = raw_input()
print '1 letra - %d palavras' %letra1
print '2 letras - %d palavras' %letra2
print '3 letras - %d palavras' %letra3
print '4 letras - %d palavras' %letra4
print '5 ou mais letras - %d palavras' %letra5mais

# ERRO PARCIAL 3 5

#Exercicio 4
#Nao ha chamada.
#Eh soh "rodar" o script.
import random
artigo = ('o','a','um','uma','uns','umas')
substantivo = ('gata','cao','cidade','carro','biboca','mano','mane','mina')
verbo = ('andou','correu','pulou','caiu','voou','quebraram','zoaram')
preposicao = ('de','sobre','sob','embaixo','em cima')

i = 0
while i < 20 : 
    frase = random.choice(artigo).capitalize()
    frase += ' ' + random.choice(substantivo)
    frase += ' ' + random.choice(verbo)
    frase += ' ' + random.choice(preposicao)
    frase += ' ' + random.choice(artigo)
    frase += ' ' + random.choice(substantivo) + '.'
    i += 1
    print frase

# ERRO TOTAL 4 8
