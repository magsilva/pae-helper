#!/usr/bin/python
from __future__ import division;
import string;


class palavra:
	def __init__(self, pala):
		self.pal = string.lower(pala);

class artigo(palavra):
	def __init__(self, pala):
		palavra.__init__(self, pala);

	def numero(self):
		if (self.pal[0] == "u"):      #indefinido
			if (self.pal[-1] == "a"):
				return self.pal + "s";
			return self.pal[:-1] + "ns";
		else:
			return self.pal + "s";

	def genero(self):
		if (self.pal == "uma" ):
			return self.pal[:-1];
		else:
			if (self.pal[-1] == "o"):
				return self.pal[:-1] + "a";
			else:
				return self.pal[:-1] + "o";

class substantivo(palavra):
	def __init__(self, pala):
		palavra.__init__(self, pala);
	def numero(self):
		if (self.pal[-1] == "l"):
			return self.pal[:-1] + "is";
		else:
			return self.pal + "s";
	def genero (self):
		if (self.pal[-1] == "a"):
			return self.pal[:-1] + "o";
		else:
			return self.pal[:-1] + "a";

class verbo(palavra):
	def __init__(self, pala):
		palavra.__init__(self, pala);
	def genero(self):
		return self.pal;
	def numero(self):
		if (self.pal[-1:] == "e"):
			return self.pal + "m";
		if (self.pal[-1:] == "i"):
			return self.pal[:-1] + "em";
		if (self.pal[-1:] == "a"):
			return self.pal + "m";

		

def handle(linha):
	sequencia = linha.split();
	if (len(sequencia) == 5):
		art = artigo(sequencia[0]);
		sub = substantivo(sequencia[1]);
		ver = verbo(sequencia[2]);
		art2 = artigo(sequencia[3]);
		sub2 = substantivo(sequencia[4]);
		print string.capitalize(art.numero()+ " "  + sub.numero() + " " + ver.numero() + " " + art2.numero() + " " + sub2.numero());
		print string.capitalize(art.genero()+ " "  + sub.genero() + " " + ver.genero() + " " + art2.genero() + " " + sub2.genero());
		print linha;
	else: 
		raise ErroArquivo;
	

f = open("texto.txt","r");
linha = "null";
while (linha):
	linha = f.readline();
	try:
		handle(linha);
	except:
		print "";

# ERRO 1 11 50
# ERRO 1 12 100
# ERRO 1 14 50
# ERRO 1 15 100
