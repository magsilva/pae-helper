 ####################################################################
#                                                                   #
# Guilherme de Almeida Cordeiro 3456690                             #
# e Thiago Kenji Souto		3530150                             #
# hoje é 22 de abri e o ano é 2003.                                 #
#                                                                   #
####################################################################


class Ponto:
    def __init__ (self, x=0, y=0):
        try:
            self.x = float(x)
            self.y = float(y)
        except:
            print 'Deveria entrar valores'

    def set_ponto (self, x, y):
        try:
            self.x = float(x)
            self.y = float(y)
        except:
            print 'Deveria entrar valores'
            
    def get_x (self):
        return self.x
    def get_y (self):
        return self.y
    def __add__ (self, other):
        try:
            p = Ponto(self.x + other.x, self.y + other.y)
        except:
            print 'Soma deveria ser de pontos'
            return self
        else:
            return p
        
    def __mul__ (self, other):
        try:
            n = self.x * other.x + self.y * other.y
        except:
            print 'Produto (__mul__) deveria ser entre pontos'
            return self
        else:
            return p
        
    def __rmul__ (self, other):
        try:
            p = Ponto (other * self.x, other * self.y)
        except:
            print 'Produto (__rmul__) deveria ser entre ponto e escalar'
            return self
        else:
            return p

    
    def __sub__ (self, other):
        try:
            s = Ponto(self.x - other.x, self.y - other.y)
        except:
            print 'Subtracao deveria ser entre pontos'
            return self
        else:
            return p
    
    def __div__ (self, other):
        try:
            n = self.x / other.x - self.y / other.y
        except:
            print 'Divisao deve ser escalar'
            return self
        else:
            return n
        
    def __rdiv__ (self, other):
        try:
            p = Ponto(self.x / other, self.y / other)
        except:
            print 'Divisao deve ser entre pontos'
            return self
        else:
            return p

    def __str__ (self):
        return '(' + str(self.x) + ',' + str(self.y) + ')'

class Circle (Ponto):
    def __init__ (self, raio=1, x=0, y=0):
        try:
            Ponto.__init__(self, x, y)
            self.raio = float(raio)
        except:
            print 'O raio deve ser um valor escalar'
            
    def get_raio (self):
        return self.raio
    def printc (self):
        print self.get_x()
        print self.get_y()
        print self.raio
    def area (self):
        return 3.141593 * self.raio * self.raio
    def set_circ (self, p):
        try:
            self.x = float(p.x)
            self.y = float(p.y)
        except:
            print 'Valores devem ser escalares'
            
    def __add__ (self, other):
        try:
            c = Circle (self.raio + other.get_raio(), self.x + other.get_x(), self.y + other.get_y())
        except:
            print 'Adicao deveria ser decirculos'
            return self
        else:
            return c

    def __sub__ (self, other):
        try:
            c = Circle (self.raio - other.get_raio(), self.x - other.get_x(), self.y - other.get_y())
        except:
            print 'Subtracao deveria ser decirculos'
            return self
        else:
            return c
        
    def __mul__ (self, other):
        try:
            c = Circle (self.raio*other.get_raio(), self.x*other.get_x(), self.y*other.get_y())
        except:
            print 'Produto (__mul__) deveria ser decirculos'
            return self
        else:
            return c
        
    def __rmul__ (self, other):
        try:
            c = Circle (self.raio*other, self.x*other, self.y*other)
        except:
            print 'Produto (__rmul__) deveria ser decirculos'
            return self
        else:
            return c
        
    def __div__ (self, other):
        try:
            c = Circle (self.raio/other.get_raio(), self.x/other.get_x(), self.y/other.get_y())
        except:
            print 'Divisao (__div__) deveria ser de circulos'
            return self
        else:
            return c
        
    def __rdiv__ (self, other):
        try:
            c = Circle (self.raio/other, self.x/other, self.y/other)
        except:
            print 'Divisao (__rdiv__) deveria ser de circulos'
            return self
        else:
            return c
        
    def __str__ (self):
        return '[' + str(self.raio) + ']' + '(' + str(self.x) + ',' + str(self.y) + ')'


# ERRO 1 5 15
# ERRO 1 6 15
# ERRO 1 7 15
# ERRO 1 8 15
    
class Cylinder (Circle):
    def __init__ (self, alt=1, raio=1, x=0, y=0):
        try:
            Circle.__init__(self, raio, x, y)
            self.alt = float(alt)
        except:
            print 'Altura deve ser escalar'
            
    def printcy (self):
        print self.get_x()
        print self.get_y()
        print self.raio
        print self.alt
    def volume (self):
        return self.area() * self.alt
    def area (self):
        return self.area * 2 + 2 * 3.141593 * self.raio * self.alt
    def get_alt (self):
        return self.alt
    def __add__ (self, other):
        try:
            c = Cylinder(self.alt+other.get_alt(), self.raio + other.get_raio(), self.x + other.get_x(), self.y + other.get_y())
        except:
            print 'Soma deve ser de cilindros'
            return self
        else:
            return c

    def __sub__ (self, other):
        try:
            c = Cylinder (self.alt-other.get_alt(), self.raio - other.get_raio(), self.x - other.get_x(), self.y - other.get_y())
        except:
            print 'Diferenca deve ser de cilindros'
            return self
        else:
            return c

    def __mul__ (self, other):
        try:
            c = Cylinder (self.alt*other.get_alt(), self.raio * other.get_raio(), self.x*other.get_x(), self.y*other.get_y())
        except:
            print 'Produto (__mul__) deve ser de cilindros'
            return self
        else:
            return c
        
    def __rmul__ (self, other):
        try:
            c = Cylinder (self.alt*other, self.raio*other, self.x*other, self.y*other)
        except:
            print 'Produto (__rmul__) deve ser de cilindros'
            return self
        else:
            return c

    def __div__ (self, other):
        try:
            c = Cylinder (self.alt/other.get_alt(), self.raio/other.get_raio(), self.x/other.get_x(), self.y/other.get_y())
        except:
            print 'Produto (__div__) deve ser de cilindros'
            return self
        else:
            return c

    def __rdiv__ (self, other):
        try:
            c = Cylinder (self.alt/other, self.raio/other, self.x/other, self.y/other)
        except:
            print 'Produto (__div__) deve ser de cilindros'
            return self
        else:
            return c
        
    def __str__ (self):
        return '{' + str(self.alt) + '}[' + str(self.raio) + ']' + '(' + str(self.x) + ',' + str(self.y) + ')'

# ERRO 1 9 15
# ERRO 1 10 15
# ERRO 1 11 15
# ERRO 1 12 15

a = Cylinder()
print a
a += 1
