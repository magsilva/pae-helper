# Alunos :
       Alessandro G. Krempi
       Jonatas Kerr


construtor :  Chamado quando uma instacia é criada. Seus argumnetos são passados para a expressão  construtora da        classe.                                                                                                                                                                 sintaxe : __init__(self[, ...]) 

 destrutor : Chamado quando a instancia esta sendo destruída.
                  Python mantem um contador para cada referencia a uma instancia. Quando este contador se torna zero __del__()
                  é chamado.


# ERRO PARCIAL 1 7
# ERRO TOTAL 1 8

Os atributos e metodos de uma classe são acessados usando o operados ponto(.)

# ERRO PARCIAL 1 9
1. Objetos e Classes
       2. Comunicação com Mensagens

# ERRO TOTAL 1 10
# ERRO TOTAL 1 3
# ERRO TOTAL 1 1
# ERRO TOTAL 1 2

# exercicio 2  e  3 (juntos)
# Alunos :
# Alessndro G. Krempi
# Jonatas Kerr

# ERRO PARCIAL 2 3

class Palavras :
   
  def __init__(self,strg = ''):
     
     print "digite uma palavra ou sentenca :"
     self.strg = raw_input() 

# ERRO TOTAL 2 4

  def conta_char(self):             # Conta o numero de caracteres de uma palavra ou instancia
       a = ''                       # Juncao
       c = []                       # todos os caracteres da sentenca exceto espaco em branco
       A = []                       # todas as palavras da sentenca
       M = []                       # todos os tamanhos encontrados
       y = 0
       for i in range(len(self.strg)):
	if self.strg[i]<> ' ' :     # se nao for espaco em branco coloca em c
		c.append(self.strg[i])
	if (self.strg[i]==' ') or  (i ==len(self.strg)-1):# espaco em branco ou fim da sentenca
		A.append(a.join(c)) # forma cada palavra da sentenca
		c = []
       for i in range(len(A)) :
         x = len(A[i])
         M.append(x)                # Tamanhos obtidos 
       while len(M) <> 0:
         y = M[0]
         print "%d Palavra(s) com %d letra(s)" %(M.count(y),y)# imprime numero e qte de palavras
         while y in M :
           M.remove(y)             # remove todos do mesmo tipo
          
  def conta_o_char(self,sub):      #Conta numero de ocorrencias de um caractere
     return self.strg.count(sub)



print "crie uma instancia da Classe Palavras "
#exercicio 4

# Alunos :
# Alessndro G. Krempi
# Jonatas Kerr

class sentenca:

    T1 = ['a','o','um','uma']                        #Artigos
    T2 = ['gata','cao','cidade','carro']             #Substantivos
    T3 = ['andou','correu','pulou','caiu']           #Verbo
    T4 = ['de','sobre','sob','embaixo']              #Preposicao

    def gerador(self,seed=0):                        #Gera uma sequencia aleatoria de palavras
        for x in range(20):                          # 20 sentencas
            ind = []                                 #Indices aleatorios
            A = []                                   #Sentenca concatenada
            a = ' '                                  #Juncao
            s = ['','','','','','']                  #Srtrings da sentenca
            from random import Random
            h = Random()                             
	    seed = h.randint(0,1000)                 #Semente Randomica
	    g = Random(seed)
	    for i in range(6):
		  x = g.randint(0,3)                 #Indice randomico
		  g.jumpahead(10)
		  ind.append(x)
	    s = [T1[ind[0]],T2[ind[1]],T3[ind[2]],T4[ind[3]],T1[ind[4]],T2[ind[5]]] #Strings da sentenca
	    A.append(a.join(s))                      #Sentenca concatenada em A
	    print A[0].capitalize() + '.'            #Primeira Maiuscula e ponto final

# ERRO TOTAL 4 8

print 'crie uma instancia da Classe sentenca :'
