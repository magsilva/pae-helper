import math

def compare(x,y):
    if (x>y):
        return 1
    elif (x==y):
        return 0
    elif (x<y):
        return -1

def distancia():
    x1 = float(raw_input("x1: "))
    y1 = float(raw_input("y1: "))
    x2 = float(raw_input("x2: "))
    y2 = float(raw_input("y2: "))
    print math.sqrt((x2-x1)**2+(y2-y1)**2)

def isBetween(x,y,z):
    if (y<=x) and (x<=z):
        return 1
    else:
        return 0

def Fibonacci(n):
    if (n==0) or (n==1):
        return 1
    else:
        print n
        return Fibonacci(n-1) + Fibonacci(n-2)

# ERRO TOTAL 1.4: Não imprime a seqüência corretamente, repete números, não tem todos os números de Fibonacci.

def inv(a):
    l = len(a)
    while (l):
        print a[l-1]
        l -= 1

def count2(a, c):
    print a.count(c)

# ERRO PARCIAL 1.6: Não conta corretamente o caracter "".

def count3(a, c):
    print a.count(c)

# ERRO PARCIAL 1.7: Não conta corretamente o caracter "".
# ERRO PARCIAL 1.7: Não aceita o caso de teste proposto no exercício.

def root():
    n=1000
    pt1=pt2=""
    while (n<9999):
        s = str(n)
        pt1 = s[0] + s[1]
        pt2 = s[2] + s[3]
        k = int(pt1) + int(pt2)
        if (math.sqrt(n) == k):
            print n
        n += 1

def umpontonove(p,q):
    a=str(p)
    b=str(q)
    if (b.len() <= a.len()):
        return a.count(b)
    else:
        return b.count(a)

# ERRO TOTAL 1.9: Não funciona.

