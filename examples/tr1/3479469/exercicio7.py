# Arquivo: exercicio7.py

# Funcao: conta substrings...
def conta_palavra (frase, palavra):
    return frase.count(palavra)

frase = ""
palavra = ""

frase = raw_input("Digite uma frase: ")
palavra = raw_input("Digite uma palavra (substring): ")

print conta_palavra(frase, palavra)
