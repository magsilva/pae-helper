# ERRO 1 14

class ConjuntoInteiros:

    def adicionar(self, numero):
        if type(numero) is type(0):
            if not numero in self.dados:
                self.dados.append(numero)

    def remover(self, numero):
        if numero in self.dados:
            self.dados.remove(numero)

    def unir(self, conjunto):
        if type(conjunto) is type(self):
            for numero in conjunto.dados:
                if not numero in self.dados:
                    self.dados.append(numero)

    def subtrair (self, conjunto):
        if type(conjunto) is type(self):
            for numero in conjunto.dados:
                if numero in self.dados:
                    self.dados.remove(numero)

    def inter (self, conjunto):
        intersec = []
        if type(conjunto) is type(self):
            for numero in conjunto.dados:
                if numero in self.dados:
                    intersec.append(numero)
        return intersec
    
    def __init__ (self, *numeros):
        self.dados = []
        for numero in numeros:
            if type(numero) is type(0):
                self.adicionar(numero)
            elif type(numero) is type(self):
                self.unir(numero)""" Autor: Daniel Cárnio Junqueira
    Este programa deve ler de um arquivo
    texto linhas com frases que contem
    palavras separadas por branco (' '),
    sendo que estas palavras podem ser tags.
    O programa deve apresentar o total de frases,
    palavras e tags. Também deve indicar existência
    de tags erradas (inconscistencia)"""

#classe frases: neste caso, ira apenas guardar numero total
#de frases do arquivo inteiro.
class frases:
    def __init__ (self, numero=0):
        self.numeroFrases = numero

    def adiciona(self, numero):
        self.numeroFrases += numero

#classe palavras
class palavras:
    def __init__ (self, numero=0):
        self.numeroPalavras = numero

    def adiciona(self, numero):
        self.numeroPalavras += numero

#classe tags
class tags:
    def __init__ (self, nCorretas=0, problema=0, corretas=""):
        self.tagsCorretas = nCorretas
        self.tagsProblema = problema
        self.strCorretas = corretas

    def adiciona(self, nCorretas=0, problema=0, corretas=""):
        self.tagsCorretas += nCorretas
        self.tagsProblema += problema
        self.strCorretas += corretas

#classe linhas
class linhas:
    def __init__ (self, conteudoLinha, numeroLinha, numeroPalavras=0, tagsb=0, tagsp=0):
        self.Tags = tags(tagsb, tagsp)
        self.Palavras = palavras(numeroPalavras)
        self.linha = numeroLinha
        self.conteudo = conteudoLinha


#le nome do arquivo
nomeArquivo = raw_input("Por favor, entre com o nome do arquivo de entrada: ")

arquivo = file(nomeArquivo, 'r')

#armazena conteudo do arquivo na variavel conteudo
conteudo=arquivo.read()

arquivo.close()

#calcula frases

Frases = frases(conteudo.count('.')-conteudo.count('...'))
Frases.adiciona(conteudo.count('?')-conteudo.count('???'))
Frases.adiciona(conteudo.count('!')-conteudo.count('!?'))

#separa as linhas do arquivo
Linhas = conteudo.splitlines()

for i in range(0, len(Linhas)):
    Linhas[i] = linhas(Linhas[i], i+1, Linhas[i].count(' ')+1, 0, 0)

for i in range(0, len(Linhas)):

    #contar numero de tags corretas e procurar por tags incorretas
    tagAtual = ""
    for j in range (0, len(Linhas[i].conteudo)):
                    if Linhas[i].conteudo[j] == '<':
                        if tagAtual == "":
                            tagAtual = '<'
                        else:
                            Linhas[i].Tags.adiciona(problema=1)
                            tagAtual = '<'
                    elif Linhas[i].conteudo[j] == '>':
                        if tagAtual == "":
                            Linhas[i].Tags.adiciona(problema=1)
                            tagAtual = ""
                        else:
                            tagAtual += '>'
                            Linhas[i].Tags.adiciona(nCorretas=1, corretas=tagAtual)
                            tagAtual = ""
                    elif tagAtual != "":
                        tagAtual += Linhas[i].conteudo[j]
                        if j == len(Linhas[i].conteudo)-1:
                            Linhas[i].Tags.adiciona(problema=1)

nomeArquivoSaida = raw_input('Por favor, digite nome do arquivo de saida: ')

arquivoSaida = file(nomeArquivoSaida, 'w')

for i in range(0, len(Linhas)):
    arquivoSaida.write('linha ')
    arquivoSaida.write(str(Linhas[i].linha))
    arquivoSaida.write(' - ')
    arquivoSaida.write(str(Linhas[i].Palavras.numeroPalavras))
    arquivoSaida.write(' palavras - ')
    arquivoSaida.write(str(Linhas[i].Tags.tagsCorretas))
    arquivoSaida.write(' tags (')
    arquivoSaida.write(Linhas[i].Tags.strCorretas)
    arquivoSaida.write(') - ')
    arquivoSaida.write(str(Linhas[i].Tags.tagsProblema))
    arquivoSaida.write(' tags-problema\n')

arquivoSaida.write('Numero de frases: ')
arquivoSaida.write(str(Frases.numeroFrases))

arquivoSaida.close()

opcao = 'X'

while opcao != 'S' and opcao != 'N':
    opcao = raw_input('Deseja imprimir os dados na tela? (S/N) ')
    if opcao == 'S' or opcao == 's':
        opcao = 'S'
        arquivoSaida = file(nomeArquivoSaida, 'r')
        conteudo = arquivoSaida.read()
        print conteudo
    elif opcao == 'n':
        opcao = 'N'

# ERRO 2 23
