# Arquivo: exercicio4.py

# Funcao: n primeiras linhas da sequencia de
#         Fibonacci
def fibonacci (n):
    if n ==0 or n ==1:
	return 1
    else:
	return fibonacci(n-1) + fibonacci(n-2) 
    

n = 0
n = int (raw_input ("Digite n: "))

fibonacci(n)

# comentario: mantendo o algoritmo recursivo,
# nao consegui imprimir primeiras n linhas
# da sequencia de fibonacci.
# daniel.
