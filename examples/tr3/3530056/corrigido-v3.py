# Aluno: Kaio Mori Tuleski
# NUSP: 3530056 

# ERRO TOTAL 1 1
# ERRO TOTAL 1 2
# ERRO TOTAL 1 3
# ERRO TOTAL 1 4
# ERRO TOTAL 1 5
# ERRO TOTAL 1 6
# ERRO TOTAL 1 7
# ERRO TOTAL 1 8
# ERRO TOTAL 1 9
# ERRO TOTAL 1 10


class Palavras:

    def __init__(self,palavra):
        self.p = palavra

    def conta_char(self):
       return len(self.p)
    def conta_o_char(self,char):
        return self.p.count(char)

#-----------------------------------------------------------------------


# ERRO TOTAL 3 3
tabela = [] 
linha = raw_input("Digite uma frase: ") 
while linha != "": 
    for i in range(1, 20): 
        tabela.append(0) 
    lista = linha.split(" ") 
    for p in lista: 
        palavra = Palavras(p) 
        i = palavra.conta_char() 
        tabela[i] += 1 
 
    for i in range(1, 20): 
        try: 
            if tabela[i] != 0: 
                print "Numero de palavras com " + str(i) + " caracteres: " + str(tabela[i]) 
        except: 
            a = 0 
 
    linha = raw_input("Digite uma frase: ") 
    tabela = []

# ERRO PARCIAL 3 5

#---------------------------------------------------------------------------------------------------

class Frases: 
    def __init__(self): 
        self.artigo = ['o', 'a', 'um', 'uma'] 
        self.substantivo = ['gata', 'cachorro', 'cidade', 'bicicleta'] 
        self.verbo = ['andou', 'correu', 'perdeu', 'pulou', 'caiu'] 
        self.preposicao = ['de', 'sobre', 'embaixo', 'em', 'sob'] 
        self.frases = [] 
        self.constroi_frase() 
    def constroi_frase(self): 
        import random 
        for i in range(0, 20): 
            frase = ' ' 
            art1 = random.choice(self.artigo) 
            art = art1.capitalize() 
            sub1 = random.choice(self.substantivo) 
            ver = random.choice(self.verbo) 
            prep = random.choice(self.preposicao) 
            art2 = random.choice(self.artigo) 
            sub2 = random.choice(self.substantivo) 
            frase = art + ' ' + sub1 + ' ' + ver + ' ' + prep + ' ' + art2 + ' ' + sub2 + '.' 
            self.frases.append(frase) 
 
        for obj in self.frases: 
            print obj

