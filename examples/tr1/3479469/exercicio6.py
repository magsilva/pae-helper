# Arquivo: exercicio6.py

# Funcao: conta letra
def conta_letra (frase, letra):
    return frase.count(letra)
    
frase = ""
letra = ""

frase = raw_input("Digite uma frase: ")
letra = raw_input("Digite uma letra: ")

if len(letra) > 1:
    letra = letra[0]

print conta_letra(frase, letra)
