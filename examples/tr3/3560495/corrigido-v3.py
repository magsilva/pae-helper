Programa��o Orientada a Objetos - Prof. Renata Pontin M. Fortes

Lista de Exerc�cios

Aluno: Santiago de Moura Luz	N� USP: 3560495	   (Data de entrega: 08/04/2003)



  1
# ERRO TOTAL 1 5
# ERRO TOTAL 1 7
	Construtor de objetos � um (pseudo) m�todo que determina quais a��es devem ser executadas quando da cria��o de um objeto. Em Python, o construtor � definido por __init__(self[,args]). Por outro lado, a remo��o de objetos � efetivada explicitamente pelo programador (atrav�s do operador __del__(self)), que pode tamb�m especificar o procedimento que deve ser executado para a libera��o de outros recursos alocados pelo objeto atrav�s de um m�todo Destrutor.
	Os 5 principais conceitos que se consolidaram no paradigma de "Programa��o Orientada a Objetos" s�o:
1.Objeto: Um objeto � um elemento computacional que representa, no dom�nio da solu��o, alguma entidade (abstrata ou concreta) do dom�nio de interesse do problema sob an�lise. Objetos similares s�o agrupados em classes.
2.Classe: � a implementa��o de um tipo de objeto o qual cont�m uma estrutura de dados e m�todos que especificam opera��es que podem ser feitas com aquela estrutura de dados.
3.M�todos e Sobrecarga: Um m�todo nada mais � que o equivalente a um procedimento ou fun��o, com a restri��o que ele manipula apenas suas vari�veis locais e os atributos que foram definidos para a classe. Sobrecarga � a capacidade de uma opera��o possuir mais do que um m�todo para sua execu��o.
4.Heran�a: � a principal caracter�stica da programa��o orientada a objetos pois � atrav�s desse mecanismo que a classe mais especializada herda todos os m�todos e atributos da classe mais geral.
5.Encapsulamento: Todas as classes possuem duas interfaces, a Interface P�blica e a Interface Privada,  interface p�blica compreende todas as opera��es e propriedades que podem ser acessadas diretamente pelas demais classes, e a interface privada compreende as opera��es e propriedades que podem ser acessadas apelas pela pr�pria classe, sendo que a interface privada � protegida pelo encapsulamento.

Programa��o orientada a objetos tem como principal objetivo atingir um desenvolvimento interativo e incremental, cria��o r�pida de prot�tipos, c�digos reutiliz�veis e extens�veis atrav�s do encapsulamento dos dados e uma modelagem do problema a ser solucionado.
	O mecanismo de heran�a d� um grande impulso � POO (Programa��o Orientada a Objetos) visto que ele oferece recursos para reutiliza��o de c�digo, onde as classes representam grupos de elementos reais e os objetos representam elementos com exist�ncia f�sica individual. A vantagem disso � justamente a modelagem e a reutiliza��o de c�digos (classes) j� testados, o que aumenta a confiabilidade do c�digo e reduz o n�vel de manuten��o.

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
            


