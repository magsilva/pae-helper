class Palavra:
	def __init__ (self, word):
		self.word = word.lower()

	def change_gen(self):
		tam = len(self.word) - 1
		if   self.word[tam-2:] == 'mas':
			self.word = self.word[:tam-2] + 'ns'
	        elif self.word[tam-1:] == 'ns':
			self.word = self.word[:tam-1] + 'mas'
	        elif self.word[tam-1:] == 'os':
			self.word = self.word[:tam-1] + 'as'
	        elif self.word[tam-1:] == 'as':
			self.word = self.word[:tam-1] + 'os'
	        elif self.word[tam-1:] == 'm':
			self.word = self.word[:tam-1] + 'ma'
	        elif self.word[tam-1:] == 'ma':
			self.word = self.word[:tam-1] + 'm'
		elif self.word[tam:] == 'o':
			self.word = self.word[:tam] + 'a'
	        elif self.word[tam:] == 'a':
			self.word = self.word[:tam] + 'o'

	def change_num(self):
		tam = len(self.word) - 1
	        if   self.word[tam] == 'o' or self.word[tam] == 'a':
			self.word = self.word + 's'
	        elif self.word[tam] == 's':
			self.word = self.word[:tam]
			if self.word[tam-1] == 'n':
				self.word = self.word[:tam-1] + 'm'
		elif self.word[tam] == 'm':
			self.word = self.word[:tam] + 'ns'

	def get_word(self):
		return self.word
	             
class Artigo_Definido(Palavra):
	def gera_ad(self, info):
		self.word == 'o'
		if info[0] == 'f':
			self.word = 'a'
		if info[1] == 'p':
			self.word += 's'

class Artigo_Indefinido(Palavra):
	def gera_ai(self, info):
		if   info == 'ms':
			self.word = 'um'
		elif info == 'mp':
			self.word = 'uns'
		elif info == 'fs':
			self.word = 'uma'
		else:
			self.word = 'umas'
	
class Substantivo(Palavra):
	def __init__ (self, word):
		self.word = word.lower()
		
	def get_info(self):
	        tam = len(self.word) - 1
	        if   self.word[tam] == 'o':
			inf = 'ms'
	        elif self.word[tam] == 'a':
			inf = 'fs'
	        elif self.word[tam] == 's':
			tam -= 1
			if   self.word[tam] == 'o':
		                inf = 'mp'
			else:
		                inf = 'fp'
	        return inf
	
class Verbo_1_Conj(Palavra):
	def __init__ (self, word):
	        tam = len(word) - 1
	        self.word = word[:tam]

	def change_num (self):
	        tam = len(self.word) - 1
	        if self.word[tam] == 'm':
			self.word = self.word[:tam]
	        else:
			self.word = self.word + 'm'

	def change_gen(self):
		a = 5
	
class Verbo_2_Conj(Palavra):
	def __init__ (self, word):
	        tam = len(word) - 1
	        self.word = word[:tam]

	def change_num (self):
	        tam = len(self.word) - 1
	        if self.word[tam] == 'm':
			self.word = self.word[:tam]
	        else:
			self.word = self.word + 'm'
	            
class Verbo_3_Conj(Palavra):
	def __init__ (self, word):
	        tam = len(word) - 2
	        self.word = word[:tam] + 'e'

	def change_num (self):
	        tam = len(self.word) - 1
	        if self.word[tam] == 'm':
			self.word = self.word[:tam]
	        else:
			self.word = self.word + 'm'
	            
class Frase:
	def __init__ (self, sub1, verb, sub2):
	        self.sub1 = Substantivo(sub1)
	        self.sub2 = Substantivo(sub2)
	        i = self.sub1.get_info()
	        j = self.sub2.get_info()
		self.art1 = Artigo_Definido('o')
	        self.art1.gera_ad(i)
	        self.art2 = Artigo_Definido('o')
	        self.art2.gera_ad(j)
		tam = len(verb) - 2
		if   verb[tam:] == 'ar':
			self.verb = Verbo_1_Conj(verb)
		elif verb[tam:] == 'er':
			self.verb = Verbo_2_Conj(verb)
		elif verb[tam:] == 'ir':
			self.verb = Verbo_3_Conj(verb)
		if i[1] == 'p':
			self.verb.change_num()
		
	def change_gen(self):
	        self.art1.change_gen()
	        self.art2.change_gen()
	        self.sub1.change_gen()
	        self.sub2.change_gen()

	def change_num(self):
	        self.art1.change_num()
	        self.art2.change_num()
	        self.sub1.change_num()
	        self.sub2.change_num()
	        self.verb.change_num()

	def change_to_def(self, sub1, sub2):
	        self.art1 = Artigo_Definido()
	        self.art1.gera_ad(sub1)
	        self.art2 = Artigo_Definido()
	        self.art2.gera_ad(sub2)
	        
	def change_to_indef(self, sub1, sub2):
	        self.art1 = Artigo_Indefinido()
	        self.art1.gera_ai(sub1)
	        self.art2 = Artigo_Indefinido()
	        self.art2.gera_ai(sub2)

	def show_frase(self):
	        aux = self.art1.get_word() + ' ' + self.sub1.get_word() + ' ' + self.verb.get_word() + ' ' + self.art2.get_word() + ' ' + self.sub2.get_word() + '.'
	        return aux.capitalize()

def Exe():
	filename = raw_input('Nome do arquivo: ')
#	try:
	f = open ( filename, "r")
        linha = f.readline()
        while linha:
		x = 0
		s1 = ''
		s2 = ''
		v  = ''
		while linha[x] <> ' ':
			s1 += linha[x]
			x  += 1
		x += 1
		while linha[x] <> ' ':
	                v  += linha[x]
	                x  += 1
		x += 1
	        while linha[x] <> '\n':
		        s2 += linha[x]
	                x  += 1
	        frase = Frase(s1,v,s2)
	        print frase.show_frase()
	        frase.change_gen()
	        print frase.show_frase()
	        frase.change_num()
		print frase.show_frase()
	        frase.change_gen()
	        print frase.show_frase()
	        frase.change_gen()
	        print frase.show_frase()
		frase.change_num()
	        print frase.show_frase()
	        frase.change_gen()
	        print frase.show_frase()
	        linha = f.readline()
	f.close()
#	except:
#	        print 'Arquivo inexistente'


Exe()

# Programa não funciona
# ERRO 1 4 100
# ERRO 1 5 100
# ERRO 1 6 100
# ERRO 1 7 100

# ERRO 1 8 100
# ERRO 1 11 50
# ERRO 1 14 25
# ERRO 1 15 50
