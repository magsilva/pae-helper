Alecio Elias Vitiello
Maikel Thiago Favarin Jacob

CONTINUAÇÃO DA LISTA 2 DE EXERCÍCIOS

# ERRO TOTAL 1.1: Não foi feito.

# ERRO TOTAL 1.2: Não foi feito.

1.3)
def isBeetween(x,y,z):
	if (y<=x) and (x<=z):
        	return 1
    	else:
		return 0

1.4)
def inversa(palavra):
	for i in range(1,len(palavra)+1): 
      		print palavra[-i]

1.5)
def ocorrencia(palavra,letra):
	n=0
	for i in range(0,len(palavra)):
		if palavra[i] == letra:
        		n = n+1
	return n

1.6)
def ocorrencia2(frase,palavra):
	auxiliar=0
	contador=0
	for i in range(0,len(frase)-len(palavra)):
        	for k in range(0,len(palavra)-1):
            		if frase[i+k] == palavra[i+k]:
                		auxiliar = 0
            		else:
				auxiliar = 1
        		if auxiliar == 0:
	            		contador = contador + 1
    	return contador

# ERRO TOTAL 1.6: Código dá erro quando executado.

1.7)
def funcao():
	for i in range(1000,9999):
        	numstring = str(i)
        	dezena1str[0] = numstring[0]
        	dezena1str[1] = numstring[1]
        	dezena2str[0] = numstring[2]
        	dezena2str[1] = numstring[3]
        	dezena1num = int(dezena1str)
       		dezena2num = int (dezena2str)
       		if sqrt(i) = dezena1num + dezena2num:
            		print i


# ERRO TOTAL 1.7: Código dá erro de sintaxe quando executado.

1.8)
def subnumeros(p,q):
	pstr = str(p)
	qstr = str(q)
	auxiliar = 0
	for i in range(0,len(qstr)-1):
		for k in range(0,len(pstr)-1):
			if qstr(i+k) == pstr(i+k):
				auxiliar = 0
			else:
				auxiliar = -1
			if auxiliar = 0:
            			print "p é subnumero de q"

# ERRO TOTAL 1.8: Código dá erro de sintaxe quando executado.

# ERRO TOTAL 1.9: Exercício não foi feito.
