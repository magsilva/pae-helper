"Alexandre Branda Viriato - 3167972"
"Andreza Miqueletti - 3672701"
"Rodrigo Mithuhiuro Oshiro - 3528863"

import math

"Exercicio 1.1"
def comparar(x,y):
   if x>y:
      return 1
   elif x==y:
      return 0
   else:
      return -1
"Exercicio 1.2"
def distancia(x1,y1,x2,y2):
   dx = x2-x1
   dy = y2-y1
   return math.sqrt(dx**2 + dy**2)
# ERRO PARCIAL 1.2: Não imprime os dados.
# ERRO PARCIAL 1.2: Não lê os dados.

"Exercicio 1.3"
def isBetween(x,y,z):
   if y<=x and x<=z:
      return 1
   else:
      return 0

"Exercicio 1.4"
def fibbonacci(n):
   i=2
   a=1
   b=1
   if n<2:
      return
   print a
   print b
   while i<n:
      c=a+b
      a=b
      b=c
      print c
      i += 1

# ERRO PARCIAL 1.4: Não funciona para o primeiro termo da seqüência (n = 1)

"Exercicio 1.5"
def reverse(message):
   i = len(message)
   while i>0:
      print message[i-1]
      i -= 1
"Exercicio 1.6"
def contar(message,c):
   count = 0;
   for m in message:
      if m==c:
         count += 1
   return count
"Exercicio 1.7"
def contar_pal(palavra,message):
   count = 0
   a = 0
   b = 0
   while(a<len(message)):
      b = 0
      while(b<len(palavra) and (a+b)<len(message)):
         if(message[a+b]!=palavra[b]):
            break;
         b += 1
      if(b==len(palavra)):
         count += 1
      a += 1
   return count


"Exercicio 1.8"
def dividir(numero):
   a = numero/100
   b = numero - a*100
   c = a+b
   if c**2==numero:
      return 1
   else:
      return 0
# ERRO PARCIAL 1.8: Não faz tudo o que o enunciado pede.

"Exercicio 1.9"
def subnumero(p,q):
   a = "%d"%p
   b = "%d"%q
   if len(a)<=len(b):
      return b.count(a,0,len(b))
   else:
      return 0
