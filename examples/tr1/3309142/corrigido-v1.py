1.1
>>> def compare(x,y):
	if x>y:
		return 1
	elif x==y:
		return 0
	else:
		return -1

	
>>> compare(1,2)
-1
>>> compare(2,2)
0
>>> compare(2,1)
1

1.2
>>> import math
>>> def distancia():
	x1 = input("x1- ")
	x2 = input("x2- ")
	y1 = input("y1- ")
	y2 = input("y2- ")
	dx = x2 - x1
	dy = y2 - y1
	dsquared = dx**2 + dy**2
	return math.sqrt(dsquared)

>>> distancia
<function distancia at 0x00BC5CF8>
>>> distancia()
x1- 0
x2- 1
y1- 0
y2- 1
1.4142135623730951

1.3
def isBetween(x,y,z):
	l = [x,y,z]
	l.sort()
	if l[1] == y:
		return 1
	else:
		return 0

print isBetween(1,2,3)
# ERRO TOTAL 1.3: Se x for menor que y e z maior que y, retornará 1 mas não é verdade.


1.4
def fibonacci_poo(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fibonacci_poo(n-1)+fibonacci_poo(n-2)

def fibonacci(n):
    for i in range(n):
        print fibonacci_poo(i)

fibonacci(10)

1.5
def letras(str):
    for x in range(len(str) - 1, -1, -1):
        print str[x]

letras('programacao')

1.6
def contar(str,chr):
    sum = 0
    for x in range(0, len(str) - 1):
        if str[x] == chr:
            sum += 1
    return sum

print contar("ABACATE", 'A')
# ERRO PARCIAL 1.6: Não conta a última letra (tente "abacate" e "e").

1.7
def contar(str1, str2):
    sum = 0
    for x in range(0, len(str1) - len(str2) + 1):
        y = string.find(str1, str2, x, x + len(str2))
        if y <> -1:
            sum += 1
    return sum
print contar("ana e mariana gostam de banana", "ana")
# ERRO PARCIAL 1.7: Não importa o pacote string.
# ERRO PARCIAL 1.7: Não conta corretamente o caracter "".

1.8
import math
import string
def scrot():
    for i in range(1000, 9999):
        str = repr(i)
        a = string.atoi(str[0:2])
        b = string.atoi(str[2:4])
        if math.sqrt(i) == a + b:
            print i
scrot()

1.9
import math
import string
def ins(p,q):
    a=repr(p)
    b=repr(q)
    if string.find(b,a)<>-1:
        return 1
    else:
        return 0

print ins(23,57238)
print ins(23,56434)
