# Arquivo: exercicio5.py

def desfaz_string (frase):
    tamanho = len(frase)
    i = 1
    for i in range (1, tamanho+1):
	print(frase[-i])

frase = ""
frase = raw_input("Digite uma frase: ")
desfaz_string(frase)
