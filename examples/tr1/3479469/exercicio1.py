# Arquivo: exercicio1.py
# Primeiro exercicio POO, dia 18/03/2003

# Funcao: compare
# Entrada: x, y
# Saida: 1, se x>y
#        0, se x==y
#       -1, se x<y
def compare (x, y):
    if (x>y):
	return (1)
    elif (x==y):
	return(0)
    else:
	return(-1)

x=0
y=0

print("Por favor, digite x: ")
x = input()

print("Por favor, digite y: ")
y = input()

resultado = compare(x,y)

print("Resultado: %d" % resultado)
