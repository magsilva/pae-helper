Guilherme de A. Cordeiro 3456690
Jefferson O. Kuramoto    3529760

# ERRO 1 10
# ERRO 1 11
# ERRO 1 12
# ERRO 1 13
# ERRO 1 14

[2.1]
>>> class ConjuntoInteiros:
	def __init__(self, *inilist):
		self.lista = []
		for x in inilist[:]:
			if type(x) == type(0):
				self.insert(x)
			elif str(x.__class__) == str(self.__class__):
				for y in x.lista[:]:
					self.insert(y)
	def insert(self, param):
		if not(param in self.lista) and type(param) == type(0):
			self.lista = self.lista + [param]
>>> a = ConjuntoInteiros(0,1.0,2,"3",4)
>>> a.lista
[0, 2, 4]
>>> b = ConjuntoInteiros(a,1,3,5,5,2)
>>> b.lista
[0, 2, 4, 1, 3, 5]
>>> b.insert(111)
>>> b.lista
[0, 2, 4, 1, 3, 5, 111]
>>> b.insert(a)
>>> b.lista
[0, 2, 4, 1, 3, 5, 111]
>>> b.insert("qwerty")
>>> b.lista
[0, 2, 4, 1, 3, 5, 111]








[2.2]
>>> class Palavra:
	def __init__(self):
		self.reset()

	def reset(self):
		self.num  = 0 # numero de palavras
		self.flag = 0 # flag de controle

	def num_up(self):
		self.num = self.num+1

	def flag_up(self):
		self.flag = 1

	def flag_down(self):
		self.flag = 0

	def flagged(self):
		return self.flag

	def FinalCount(self):
		return self.num

	
>>> class Tag(Palavra):
	def reset(self):
		self.num     = 0 # numero de tags corretas
		self.prob    = 0 # numero de tags-problema
		self.flag    = 0 # flag de controle
		self.CurrTag = "" # buffer que guarda a tag analizada atualmente
		self.lista   = " " # lista de tags corretas ja analizadas

	def prob_up(self):
		self.prob = self.prob+1

	def new_tag(self):
		self.CurrTag = ""

	def push(self, ch):
		self.CurrTag = self.CurrTag + ch

	def flush(self):
		self.lista = self.lista + '<' + self.CurrTag + '> '

	def ProbCount(self):
		return self.prob


>>> class Frase:
	def __init__(self):
		self.linha = "" # string com a linha atual
		self.num = 0 # numero de frases
	def push(self, ch):
		self.linha = ch
	def access(self, i):
		return self.linha[i]
	def show_line(self):
		p = self.linha
		return p
	def count_up(self):
		self.num = self.num+1
	def FinalCount(self):
		return self.num
	

>>> def TagAnalizer():
	
	arq = raw_input('De o nome do arquivo de entrada: ')
	try:
		f = open (arq, "r")
		arqsai = raw_input('De o nome do arquivo de saida: ')
		g = open (arqsai, "w")

		print "\n<Arquivo de saida criado com sucesso!>\n"

		cp = Palavra()
		ct = Tag()
		fr = Frase()
		
		fr.push(f.readline())
		while fr.show_line(): 
			fr.count_up()
			i   = 0
			tam = len(fr.show_line())
			cp.reset()
			ct.reset()

			while (i < tam):
				
				if (fr.access(i) == '<'):
					if ct.flagged():
						ct.prob_up()
						ct.new_tag()
					else:
						ct.flag_up()
						ct.new_tag()
						
				elif (fr.access(i) == ' ' or fr.access(i) == '\n'):
					if cp.flagged():
						cp.flag_down()
				elif (fr.access(i) == '>'):
					if ct.flagged():
						ct.flush()
						ct.num_up()
						ct.new_tag()
						ct.flag_down()
					else:
						ct.prob_up()
				else:
					if not(cp.flagged()):
						cp.flag_up()
						cp.num_up()
					if ct.flagged():
						ct.push(fr.access(i)) 
					
				i = i+1

			print "- linha %d -" % (fr.FinalCount()) 
			print fr.show_line() 
			print "%d palavras" % (cp.FinalCount())
			print "%d tags (%s)" % (ct.FinalCount(), ct.lista) 
			print "%d tags-problema\n" % (ct.ProbCount())

			print >>g, "- linha %d -" % (fr.FinalCount())
			print >>g, fr.show_line()
			print >>g, "%d palavras" % (cp.FinalCount())
			print >>g, "%d tags (%s)" % (ct.FinalCount(), ct.lista) 
			print >>g, "%d tags-problema\n" % (ct.ProbCount())
									
			fr.push(f.readline())
			
		f.close()
		g.close()

	except:
		print 'Impossivel localizar o arquivo', arq



>>> TagAnalizer()
De o nome do arquivo de entrada: a:/test.txt
De o nome do arquivo de saida: a:/testsai.txt

<Arquivo de saida criado com sucesso!>

- linha 1 -
Teste de uso de <TAGS> em POO

7 palavras
1 tags ( <TAGS> )
0 tags-problema

- linha 2 -
e processamento de <problemas com <mau> uso <de> tags?
9 palavras
2 tags ( <mau> <de> )
1 tags-problema


>>> TagAnalizer()
De o nome do arquivo de entrada: a:/test2.txt
De o nome do arquivo de saida: a:/test2sai.txt

<Arquivo de saida criado com sucesso!>

- linha 1 -
Este <programa> executou uma <<opera>cao ilegal> e sera fechado
9 palavras
2 tags ( <programa> <opera> )
2 tags-problema

# ERRO 2 23
