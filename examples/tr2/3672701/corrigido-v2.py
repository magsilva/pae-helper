"Andreza Miqueletti"
"Alexandre Branda Viriato"
"Rodrigo Mithuhiro Oshiro"

#"Exercicio 2.1"
class ConjuntoInteiro:
    def __init__(self,*int):
        self.inteiros = []
        for x in int:
            if type(x) is type(1):
                equal = 0
                for y in self.inteiros:
                    if x == y:
                        equal = 1
                if equal == 0:
                    self.inteiros.append(x)
            elif type(x) is type(self):
                self += x

    def __add__(self,other):
        for x in other.inteiros:
            self.store(x)
    def __sub__(self,other):
        for x in other.inteiros:
            self.remove(x)
    def __mul__(self,other):
        for x in self.inteiros:
            if x not in other.inteiros:
                self.remove(x)
    def __str__(self):
        result = ""
        for x in self.inteiros:
            result += str(x) + " "
        return result
    def store(self,*int):
        for x in int:
            if type(x) is type(1):
                equal = 0
                for y in self.inteiros:
                    if x == y:
                        equal = 1
                if equal == 0:
                    self.inteiros.append(x)
    def remove(self,*int):
        for x in int:
            self.inteiros.remove(x)

#"Exercicio 2.2"
class Palavra:
    def __init__(self):
        self.palavra = []
    def __add__(self,palavra):
        self.palavra.append(palavra)
        
class Tag:
    def __init__(self):
        self.tag = []
    def __add__(self,tag):
        self.tag.append(tag)
        
class Frase:
    def __init__(self,frase=""):
        self.palavra = Palavra()
        self.tag = Tag()
        array = frase.split(" ")
        self.palavras = len(array)
        self.tags = 0
        self.erros = 0
        for x in array:
            if x == "":
                self.palavras -= 1
            elif x[0] == "<" and x[-1] == ">":
                self.tags += 1
                self.tag + x
            elif x[0] == "<" or x[-1] == ">":
                self.erros += 1
                self.palavra + x
            else:
                self.palavra + x
                
class Text:
    def __init__(self,file):
        self.frase = []
        self.file = open(file)
        line = self.file.readline()
        while line: 
            frase = Frase(line)
            self.frase.append(frase)
            line = self.file.readline()
        self.file.close()
    def __str__(self):
        result = ""
        count = 0
        for x in self.frase:
            count += 1
            result += str("linha %d - %d palavras - %d tags (" % (count,x.palavras,x.tags))
            for y in x.tag.tag:
                result += str(y)
            result += str(") -  %d tags problematicas\n" % (x.erros))
        return result

# ERRO 2 23
