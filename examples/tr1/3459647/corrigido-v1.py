import math

#------------------------------------------------------
#exemplo de chamada: compare(5,4)

def compare(x,y):
    if x > y:
        return 1
    elif x == y:
        return 0
    else:
        return -1

#----------------------------------------------
#exemplo de chamada: distancia()

def distancia():
    x1 = int(raw_input('Digite x1: '))
    y1 = int(raw_input('Digite y1: '))
    x2 = int(raw_input('Digite x2: '))
    y2 = int(raw_input('Digite y2: '))
    return calcula(x1,y1,x2,y2)

def calcula(x1,y1,x2,y2):
    dx = x2 - x1
    dy = y2 - y1
    dsquared = dx**2 + dy**2
    result = math.sqrt(dsquared)
    return result

#-------------------------------------------------
#exemplo de chamada: isbetween(1,0,2)

def isbetween(x,y,z):
    if y <= x and x <= z:
        return 1
    else:
        return 0

#------------------------------------------------
#exemplo de chamada: imprime(5)

def fibonacci(n):
    if n == 0 or n == 1:
        return 1
    else:
        a = fibonacci(n-1)
        b = fibonacci(n-2)
        return a + b

num = []
def imprime(n):
    for i in range (0,n+1):
        num.append(fibonacci(i))
        print num

#--------------------------------------------------
#exemplo de chamada: inverte('casa')

def inverte(x):
    a = len(x) - 1
    while a >= 0:
        print x[a]
        a = a - 1
    
#---------------------------------------------------
#exemplo de chamada: letra('abacate','a')

def letra(string, letra):
    a = len(string)
    b = 0
    count = 0
    while b <= a - 1:
	if letra == string[b]:
	    count = count + 1
	b = b + 1
    return count

#----------------------------------------------------
#exemplo de chamada: ocorre('ana e mariana gostam de banana', 'ana')

def ocorre(frase, palavra):
    count = 0
    for a in range(0,len(frase)-1):
	if frase.startswith(palavra,a):
	    count = count + 1
    return count
# ERRO PARCIAL 1.7: ocorre('ana e mariana gostam de banana', 'a') = 9 mas está retornando 8.


#---------------------------------------------------
#exemplo de chamada: raiz()

def raiz():
    for n in range(1000,9999):
	numtostr = str(n)
	abstr = numtostr[0]+numtostr[1]
	cdstr = numtostr[2]+numtostr[3]
	ab=int(abstr)
	cd=int(cdstr)
	if math.sqrt(n) == ab + cd :
	    print n

#----------------------------------------------------
#exemplo de chamada: subnumero(23,57238)

def subnumero(p,q):
    pstr = str(p)
    qstr = str(q)
    count = 0
    for a in range(0,len(qstr)-1):
	if qstr.startswith(pstr,a):
	    count = count + 1
    if count == 0 :
	return 'p nao eh subnumero de q'
    else:
	return 'p eh subnumero de q'
