# Exercicio - Aula de sobrecarga de operadores e tratamento de excecoes
# SCE 213 - Programacao Orientada a Objetos
# Profa. Renata Pontin M. Fortes
#
# Joao Paulo Scardua Coelho    3560630  jpcoelho@grad.icmc.usp.br
# Koji E. Sasaoka              3560665  koji@grad.icmc.usp.br



class Ponto:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def set_ponto(self, x, y):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def __add__(self, other):
        return Ponto(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Ponto(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return self.x * other.x + self.y * other.y

    def __div__(self, other):
        return Ponto(self.x/other.x, self.y/other.y)

    def __rmul__(self, other):
        return Ponto(other * self.x, other * self.y)

    def __idiv__(self, other):
        try :
            c = Ponto(self.x/other, self.y/other)
        except ZeroDivisionError:
            c = self
            print "ERRO : Divisao por zero"
        else :
            print "Abnormal ERROR"
        return c

    def __str__(self):
        return '('+ str(self.x) + ',' + str(self.y) + ')'

a = Ponto()
b = Ponto()
c = a + b

# ERRO 1 1 75
# ERRO 1 2 75
# ERRO 1 3 75
# ERRO 1 4 75

class Circle(Ponto):
    def __init__(self, raio = 1, x = 0, y = 0):
        Ponto.__init__(self, x, y)
        self.raio = raio

    def printc(self):
        print self.get_x()
        print self.get_y()
        print self.raio

    def area(self):
        return 3.141592 * self.raio * self.raio

    def set_circle(self, p):
        self.x = p.x
        self.y = p.y
    
    def __add__(self, other):
        return Circle(self.raio + other.raio, self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Circle(abs(self.raio - other.raio), self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Circle((self.raio * other.raio)/2, (self.x * other.x)/2, (self.y * other.y)/2)
        
    def __div__(self, other):
        return Circle((self.raio / other.raio)*2, (self.x / other.x)*2, (self.y / other.y)*2)

    def __rmul__(self, other):
        return Circle(self.raio * other, self.x * other, self.y * other)

    def __idiv__(self, other):
        try :
            c = Circle(self.raio / other, self.x / other, self.y / other)
        except ZeroDivisionError:
            c = self
            print "ERRO : Divisao por zero"
        else :
            print "Abnormal ERROR"
        return c

    def __str__(self):
        return '('+ str(self.raio) + ',' + str(self.x) + ',' + str(self.y) + ')'

# ERRO 1 5 75
# ERRO 1 6 75
# ERRO 1 7 75
# ERRO 1 8 75

class Cylinder(Circle):
    def __init__(self, alt = 1, raio = 1, x = 0, y = 0):
        Circle.__init__(self, raio, x, y)
        self.alt = alt

    def printcy(self):
        print self.get_x()
        print self.get_y()
        print self.raio
        print self.alt

    def volume(self):
        return self.area() * self.alt

    def area_cy(self):
        return ((self.area() * 2) + (2 * 3.141592 * self.raio * self.alt))

    def __add__(self, other):
        return Cylinder(self.alt + other.alt, self.raio + other.raio, self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Cylinder(abs(self.alt - other.alt), abs(self.alt - other.alt), self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Cylinder((self.alt * other.alt)/2, (self.raio * other.raio)/2, (self.x * other.x)/2, (self.y * other.y)/2)
        
    def __div__(self, other):
        return Cylinder((self.alt / other.alt)*2, (self.raio / other.raio)*2, (self.x / other.x)*2, (self.y / other.y)*2)

    def __rmul__(self, other):
        return Cylinder(self.alt * other, self.raio * other, self.x * other, self.y * other)

    def __idiv__(self, other):
        try :
            c = Cylinder(self.alt / other, self.raio / other, self.x / other, self.y / other)
        except ZeroDivisionError:
            c = self
            print "ERRO : Divisao por zero"
        else :
            print "Abnormal ERROR"
        return c

    def __str__(self):
        return '('+ str(self.alt) + ',' + str(self.raio) + ',' + str(self.x) + ',' + str(self.y) + ')'

# ERRO 1 9 75
# ERRO 1 10 75
# ERRO 1 11 75
# ERRO 1 12 75

# ERRO 1 13 100

d = Cylinder()
e = Cylinder()
f = d * e
print f
