1.1
	def comparar (x,y):
	if x>y:
		return 1
	elif x==y:
		return 0
	else: return -1

1.2
import math

def princ():
    x1 = float (raw_input("Digite x1:"))
    y1 = float (raw_input("Digite y1:"))
    x2 = float (raw_input("Digite x2:"))
    y2 = float (raw_input("Digite y2:"))
    result = distancia(x1,y1,x2,y2)
    return result

def distancia(x1,y1,x2,y2):
    dx = x2-x1
    dy = y2-y1
    dsquared = dx**2 + dy**2
    result = math.sqrt(dsquared)
    return result
1.3
	def Between(x,y,z):
    if (x<=z)and (y<=z):
       	    	return 1
    else: return 0

1.4
def fibonacci(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def imprime(n):
    result=[]
    for x in range(1,n):
        result = [result,fibonacci(x)]
        print result

OBS: o resultado aparece com excesso de colchetes

# ERRO PARCIAL 1.4: Não imprime quando n = 0 e 1.

1.5
def imprime():
    str = raw_input('Digite a frase:')
    x = len(str)
    x=x-1
    while x >=0:
        print str[x]
        x = x-1

1.6
def contagem():
    str = raw_input('digite a frase:')
    caracter = raw_input('digite o caracter que se deseja        procurar:')
    y = len(str)
    vezes = 0
    for cont in range(0,y):
        if (caracter==str[cont]):
            vezes = vezes+1
    print (vezes)

1.7
def contagem(): 
    frase = raw_input("Digite uma frase: ")
    palavra = raw_input("Digite a palavra desejada: ") 
    y = len(frase) - 1 
    cont = 0 
    for x in range(0,y): 
        if frase.startswith(palavra,x): 
            cont += 1
    return cont
# ERRO PARCIAL 1.7: Não conta corretamente se a palavra for ""

1.8
def dezoito(): 
     for num in range(1000,9999): 
          n = str(num) 
          x = n[0] 
          y = n[1] 
          z = n[2] 
          w = n[3] 
          xy = (int(x) * 10) + int(y) 
          zw = (int(z) * 10) + int(w)
          ab = xy + zw 
          xysquared = ab ** 2 
           if xysquared == num: 
              print num

# ERRO TOTAL 1.9: Não foi feito.
