## Lista de Exercicios de P.O.O.
## Classes

## Katsumi Arackawa Junior          N#3530185
## Jose Arnaldo M. de Holanda       N#3564502

############### Exercício 1 ###################

class c_int:
                              
    def __init__(self,*temp):
        self.lista=[]
        self.insere(temp)
## adicao de elemento na lista                    
    def adicao(self,elemento):
        if type(elemento) == int:
            if  elemento not in self.lista:
                self.lista.append(elemento)

        else:
            for n in elemento:
                if type(n) == int:
                   if n not in self.lista:
                        self.lista.append(n)
## elemento da lista
    def remocao(self, elemento):
        if elemento in self.lista :
            self.lista.remove(elemento)
        else :
            print "Elemento nao esta na lista"
## imprime item da lista
    def imprime(self):
        for item in self.lista:
            print item
## insere elemento
    def insere(self, temp):
        tam_list=len(temp)
        i=0
        while i<tam_list:
            if type(temp[i]) == int:
                self.adicao(temp[i])
            else :
                self.adicao(temp[i].lista)
            i+=1
##interseccao de lista1 e lista2 
    def interseccao (self, lista1, lista2):
        aux=[]
        for i in lista1:
            for j in lista2:
                if i == j:
                    aux.append(i)
        return aux
##juncao de duas listas
    def uniao (self, lista1, lista2):
        aux=[]
        for n in lista1:
                if type(n) == int:
                   if n not in aux:
                        aux.append(n)
        for n in lista2:
                if type(n) == int:
                   if n not in aux:
                        aux.append(n)
        return aux
##subtracao de lista, lista2
    def subtracao (self, lista1, lista2):
        aux=[]
        for n in lista1:
                if type(n) == int:
                   if n not in aux:
                        aux.append(n)
        for m in lista2:
                if type(m) == int:
                   if n in aux:
                        aux.remove(m)
        return aux
    
############### Exercício 2 ######################

## Classe que inicializa lista
class frases:

    def __init__(self,lista):
        
        self.lista = lista
        self.num_linhas = len(self.lista)

## Classe que conta o numero de palavras
class palavras:
	
    def __init__(self,lista):
        self.lista = lista
        self.cont_p = len(self.lista)
	for item in self.lista:
		for caracter in item:
			if caracter == ' ':
				self.cont_p += 1


			   
#classe que conta o numero de tags "<tag>" em um texto
#OBS: Ele nao admite tags dentro de tags <<tag>>
class tag:

    def __init__(self,lista):

        self.lista = lista
        flag = 0
        self.num_erro = 0
        self.num_acerto = 0
        tag = ''
	self.l_tag = ''
        
        for frase in self.lista:
            for caracter in frase:

                if caracter == '<':
                    if flag == 1:
                        self.num_erro += 1
                        flag = 1
                        tag = '<'   
			
                    else:
                        flag = 1
			tag = '<'

                elif caracter == '>':
                    if flag ==1:
                        self.num_acerto += 1
                        flag = 0
			tag = tag + '>'
 			self.l_tag = self.l_tag + ' ' + tag
                    else:
                        flag =0
                        self.num_erro += 1

		elif caracter == '\n' and flag == 1:
			flag =0
			tag = ''
			self.num_erro += 1
                    
                if flag == 1 and caracter != '<' and caracter != '>':
                    tag = tag + caracter

            
	
## Classe que abre um arquivo texto "texto.txt" e imprime um arquivo de saida "saida.txt
## Com o numero de tags corretas, incorretas, palavras e linhas 
class imprime:

	def __init__(self):
		arq_in  = open("texto.txt", 'r')
		arq_out = open("saida.txt", 'w')
		lista = arq_in.readlines()
		f = frases(lista)
		p = palavras(lista)
		t = tag(lista)

		arq_out.write('TOTALIZANDO:' '\n' '\n')
		arq_out.write(str(f.num_linhas) + ' linha(s)  --> ')
		arq_out.write(str(p.cont_p) + ' palavras; ')
		arq_out.write(str(t.num_acerto) +  ' tags corretas:'+ t.l_tag + '; ')
		arq_out.write(str(t.num_erro) + ' tags incorretas.' + '\n')		
    
    
i = imprime()
    
# ERRO 2 23

