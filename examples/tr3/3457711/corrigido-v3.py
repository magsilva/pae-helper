#!/usr/bin/python
#Exercicio 2.

import pprint;
import string;
import fileinput
import sys;

array = [0,0,0,0,0,0,0,0,0,0];
def divide(line):
	lista = string.split(line);
	return lista

class palavra: 
	def __init__(self, word):
		self.palavra = word;
	def qtd_caracter(self):
		return len(self.palavra);
	def ocorrencia(self, char):
		return string.count(self.palavra, char);
		
	
print "Digite o texto e aperte ^D^D para terminar"
for line in fileinput.input():
	lista = divide(line);
	for x in lista: 
		tmp = palavra(x);
		qtd = tmp.qtd_caracter();
		if (qtd < 9):
			array[qtd-1] +=1;
		else :
			array[9] += 1;

print "qtd Caracter   |   Ocorrencia"
for i in range(1,10): 
  	print "%6d         |"%i, "%6d"%array[i-1];
	
print "     > 10      |   %4d "% array[9];

# ERRO PARCIAL 3 5

#Breno Leitao 3457711

# ERRO TOTAL 1 4
# ERRO TOTAL 1 5
1-a) Construtor eh um metodo dentro de uma classe que instancia a classe em um objeto.  Destrutor, por sua vez, eh uma mensagem dentro de uma classe que tem a funcao de remover o objeto instanciado por essa classe. Na linguagem Python seguimos a seguinte sintaxe:
	Construtor: 
		__init__(argumentos):
			corpo
	
	Destrutor:
		__del__(self):
			corpo

	`A essas duas fases, tem-se a fase de atuacao, que fecha o ciclo de vida de uma objeto.

# ERRO TOTAL 1 7

1-b) 	Formas de acesso??  Nao sei.
# ERRO TOTAL 1 8

1-c)	Os cinco principais conceitos empregados nas linguagens de orientacao objeto sao:
	- Classes e Objetos
	- Heranca
	- Comunicacao com mensagens
	- Polimorfismo e sobrecarga
	- Encapsulamento

# ERRO PARCIAL 1 1
1-d)	Uma classe eh a "planta de projeto" de um objeto, ou seja, descreve que dados/metodos um objeto dado deve conter.
# ERRO PARCIAL 1 2
	Um objeto eh a instanciacao de uma classe, ou seja, eh a classe sendo utilizada.
	Metodos de uma classe, sao meramente funcoes pertencentes a essa classe.

1-e)	As vantagens sao, segundo comentam, a diminuicao do "gap semantico", que ocorre entrea a fase de analise de requisito e a fase de implementacao, isso significa que com a utilizacao de uma linguagem com capacidade de orientacao objeto fica mais facil a traducao do projeto para o software em si. Ademais, pode-se citar as vantagens dadas acima, somada a uma forte reutilizacao de classes, expansibilidade, maior claridade e produtividade.



			

#!/usr/bin/python
# Aluno: Breno Leitao 3457711

import gc;



class quadrilatero:
	def __init__(self,p1,p2,p3,p4):
		self.x1 = p1[0];
		self.y1 = p1[1];
		self.x2 = p2[0];
		self.y2 = p2[1];
		self.x3 = p3[0];
		self.y3 = p3[1];
		self.x4 = p4[0];
		self.y4 = p4[1];

	def imprime_cordenadas(self):         #obsoleto
		print "(%2.2f,%2.2f) (%2.2f,%2.2f)\n(%2.2f,%2.2f) (%2.2f,%2.2f)"%(self.x1, self.y1, self.x2, self.y2, self.x3, self.y3, self.x4, self.y4); 

	def __str__(self):
		return "(%2.2f,%2.2f) (%2.2f,%2.2f)\n(%2.2f,%2.2f) (%2.2f,%2.2f)\n"%(self.x1, self.y1, self.x2, self.y2, self.x3, self.y3, self.x4, self.y4); 

class trapesio(quadrilatero):
	pass;
class paralelograma(quadrilatero):
	pass;
class retangulo(quadrilatero):
	def __init__(self, canto1,canto2):
		self.x1 = canto1[0];
		self.y1 = canto1[1];
		self.x2 = canto2[0];
		self.y2 = canto2[1];
		self.x3 = canto1[0];
		self.y3 = canto2[1];
		self.x4 = canto2[0];
		self.y4 = canto1[1];

q = quadrilatero([1,2],[3,2],[1,2],[3,10]);
r = quadrilatero([1,2],[3,2],[1,2],[3,10]);
p = paralelograma([1,2],[3,3],[10,11], [3, 3.1415]); 
t = paralelograma([2,2],[2,3],[10.1,1], [2.7182, 3.1415]); 
print q
#print
print r
#print
print p
#print
print t
#!/usr/bin/python
#Exercicio 2.

import string;
import sys;
if (len(sys.argv) > 2): 
	word = sys.argv[1];
	letra = sys.argv[2];
else: 
	word = "Breno Leitao";
	letra = "o";

class palavra: 
	def __init__(self, word):
		self.palavra = word;
	def qtd_caracter(self):
		return len(self.palavra);
	def ocorrencia(self, char):
		return string.count(self.palavra, char);
		
	
a=palavra(word);
print "A quantidade de ocorrencia da letra '", letra, "' na palavra '", word, " ' eh :" ,  a.ocorrencia(letra);
print "o Total de caracter dessa palavra eh: %d"% a.qtd_caracter();

#!/usr/bin/python
#autor: Breno Leitao

import string
from random import Random

artigo = ["o","um","a", "uma"]
substantivo = ["cao", "carro", "bicicleta","gata","cidade"]
verbo = ["andou", "correu", "pulou","caiu"]
preposicao = ["de", "sobre", "sob", "embaixo"]

g =  Random();             # Seed baseado no clock
oracao=[];

rand = g.randrange(0.0, 4.0);
oracao.append(artigo[rand]);


if (rand <2 ):          #Adicionando Concordancia verbal..
	rand  = g.randrange(0.0,2.0);
else: 
	rand = g.randrange(3.0, 5.0);
oracao.append(substantivo[rand]);

rand = g.randrange(0.0, 4.0);
oracao.append(verbo[rand]);

rand = g.randrange(0.0, 4.0);
oracao.append(preposicao[rand]);

rand = g.randrange(0.0, 4.0);
oracao.append(artigo[rand]);

if (rand <2 ):          #Adicionando Concordancia verbal..
	rand  = g.randrange(0.0,2.0);
else: 
	rand = g.randrange(3.0, 5.0);
oracao.append(substantivo[rand]);

string =  string.capitalize(oracao[0]) + " " + oracao[1] + " " + oracao[2] + " " + oracao[3] + " " + oracao[4] + " " +  oracao[5] + "."
print string

# ERRO TOTAL 4 8
