#Lista de Exercicios de P.O.O.
# Hugo Degiovani Junior   n. 3530230
# Luiz Carlos Genoves Junior n. 3542376
#------------------------------------------------------------------------------

# Exercicio 1

# ERRO TOTAL 1 4
# ERRO TOTAL 1 5
# ERRO PARCIAL 1 7

#  A)Contrutor e uma funcao que desempenha o papel de criacao de novas instancias de objetos.
#              def __init__(self,[arg]):
#                  {corpo da funcao}
#    Destrutor e a funcao com o papel de apagar o espaco de memoria utilizado pela
#      instancia que nao e mais uzada.
#    Em Python a funcao de "destrutor" e feita automaticamente pelo compilador atraves
#      da funcao garbage_colector.

#  B)As formas de acesso normalmente ultilizadas sao por Nome da Classe,Metodos e Atributos.
# ERRO TOTAL 1 8

#  C) 1-     Objetos e Classes
#     2-     Comunicacao com Mensagens
#     3-     Heranca
#     4-     Encapsulamento
#     5-     Sobrecarga e Polimorfismo

#  D)Classe: E uma especificacao de um tipo de dados definidas para variaveis e funcoes
#            comuns a todos os objetos desse tipo.
#    Objeto: E uma instancia de uma classe.
#    Metodos de uma Classe: Sao as funcoes definidas para os objetos do tipo de dados
#            da classe.

#  E)-Reutilizacao do codigo;
#    -Facilidade de implementacao;
#    -Disponibilidade de implementacao em grupos;
#    -Desenvolvimento e manutencao mais rapido e mais barato;etc
# Exercicio 2
class Palavras:
    def __init__(self,palavra=""):
        self.palavra=palavra
    def Conta_char(self):
        return len(self.palavra)
         
    def Conta_o_char(self,letra):
        print self.palavra.count(letra)

# Exercicio 3
class Texto:
    def __init__(self,texto=""):
        self.texto=texto
    def tabela(self):
        lista2=[]
        c=1
        lista=self.texto.split(" ")
        for a in lista:
            palavra=Palavras(a)
            n=palavra.Conta_char()
            lista2.append(n)
        print "Palavras com:"
        while c <= max(lista2):
            if lista2.count(c)!=0:
                print "%d letra(s): %d" %(c,lista2.count(c)) 
            c=c+1
        
            
#Exercicio 4
a=("o","a","um","uma")
s=("gato","cachorro","homem","garota")
v=("correu","falou","pulou","latiu")
p=("com",",sobre","emcima","para")
class Frases:
    def __init__(self,art=(),sub=(),ver=(),prepo=()):
        self.art=art
        self.sub=sub
        self.ver=ver
        self.prepo=prepo
    def Monta(self):
        from random import choice
        for a in range(0,20):
            lista=[]
            lista.append(choice(self.art))
            lista.append(choice(self.sub))
            lista.append(choice(self.ver))
            lista.append(choice(self.prepo))
            lista.append(choice(self.art))
            lista.append(choice(self.sub))
            lista[0]=lista[0].capitalize()
            print "Frase %d: %s %s %s %s %s %s." %(a+1,lista[0],lista[1],lista[2],lista[3],lista[4],lista[5])
                
# ERRO TOTAL 4 6
# ERRO TOTAL 4 7
# ERRO TOTAL 4 8         
