# Desenvolvido por LUIZ CARLOS GENOVES JR. NUSP 3542376
#		   DENIS MACIEL GONCALVES  NUSP 3641220

# Data do desenvolvimento: 28/03/2003, SCE-213

# 2.1: O programa abaixo define uma classe "conjunto de inteiros", que contem uma lista
#      de numeros inteiros. Faz entre objetos desta classe operacoes basicas de conjuntos
#      como INTERSECCAO *inter(a,b)*, UNIAO *uniao(a,b)* e SUBTRACAO *sub(a,b)*

class ConjInt:
  "Conjunto de numeros inteiros"
  def __init__(self,lista=[]):
    self.lista = []
    if lista:
      if type(lista) != list:
        if lista.__class__ == ConjInt:
	  lista = lista.lista
	else:
          lista = [lista]
      for i in range(len(lista)):
        if type(lista[i]) == int:
	  self.lista.append(lista[i])
    if self.lista:
      self.noredunt(0)
    self.lista.sort()

  def noredunt(self,i):
    if i < len(self.lista):
      if self.lista.count(self.lista[i]) > 1:
        for j in range(self.lista.count(self.lista[i])):
          self.lista.remove(self.lista[i])
      self.noredunt(i+1)
      
  def printo(self):
    print self.lista

  def add(self, x):
    if type(x) == int:
      self.lista.append(x)

def inter(A, B):
  interAB = []
  if len(A.lista) < len(B.lista):
    for i in range(len(A.lista)):
      if B.lista.count(A.lista[i]):
        interAB.append(A.lista[i])
  else:
    for i in range(len(B.lista)):
      if A.lista.count(B.lista[i]):
        interAB.append(B.lista[i])
  return ConjInt(interAB)

def sub(A, B):
  import copy
  C = copy.deepcopy(A)
  D = inter(A, B)
  for i in range(len(D.lista)):
    C.lista.remove(D.lista[i])
  return C

def uniao(A, B):
  #cria um conjunto C com todos os elementos de A e B
  C = ConjInt(A)
  C.lista.extend(B.lista)
  #elimina elementos repetidos
  D = inter(A, B)
  C = sub(C, D)
  C.lista.sort()
  return C

Conjunto = ConjInt(1.1)
A = ConjInt([1,2,3])
B = ConjInt([1,2.2,"a",[1],4,5,6,7,8,8,8,8,8,8,8,9,10,13,8,12,11,10,2])
C = ConjInt([1,2])

print "\nA, B, A^B, A U B"
A.printo()
B.printo()
inter(A,B).printo()
uniao(A,B).printo()
print "\nC, A-C, A^C, C-A"
C.printo()
sub(A,C).printo()
inter(A,C).printo()
sub(C,A).printo()

print A.lista, B.lista, Conjunto.lista, C.lista

#2.2: Dado um arquivo, o programa abaixo analisa-o e gera um relatorio com informacoes,
#	como numero de linhas, palavras, tags, tags errados e os tags da linha

class texto:

  def __init__(self,arquivo=""):
    self.lista=[]
    self.readfile(arquivo)
  
  def newfrase(self, sent):
    #insere uma frase no texto
    A = frase(sent)
    self.lista.append(A)
    
  def readfile(self, arquivo):
    #insere todas as frases do arquivo
    f = open(arquivo, "r")
    s = f.readline()
    while s:
      self.newfrase(s)
      s = f.readline() 
        
  def nro_frases(self):
    # nro de frases do texto
    return len(self.lista)
  
  def relatorio(self):
    #gera um arquivo result com o relatorio
    f = open("result", "w")
    for i in range(self.nro_frases()):
      s = "linha" + str(i+1) + " - " + self.lista[i].relatorio() + "\n"
      f.write(s)
    f.close()
    
class frase:
  
  def __init__(self, linha=''):
    self.listatags = [] #lista com tags
    self.erro = 0 # tags com erro
    self.linha = linha
    self.tags()
  
  def nro_word(self):
    #nro de palavras (espacos em branco + 1)
    return self.linha.count(" ") + 1
    
  def tags(self):
    #insere tags no atributo listatags da classe e conta tags com erros
    initag = 0
    for i in range(len(self.linha)):
      if self.linha[i] == '<':
        if initag:
	  self.erro+= 1
	initag = i+1  #i+1 pois se linha[0] = < , initag continua 0 e portanto naum reconhece tag
      if self.linha[i] == '>': 
        if initag: #tag definida corretamente
	  #insere tag na listatags
	  self.listatags.append(self.linha[initag-1 : i+1])
	  initag = 0
        else:
	  self.erro+= 1
	  
  def nro_tags(self):
    #nro de tags na frase
    return len(self.listatags)
        
  def relatorio(self):
    s = str(self.nro_word()) + " palavras - "
    if self.nro_tags():
      s += str(self.nro_tags()) + " tags" + str(self.listatags)
      s += " - " + str(self.erro) + " tags com problema"
    else:
      s += "frase sem tags"
    return s
    
#PROGRAMA TESTE DO 2.2

# ERRO 2 23

A = texto("teste.txt")
A.relatorio()
