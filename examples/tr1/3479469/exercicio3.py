# Arquivo: exercicio3.py

# Funcao: isBetween(x,y,z)
# Entrada: x, y, z
# Saida: 1, se y <= x <= z
#        0, caso contrário
def isBetween(x, y, z):
    if (x >= y) and (x <= z):
	return (1)
    else:
	return (0)

x=0
y=0 
z=0

x=input("Digite x: ")
y=input("Digite y: ")
z=input("Digite z: ")

print ("Resultado: %d" % isBetween(x,y,z))
