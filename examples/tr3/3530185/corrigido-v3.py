--------------------------------------------------	
	ICMC - USP - Exercicio de P.O.O 
	    Renata Pontin M. Fortes
--------------------------------------------------
Katsumi Arackawa Junior		N.USP:3530185
--------------------------------------------------
1))
a)
# ERRO TOTAL 1 4
Construtor de objetos: Assim como as variaveis precisam ser instanciadas
os objetos também precisam ser criadas. Para isso eh utilizada o construtor de
objetos.
Destrutor de objetos é utilizado quando os objetos não são mais necessários e são 
apagados e a memória utilizada pelo objeto eh liberada.
Ex: 	def__init__(self [,args]) => inicializa uma nova instancia
	def__del__(self) => destrói uma instancia
# ERRO PARCIAL 1 5 
# ERRO TOTAL 1 7
b)
# ERRO TOTAL 1 8

c)
*Classe/Objeto
*Herança
*encapsulamento
*Sobrecarga e Polimorfismo
*Comunicação por mensagens

d)
# ERRO TOTAL 1 1
Classe eh um conjunto de atributos que são associados a uma coleção de objetos chamados
intâncias.
# ERRO TOTAL 1 2
Objetos incluem os tipos de dados fundamentais como números, strings, listas e dicionarios,
Método é uma função que realiza alguma operação sobre um objeto quando o método eh chamado.

e)
A programação orientada a objetos veio para aumentar a produtividade do programador permitindo
o reuso do software e a expansabilidade.  Melhora também a questão de complexibilidade
e o custo de manutenção do software.

2)
Vide programas em ANEXO.
class palavras :

    def __init__(self, palavra):
        self.palavra=palavra

    def conta_char(self):
        nrochar=len(self.palavra)
        return(nrochar)

    def conta_o_char(self, caracter):
        nrocaracter=self.palavra.count(caracter)
        return nrocaracter

# ERRO TOTAL 3 3
quantidade=[]
listaux=""
lista2=[]
i=0
frase=raw_input('Digite uma frase: ')
for caracter in frase:
    if caracter != ' ':
        listaux=str(listaux)+str(caracter)
    elif caracter == ' ':
        lista2.append(palavras(listaux))
        listaux=""
        i+=1
lista2.append(palavras(listaux))

for n in range(0,i+1):
    quantidade.append(lista2[n].conta_char())

for m in range(1,20):
    print "%d palavras com %d caracteres" % (quantidade.count(m),m)

# ERRO PARCIAL 3 5


   
  
        
    
import random
artigo=('o','a','um','uma')
substantivo= ('bicicleta', 'gato', 'cachorro','carro')
verbo=('atropelou','bateu', 'comeu', 'mordeu', 'caiu', 'correu')
preposicao=('de','sobre','sob', 'embaixo')

listasentenca=[]
sentenca=""
frase=""
for n in range(0,20):
    sentenca=""
    auxart1=random.choice(artigo)
    auxsub1=random.choice(substantivo)
    auxverb=random.choice(verbo)
    auxprep=random.choice(preposicao)
    auxart2=random.choice(artigo)
    auxsub2=random.choice(substantivo)
    sentenca=str(auxart1)+" "+str(auxsub1)+" "+str(auxverb)+" "+str(auxprep)+" "+str(auxart2)+" "+str(auxsub2)+"."
    listasentenca.append(sentenca)

for n in range(0,20):
    frase=str(listasentenca[n])
    print "%d) %s" %(n+1, frase.capitalize())
    
# ERRO PARCIAL 4 6
# ERRO PARCIAL 4 7 
