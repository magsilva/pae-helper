Programação Orientada a Objetos - Prof. Renata Pontin M. Fortes

Lista de Exercícios

Aluno: Santiago de Moura Luz	Nº USP: 3560495	   (Data de entrega: 08/04/2003)



  1
# ERRO TOTAL 1 5
# ERRO TOTAL 1 7
	Construtor de objetos é um (pseudo) método que determina quais ações devem ser executadas quando da criação de um objeto. Em Python, o construtor é definido por __init__(self[,args]). Por outro lado, a remoção de objetos é efetivada explicitamente pelo programador (através do operador __del__(self)), que pode também especificar o procedimento que deve ser executado para a liberação de outros recursos alocados pelo objeto através de um método Destrutor.
	Os 5 principais conceitos que se consolidaram no paradigma de "Programação Orientada a Objetos" são:
1.Objeto: Um objeto é um elemento computacional que representa, no domínio da solução, alguma entidade (abstrata ou concreta) do domínio de interesse do problema sob análise. Objetos similares são agrupados em classes.
2.Classe: É a implementação de um tipo de objeto o qual contém uma estrutura de dados e métodos que especificam operações que podem ser feitas com aquela estrutura de dados.
3.Métodos e Sobrecarga: Um método nada mais é que o equivalente a um procedimento ou função, com a restrição que ele manipula apenas suas variáveis locais e os atributos que foram definidos para a classe. Sobrecarga é a capacidade de uma operação possuir mais do que um método para sua execução.
4.Herança: É a principal característica da programação orientada a objetos pois é através desse mecanismo que a classe mais especializada herda todos os métodos e atributos da classe mais geral.
5.Encapsulamento: Todas as classes possuem duas interfaces, a Interface Pública e a Interface Privada,  interface pública compreende todas as operações e propriedades que podem ser acessadas diretamente pelas demais classes, e a interface privada compreende as operações e propriedades que podem ser acessadas apelas pela própria classe, sendo que a interface privada é protegida pelo encapsulamento.

Programação orientada a objetos tem como principal objetivo atingir um desenvolvimento interativo e incremental, criação rápida de protótipos, códigos reutilizáveis e extensíveis através do encapsulamento dos dados e uma modelagem do problema a ser solucionado.
	O mecanismo de herança dá um grande impulso à POO (Programação Orientada a Objetos) visto que ele oferece recursos para reutilização de código, onde as classes representam grupos de elementos reais e os objetos representam elementos com existência física individual. A vantagem disso é justamente a modelagem e a reutilização de códigos (classes) já testados, o que aumenta a confiabilidade do código e reduz o nível de manutenção.

# ERRO TOTAL 1 8

  2

class palavras:
    def __init__(self, palav):
        self.palavra = palav
    def conta_char(self):
        return len(self.palavra)
    def conta_o_char(self, caracter):
        return self.palavra.count(caracter)




  3

def tabletras():
    tabela = [] 
    linha = raw_input("Frase: ") 
    while linha != "": 
        for i in range(1, 20): 
            tabela.append(0) 
        lista = linha.split(" ") 
        for p in lista: 
            palavra = palavras(p) 
            i = palavra.conta_char() 
            tabela[i] += 1 

        print("Numero de palavras com")
        for i in range(1, 20): 
            try: 
                if tabela[i] != 0: 
                    print "   " + str(i) + " caracteres: " + str(tabela[i]) 
            except: 
                a = 0 

        print("--------------------------------------- (digite <ENTER> para parar)")
        linha = raw_input("Frase: ") 
        tabela = []

# ERRO PARCIAL 3 3
# ERRO PARCIAL 3 5

  4

class frases: 
    def __init__(self): 
        self.artigo = ['o', 'a', 'um', 'uma'] 
        self.substantivo = ['gata', 'cachorro', 'cidade', 'bicicleta', 'aviao', 'lagartixa'] 
        self.verbo = ['andou', 'correu', 'perdeu', 'pulou', 'caiu', 'voou', 'quebrou'] 
        self.preposicao = ['de', 'sobre', 'embaixo', 'em', 'sob'] 
        self.frases = [] 
        self.constroi_frase() 
    def constroi_frase(self): 
        import random 
        for i in range(0, 20): 
            frase = ' ' 
            art1 = random.choice(self.artigo) 
            art = art1.capitalize() 
            sub1 = random.choice(self.substantivo) 
            ver = random.choice(self.verbo) 
            prep = random.choice(self.preposicao) 
            art2 = random.choice(self.artigo) 
            sub2 = random.choice(self.substantivo) 
            frase = art + ' ' + sub1 + ' ' + ver + ' ' + prep + ' ' + art2 + ' ' + sub2 + '.' 
            self.frases.append(frase) 
 
        for obj in self.frases: 
            print obj
            


