Alunos
Marco Aurelio Rescia Alher 3560481
Santiago de Moura Luz      3560495


Lista de Exercicios 2

2 Classes

2.1

# ERRO 1 5
# ERRO 1 6
# ERRO 1 7

class ci:

    def __init__(self):
        self.lista = []

    def cria(self, listaa):
        n = len(listaa)
        pode = 1
        while n >= 0:
            if type(listaa[n-1]) != int:
                pode = 0
            if listaa.count(listaa[n-1]) != 1:
                pode = 0
            n -= 1
        if pode:
            self.lista = listaa
            return 1
        else:
            return 0
    
    def adic(self, elemento):
        k=0
        jaexiste=0
        tamanho=len(self.lista)
        while k < tamanho:
            if self.lista[k]==elemento:
                jaexiste=1
            k+=1
        if jaexiste==0:
            self.lista.append(elemento)
            return 1
        else:
            return 0

    def rem(self, elemento):
        n = len(self.lista)
        existe = 0
        while n >= 0:
            if self.lista[n-1] == elemento:
                existe = 1
            n -= 1
        if existe:
            self.lista.remove(elemento)
            return 1
        else:
            return 0
        
    def impr(self):
        print(self.lista)

    def uniao(self, lista2):
        n = len(lista2)
        pode = 1
        while n >= 0:
            if type(lista2[n-1]) != int:
                pode = 0
            if lista2.count(lista2[n-1]) != 1:
                pode = 0
            if self.lista.count(lista2[n-1]) > 0:
                 pode = 0
            n -= 1
        if pode:
            self.lista.extend(lista2)
            return 1
        else:
            return 0        
    def interseccao(self, lista2):
        n = len(lista2)
        pode = 1
        lista3 = []
        while n >= 0:
            if type(lista2[n-1]) != int:
                pode = 0
            if lista2.count(lista2[n-1]) != 1:
                pode = 0
            if self.lista.count(lista2[n-1]) > 0:
                lista3.append(lista2[n-1])
            n -= 1
        if pode:
            self.lista = lista3
            return 1
        else:
            return 0  

    def subtracao(self, lista2):
        n = len(lista2)
        pode = 1
        lista3 = self.lista
        while n >= 0:
            if type(lista2[n-1]) != int:
                pode = 0
            if lista2.count(lista2[n-1]) != 1:
                pode = 0
            if self.lista.count(lista2[n-1]) > 0:
                lista3.remove(lista2[n-1])
            n -= 1
        if pode:
            self.lista = lista3
            return 1
        else:
            return 0         


Exercicio 2.2 (trabalhando com arquivos)


"Abrindo o arquivo"
arq = open("/home/alher/frase.txt")
"Criando o novo arquivo"
narq = open("/home/alher/novo.txt","w")

#****************************************************************************************************************			

class frase:
	def __init__(self):
                
                np=0
		nl=0
		k=0		
				
                linha = arq.readlines()

		#numero de linhas no texto
		nl=len(linha)		
			
		#numero de tags no texto tags.listag[k]
		tags = tag(linha,nl)
	
		#numero de palavras	 pal.lpal[k]
		pal = palavra(linha,nl)
		
		k=0
		while k < nl:
			texto = pal.lpal[k] + " - " + tags.listag[k] + "\n"
			narq.write(texto)
			k+=1

		#fecha arquivo
		narq.close()
		arq.close()

#****************************************************************************************************************			
class palavra:
	def __init__(self,linha,nl):

		self.linha = linha
		self.nl = nl
		self.lpal=[]
		
		k=0
		np=0
		frase=""

		while k < self.nl:
			np = self.linha[k].count(" ")
			frase = "Linha " + str(k+1) + " : " + str(np+1) + " palavras"
		       	self.lpal.append(frase)  
		        k=k+1
			


#****************************************************************************************************************			

class tag:
	def __init__(self,linha,nl):

		self.linha = linha
		self.nl = nl
        	self.listag=[]
		
		k=0
		ntag1=0
		ntag2=0
		menor=0
		maior=0
		meio=0
		frase=""

		while k < self.nl:
			ntag1 = self.linha[k].count("<")
			ntag2 = self.linha[k].count(">")
			if ntag1==ntag2:
				self.listag.append("%d tag(s) correta(s)" %ntag1)
			else:

				if ntag1>ntag2:
					menor=ntag2
					maior=ntag1
				else:	
					menor=ntag1
					maior=ntag2

				meio=maior-menor
  				frase = str(menor) + " tag(s) corretas e " + str(maior-menor) + " tag(s) errada(s)"
				self.listag.append(frase)  
			ntag1=0
			ntag2=0
			k=k+1

# ERRO 2 23
