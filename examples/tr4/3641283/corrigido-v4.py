class Frase:
  def __init__(self, word=""):
    self.oracao = []
    self.oracao.append( Artigo(word[0:word.find(" ")]) )
    word = word[word.find(" ")+1 : len(word)]
    self.oracao.append( Substantivo(word[0:word.find(" ")]) )
    word = word[word.find(" ")+1 : len(word)]
    self.oracao.append( Verbo(word[0:word.find(" ")]) )
    word = word[word.find(" ")+1 : len(word)]
    self.oracao.append( Artigo(word[0:word.find(" ")]) )
    word = word[word.find(" ")+1 : len(word)]
    self.oracao.append( Substantivo(word) )

  def AlterGen(self):
    aux = []
    for i in self.oracao:
      i.AlterGen()
      aux.append(i) 
    self.oracao = aux    

  def AlterNum(self):
    aux = []
    for i in self.oracao:
      i.AlterNum()
      aux.append(i) 
    self.oracao = aux    
    
  def printo(self):
    s = ""
    for i in self.oracao:
      s += i.printo() 
    print s

class Palavra(Frase):
  "Algo definido como palavra!"
  def __init__(self,word):
    self.word = str(word)
    self.genero = self.detgenero()
    self.numero = self.detnumero()

  def printo(self):
    return self.word + " "
  
  def detnumero(self):
    if self.word[len(self.word)-1] == "s":
      return 1  #plural
    else:
      return 0  #singular

  def detgenero(self):
    if self.word[len(self.word)-1] == "a":
      return 1  #feminino
    else:
      return 0  #masculino
      
  def AlterGen(self):
    if self.genero:
      self.Masc()
    else:
      self.Fem()
    self.genero = not(self.genero)
  
  def AlterNum(self):
    if self.numero:
      self.Singular()
    else:
      self.Plural()
    self.numero = not(self.numero)

  def Masc(self):
    if self.word[len(self.word)-1] == "s":
      self.word = self.word[0 : len(self.word)-2] + "os"
    else:
      self.word = self.word[0 : len(self.word)-1] + "o"

  def Fem(self):
    if self.word[len(self.word)-1] == "s":
      self.word = self.word[0 : len(self.word)-2] + "as"
    else:
      self.word = self.word[0 : len(self.word)-1] + "a"      
      
  def Plural(self):
    if self.word[len(self.word)-1] == "m":
      self.word = self.word[0 : len(self.word)-1] + "ns"
    else:
      if self.word[len(self.word)-1] == "l":
        self.word = self.word[0 : len(self.word)-2] + "'eis"
      else: 
        self.word = self.word + "s"    
	
  def Singular(self):
    if self.word[len(self.word)-2: len(self.word)] == "ns":
      self.word = self.word[0 : len(self.word)-2] + "m"
    else:
      if self.word[len(self.word)-3: len(self.word)] == "eis":
        self.word = self.word[0 : len(self.word)-3] + "'el"
      else: 
        self.word = self.word[0:len(self.word)-1]    


class Artigo(Palavra):
  pass   
class ArtigoDef(Artigo):
  pass
  
class ArtigoIndef(Artigo):
  pass
  

class Substantivo(Palavra):
  pass  

class Verbo(Palavra):
  
  def detnumero(self):
    if self.word[len(self.word)-1] == "m":
      return 1  #plural
    else:
      return 0  #singular
  
  def detgenero(self):
    pass

  def Plural(self):
    #Altera o genero do verbo para concordar com o plural
    self.word += "m"
 
  def Singular(self):
    #Altera o genero do verbo para concordar com o singular
    self.word = self.word[0:len(self.word) - 1]
  
  def AlterGen(self):
    pass
    
class Conj1(Verbo):
  pass
class Conj2(Verbo):
  pass
class Conj3(Verbo):
  pass

a = Frase("O rato esconde a rata")
a.printo()
a.AlterGen()
a.printo()
a.AlterNum()
a.printo()
a.AlterGen()
a.printo()
a.AlterNum()
a.printo()

# ERRO 1 12 100
# ERRO 1 14 15
# ERRO 1 15 15
