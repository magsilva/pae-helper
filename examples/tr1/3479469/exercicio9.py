# Arquivo: exercicio9.py

p = raw_input("Digite o numero p: ")
q = raw_input("Digite o numero q: ")

if len(q) > len(p):
    print("Erro: numero de digitos de q deve ser menor ou igual ao de p")
else:
    if p.count(q) >= 1:
	print("q eh subnumero de p")
    else:
	print("q nao eh subnumero de p")
    
