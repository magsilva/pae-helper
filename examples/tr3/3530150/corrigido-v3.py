3� lista de POO
Thiago Kenji Souto	-	3530150

1)
# ERRO TOTAL 1 4
# ERRO TOTAL 1 5
	1.1)	"construtor" � o m�todo que cria o objeto a partir de
		uma instancia��o de uma classe.
		"destrutor" � o metodo que destr�i o objeto,
		liberando a mem�ria referente �quele objeto.

		Em Python, o m�todo construtor � definido com
		def __init__ (self[,a[,b[...]]]):
		E o m�todo destrutor � autom�tico. Quando n�o h�
		refer�ncia para um determinado objeto, ele �
		destru�do.
# ERRO PARCIAL 1 7
	1.2)	Acessa-se um objeto por m�todos da classe do objeto.
# ERRO TOTAL 1 8
	1.3)	Classes, objetos, encapsulamento, sobrecarga e
		polimorfismo.
# ERRO PARCIAL 1 1
	1.4)	Classe � o mecanismo para se criar estruturas de
		dados e novos tipos de objetos. Um objeto � uma
		instancia��o de uma classe. Um m�todo � o meio de se
		manipular um objeto.

	1.5)	Em linguagem orientada a objetos, h� um menor "gap
		sem�ntico", a diferen�a entre o modelo computacional
		e o real.

# ERRO PARCIAL 2 3
2)
class Palavras:
    def __init__(self):
        self.word = ""

    def nrochar(self):
        return len(self.word)

    def thechar(self, c):
        return self.word.count(c)

3)

# ERRO PARCIAL 3 3
q = raw_input("entre com o texto:")
w = q.split()
e = len(w)
n = e
r = Palavras()
t = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
while (e):
    t[r.nrochar()] = t[r.nrochar()] + 1
    e-= 1
a=1
while (a < 35):
    if (t[a]):
        print "palavras com " + str(a) + " letras: " + str(t[a])
    a+= 1

# ERRO PARCIAL 3 5

4)
from random import Random

artigos = ['o','a','os','as','um','uma','uns','umas']
substantivos=['gata','cao','cidade','bicicleta','Baptista','cadela','cavalo','carro','animal','tecido','olho','martelo','aviao','pistache']
verbos=['andou','correu','pulou','caiu','cheirou','comeu','lambeu','implicou','navegou','assumiu','cantou','desafinou']
prepos=['de','sobre','sob','embaixo','para']

q = Random()

a = 0
while(a<20):
    lista = []
    lista.append(artigos[int(q.random()*len(artigos))])
    lista[0] = lista[0].capitalize()
    lista.append(' ')
    lista.append(substantivos[int(q.random()*len(substantivos))])
    lista.append(' ')
    lista.append(verbos[int(q.random()*len(verbos))])
    lista.append(' ')
    lista.append(prepos[int(q.random()*len(prepos))])
    lista.append(' ')
    lista.append(artigos[int(q.random()*len(artigos))])
    lista.append(' ')
    lista.append(substantivos[int(q.random()*len(substantivos))])
    lista.append('.')

    print ''.join(lista)
    
    a+= 1

# ERRO TOTAL 4 8
5)
Ainda n�o fiz.
Implementar at� 7/4/03.
(N�o se esque�a de mover para a pasta de exerc�cios completos ao implementar!)
