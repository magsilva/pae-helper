Lista de Exercícios 2 ? Parte 2 ? Classes
SCE 213 - POO ? Renata Pontin M. Fontes
Alunos:
Carolina Toledo Ferraz  		nº USP 3344524
João Paulo Scardua Coelho 	nº USP 3560630

*****************************************************************************************************************

Exercício 2.1

Criação da classe ConjuntoInteiros:

class ConjuntoInteiros:
    def __init__(self, *x):
        self.conjunto = []
        for i in x:
            if type(i) == type (0): #se eh do tipo int
                self.adicionar(i)
            elif type(i)== type(self): #do tipo ConjuntoInteiro
                self.uniao_inicia(i)

# ERRO 1 2

    def adicionar(self, inteiro):
        if inteiro not in self.conjunto:
	    self.conjunto.append(inteiro)

    def remover(self, inteiro):
        try:
            self.conjunto.remove(inteiro)
        except:
            print 'Elemento '+ str(inteiro) +' nao pertece ao conjunto'

    def uniao_inicia(self, objeto):
        for k in objeto.conjunto:
            self.adicionar(k)

    def uniao(self, objeto):
	ret = []
	ret.extend(objeto.conjunto)
	for k in self.conjunto:
		if k not in ret:
			ret.append(k)
	print ret

    def interseccao(self,objeto):
	ret = []
	for j in objeto.conjunto:
		if j in self.conjunto:
			ret.append(j)
	print ret    

    def subtracao(self,objeto):
	ret = [] 
	for i in self.conjunto:
		if i not in objeto.conjunto:
			ret.append(i)
	print ret

    def imprime(self):
        print self.conjunto


Exemplos de inicializações e operações:

a = ConjuntoInteiros(1,2,3,4)
a.imprime()
a.adicionar(22)
a.imprime()
b = ConjuntoInteiros(1,5)
b.imprime()
b.uniao(a)
a.imprime()
b.imprime()
b.interseccao(a)
b.imprime()
b.subtracao(a)
a.subtracao(b)
b.imprime()
a.imprime()
c = ConjuntoInteiros(a,b,6,7,8,9,10)
c.imprime()
a.remover(189)
c.remover(22)
c.imprime()
d = ConjuntoInteiros(10,9,23)
d.imprime()
d.uniao(b)
c.subtracao(d) 

*****************************************************************************************************************

Exercício 2.2

Manipulação de arquivos e cadeia de caracteres

class palavras:
    def __init__(self):
        self.num_pal = 0

    def incrementa(self):
        self.num_pal += 1

class tags:
    def __init__(self):
        self.num_tags = 0
        self.num_tags_probl = 0
        self.tags = '' #lista das tags encontradas

class frases:
    def __init__(self):
        self.linha = ""     

O método analisa da classe frases faz a verificação de quantas palavras,tags e tags com problema há no arquivo

    def analisa(self,filentrada,filesaida):
        p = palavras()
        t = tags()
        fin = open(filentrada,'r')
        fout = open(filesaida,'w')
        self.linha = fin.readline()
	l = 1
        while self.linha:  
            p.num_pal = 0
            t.num_tags = 0
	    aux =''
            t.tags = ''
            tag_state = 0
            for i in self.linha:
                if i.isspace(): #considera espaco, tabs, \n, ...
                    p.incrementa()
                elif i == '<' and not tag_state:
                    tag_state = 1
                    t.num_tags += 1
                elif i == '<' and tag_state:
		    aux = ''
		    t.num_tags_probl += 1
                elif i == '>' and tag_state:
                    tag_state = 0
                    aux += i
                    t.tags += aux
                    aux = ''
                if tag_state == 1:
		    aux += i
	    fout.write('Linha '+ str(l)+ ' - '+ str(p.num_pal)
		       +' palavra(s) - '+ str(t.num_tags)+' tag(s) '
		       +'('+ t.tags +') '+ str(t.num_tags_probl)
		       +' tag(s) com problema(s)\n') 
            self.linha = fin.readline()
	    l += 1
        fin.close()
        fout.close()

Formas de instanciação do objeto a e da chamada do método analisa:

a = frases()

a.analisa('teste_in.txt','teste_out.txt')

a.analisa('teste_in2.txt','teste_out2.txt')

Arquivos  de entrada utilizado como teste:

'teste_in.txt':

Teste de uso de <TAGS> em POO
e processamento de <problemas com <mau> uso <de> tags?
'teste_in2.txt': Arquivo html de uma página web qualquer

<font face="Arial,Helvetica">Caixa Postal 668&nbsp;</font> <br>
<font face="Arial,Helvetica">S&atilde;o Carlos - SP&nbsp;</font> 
<br>
<font face="Arial,Helvetica">13560-970</font> 
<p><b><font face="Arial,Helvetica">Telefone:</font></b> <br>
<font face="Arial,Helvetica">(016) 273-9639</font>

Arquivo de saída obtido:

'teste_out.txt;

Linha 1 - 7 palavra(s) - 1 tag(s) (<TAGS>) 0 tag(s) com problema(s)
Linha 2 - 9 palavra(s) - 2 tag(s) (<mau><de>) 1 tag(s) com problema(s)

'teste_out2.txt':

Linha 1 - 5 palavra(s) - 3 tag(s) (<font face="Arial,Helvetica"></font><br>) 0 tag(s) com problema(s)
Linha 2 - 6 palavra(s) - 2 tag(s) (<font face="Arial,Helvetica"></font>) 0 tag(s) com problema(s)
Linha 3 - 1 palavra(s) - 1 tag(s) (<br>) 0 tag(s) com problema(s)
Linha 4 - 3 palavra(s) - 2 tag(s) (<font face="Arial,Helvetica"></font>) 0 tag(s) com problema(s)
Linha 5 - 3 palavra(s) - 6 tag(s) (<p><b><font face="Arial,Helvetica"></font></b><br>) 0 tag(s) com problema(s)
Linha 6 - 2 palavra(s) - 2 tag(s) (<font face="Arial,Helvetica"></font>) 0 tag(s) com problema(s)
# ERRO 2 23
