Nome: Alexandra Kelli Barbato    nº USP: 3459053 
Nome: Ottone Alexandre Traldi    nº USP: 3457749
Nome: Marcos Fabio Martins       nº USP: 3458100

# ERRO 1 4

2.1
class conjuntointeiro:
	def __init__(self,*x):
		self.lista = []
		qtdi = x.__len__()
		i = 0
		while ( i < qtdi):
		if type(x[i]) is type(0) and self.lista.count(x[i]) == 0:
				self.lista.append(x[i])
			elif type(x[i]) is type(self):
				qtdj = x[i].lista.__len__()
		            j = 0
		            while ( j < qtdj):
if type(x[i].lista[j]) is type(0) and self.lista.count(x[i].lista[j]) == 0:
self.lista.append(x[i].lista[j])
		                  j = j + 1
 			i = i + 1

	def adiciona(self, *x):
		qtd = x.__len__()
          	i = 0
            while ( i < qtd):
if type(x[i]) is type(0) and self.lista.count(x[i]) == 0:
                  	self.lista.append(x[i])
                  i = i + 1

	def subtrai(self, num):
		if num in self.lista:
			self.lista.remove(num)

	def imprime(self):
		print self.lista

	def uniao(self, x):
		qtd = x.lista.__len__()
            i = 0
            while ( i < qtd):
if type(x.lista[i]) is type(0) and self.lista.count(x.lista[i]) == 0:
                  	self.lista.append(x.lista[i])
                  i = i + 1

	def inter(self,x,y):
		self.lista = []
		qtdx = x.lista.__len__()
		qtdy = y.lista.__len__()
		i = 0
		if qtdy < qtdx:	
            	while ( i < qtdx):
                  	if y.lista.count(x.lista[i]) <> 0:
                        	self.lista.append(x.lista[i])
            		i = i + 1 
            else:
            	while ( i < qtdy):
                  	if x.lista.count(y.lista[i]) <> 0:
                        	self.lista.append(y.lista[i])
                        i = i + 1

	def subtracao(self, x):
		qtd = x.lista.__len__()
		i = 0
		while (i < qtd):
			if self.lista.count(x.lista[i]) <> 0:
				self.lista.remove(x.lista[i])
			i = i + 1 	

print "***************************"
a = conjuntointeiro(1,2,3,4,5)
b = conjuntointeiro(11,12,13,5,'a','b','c')
c = conjuntointeiro(a,1,2)
print "a"
a.imprime()
print "b"
b.imprime()
print "c"
c.imprime()
a.adiciona(3,4,5,6,7,8,9,10)
print "a + alguns elementos "
a.imprime()
a.subtrai(7)
print "a - 7"
a.imprime()
a.uniao(b)
print "a + b:"
a.imprime()
c.inter(a,b)
print "a * b:"
c.imprime()
b.subtracao(a)
print "b - a"
b.imprime()
a.subtracao(b)
print "a - b"
a.imprime()









# ERRO 2 23

2.2
class tag:
    def __init__(self,palavras):
        self.tags = []
        j = 0
        while j < palavras.__len__():
if (palavras[j][0] == '<' and palavras[j][palavras[j].__len__() - 1] == '>'):
                self.tags.append(palavras[j])
            j = j+1

    def problema (self, palavras = []):
        count = 0
        j = 0
        while j < palavras.__len__():
if (palavras[j][0] == '<' and palavras[j][palavras[j].__len__() - 1] <> '>') or (palavras[j][0] <> '<' and palavras[j][palavras[j].__len__() - 1] == '>'):
            	count = count + 1
            j = j + 1
        return count    

class frase:
    def __init__(self,conteudo):
        self.frases = conteudo.split('\n')

class palavra:
    def __init__(self, frase):
        self.palavras = frase.split(' ')


arq = file("z:/poo/entradapoo.txt",'r')
print '*******************************'
f = frase(arq.read())
arq.close()
i = 0
qtd = f.frases.__len__()
arqout = file ("z:/poo/saidapoo.txt",'w')
while (i < qtd):
    p = palavra(f.frases[i])
    arqout.write('linha ' + str(i+1) + ' - ')
    arqout.write(str(p.palavras.__len__()))
    arqout.write(' palavras - ')
    t = tag(p.palavras)
    arqout.write(str(t.tags.__len__()) + ' tags' + '(')
    j = 0
    while j < t.tags.__len__():
        arqout.write(t.tags[j] + ' ')
        j = j+1
    arqout.write(') - ' + str(t.problema(p.palavras)) + ' tags-problema\n')
    i = i+1
arqout.close()


