import string

class Frase:
	frase = [];
	def __init__(self, string):
		strings = string.lower().split(' ')
		if len(strings) <> 5:
			print "erro: frase mal-composta"
			return
		self.frase.append(Artigo(strings.pop(0)))
		self.frase.append(Substantivo(strings.pop(0)))
		self.frase.append(Verbo(strings.pop(0)))
		self.frase.append(Artigo(strings.pop(0)))
		self.frase.append(Substantivo(strings.pop(0)))

	def show(self):
		for word in self.frase:
			word.show()
		print

	def muda_genero(self):
		for word in self.frase:
			word.muda_genero()

	def muda_numero(self):
		for word in self.frase:
			word.muda_numero()

class Palavra(Frase):
	genero = 0
	numero = 0
	def __init__(self, word):
		self.word = word

	def show(self):
		print str(self.word),

	def numgen(self):
		word = self.word.lower()
		if word[-1] == 's':
			self.numero = 1
		if len(word) >= 2:
			penultima = -2
		else:
			penultima = -1
		if word[-1] == 'a' or word[penultima] == 'a':
			self.genero = 1

	def chgen(self):
		if self.genero:
			self.genero = 0
			return 1
		else:
			self.genero = 1
			return 0

	def chnum(self):
		if self.numero:
			self.numero = 0
			return 1
		else:
			self.numero = 1
			return 0

class Artigo(Palavra):
	def __init__(self, word):
		Palavra.__init__(self, word)
		self.numgen()

	def muda_genero(self):
		if self.chgen():
			if self.word == 'uma':
				self.word = 'um'
			else:
				self.word = string.replace(self.word, 'a', 'o')
		else:
			self.word = string.replace(self.word, 'o', 'a')
			if string.count(self.word, 'a') == 0:
				self.word += 'a'

	def muda_numero(self):
		if self.chnum():
			if self.word == 'uns':
				self.word = 'um'
			else:
				self.word = self.word[0:-1]
		else:
			if self.word == 'um':
				self.word = 'uns'
			else:
				self.word += 's'

class Substantivo(Palavra):
	def __init__(self, word):
		Palavra.__init__(self, word)
		self.numgen()

	def muda_genero(self):
		self.word = self.word[0:-1]
		if self.chgen():
			self.word += 'o'
		else:
			self.word += 'a'

	def muda_numero(self):
		if self.chnum():
			self.word = self.word[0:-1]
		else:
			self.word += 's'

class Verbo(Palavra):
	def __init__(self, word):
		Palavra.__init__(self, word)

	def muda_genero(self):
		return

	def muda_numero(self):
		if self.chnum():
			self.word = self.word[0:-1]
		else:
			self.word += 'm'


a = Frase("um bobo nutre uma gata")
a.muda_genero()
a.muda_numero()
a.show()

# ERRO 1 2 100
# ERRO 1 12 100
# ERRO 1 14 50
