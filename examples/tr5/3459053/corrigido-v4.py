# Alunos: Alessandra Kelli Barbato   no.USP: 3459053 
#         Daniel Carnio Junqueira    no.USP: 3479469
#         Marcos Fabio Martins       no.USP: 3458100  
#         Ottone Alexandre Traldi    no.USP: 3457749

from os import system

system('cls')

class Ponto:
    def __init__(self, x=0, y=0):
        if type(x) is type(0) or type(x) is type(0.0):
            self.x = x
        else:    
            self.x = 0   # valor default
        if type(y) is type(0) or type(y) is type(0.0):
            self.y = y
        else:    
            self.y = 0   # valor default
    def set_ponto(self, x, y):
        if type(x) is type(0) or type(x) is type(0.0):
            self.x = x
        else:    
            self.x = 0   # valor default
        if type(y) is type(0) or type(y) is type(0.0):
            self.y = y
        else:    
            self.y = 0   # valor default     
    def get_x(self):
        return self.x
    def get_y(self):
        return self.y
    def __add__(self, other):
        try:
            return Ponto(self.x + other.x, self.y + other.y)
        except:
            return Ponto(self.x, self.y)
    def __mul__(self, other):
        try:
            return Ponto(self.x * other.x, self.y * other.y)
        except:
            return Ponto(self.x, self.y)
    def __rmul__(self, other):
        try:
            return Ponto(other * self.x, other * self.y)
        except:
            return Ponto(self.x, self.y)

class Circle(Ponto):
    def __init__(self, raio=1, x=0, y=0):
        Ponto.__init__(self, x, y)
        if type(raio) is type(0) or type(raio) is type(0.0):            
            self.raio = abs(raio)
        else:
            self.raio = 1   # valor default
    def printc(self):
        print self.get_x()
        print self.get_y()
        print self.raio
    def area(self):
        return 3.141592 * self.raio * self.raio
    def set_circ(self, raio, p):
        try:
            self.x = p.x
            self.y = p.y
        except:
            self.x = 0   # valor default
            self.y = 0   # valor default
        if type(raio) is type(0) or type(raio) is type(0.0):            
            self.raio = abs(raio)
        else:   
            self.raio = 1  # valor default
    def __add__(self, other):
        try:
            return Circle(self.raio + other.raio, self.x + other.x, self.y + other.y)
        except:
            return Circle(self.raio, self.x, self.y)
    def __mul__(self, other):
        try:
            return Circle(self.raio * other.raio, self.x * other.x, self.y * other.y)
        except:
            return Circle(self.raio, self.x, self.y)
    def __sub__(self, other):
        try:
            return Circle(abs(self.raio - other.raio), self.x - other.x, self.y - other.y)
        except:
            return Circle(self.raio, self.x, self.y)
    def __div__(self, other):
        try:
            return Circle((self.raio+0.0)/other.raio, (self.x+0.0)/other.x, (self.y+0.0)/other.y)
        except:
            return Circle(self.raio, self.x, self.y)
    def __rmul__(self, other):
        try:
            return Circle(other * self.raio, self.x, self.y)
        except:
            return Circle(self.raio, self.x, self.y)
       
class Cylinder(Circle):
    def __init__(self, alt=1, raio=1, x=0, y=0):
        Circle.__init__(self, raio, x, y)
        if type(alt) is type(0) or type(alt) is type(0.0):
            self.alt = alt
        else:
            self.alt = 1   # valor default
    def set_cyli(self, alt, circ):
        try:
            self.x = circ.x
            self.y = circ.y
            self.raio = circ.raio
        except:
            self.x = 0     # valor default
            self.y = 0     # valor default
            self.raio = 1  # valor default
        if type(alt) is type(0) or type(alt) is type(0.0):
            self.alt = alt
        else:
            self.alt = 1   # valor default
    def printcy(self):
        print self.get_x()
        print self.get_y()
        print self.raio
        print self.alt
    def volume(self):
        return self.area() * self.alt
    def areacy(self):
        return self.area() * 2 + 2 * 3.141592 * self.raio * self.alt
    def __add__(self, other):
        try:
            return Cylinder(self.alt + other.alt, self.raio + other.raio, self.x + other.x, self.y + other.y)
        except:
            return Cylinder(self.alt, self.raio, self.x, self.y)
    def __mul__(self, other):
        try:
            return Cylinder(self.alt * other.alt, self.raio * other.raio, self.x * other.x, self.y * other.y)
        except:
            return Cylinder(self.alt, self.raio, self.x, self.y)
    def __sub__(self, other):
        try:
            return Cylinder(self.alt - other.alt, self.raio - other.raio, self.x - other.x, self.y - other.y)
        except:
            return Cylinder(self.alt, self.raio, self.x, self.y)
    def __div__(self, other):
        try:
            return Cylinder((self.alt+0.0)/other.alt, (self.raio+0.0)/other.raio, (self.x+0.0)/other.x, (self.y+0.0)/other.y)
        except:
            return Cylinder(self.alt, self.raio, self.x, self.y)
    def __rmul__(self, other):
        try:
            return Cylinder(self.alt*other, self.raio*other, self.x, self.y)
        except:
            return Cylinder(self.alt, self.raio, self.x, self.y)

# ERRO 1 5 10
# ERRO 1 6 10
# ERRO 1 7 10
# ERRO 1 8 10
# ERRO 1 9 10
# ERRO 1 10 10
# ERRO 1 11 10
# ERRO 1 12 10
        
p1 = Ponto(1,1)
print 'Circulo 1:'
c1 = Circle()
c1.set_circ(-4,3 * p1)
c1.printc()
print 'Cilindro 1:'
cy1 = Cylinder()
cy1.set_cyli(6, 2 * c1)
cy1.printcy()

p2 = Ponto(2,4)
print '\nCirculo 2:'
c2 = Circle()
c2.set_circ(5,p2)
c2.printc()
print 'Cilindro 2:'
cy2 = Cylinder()
cy2.set_cyli(10,c2)
cy2.printcy()

c3 = c1 + c2
cy3 = cy1 + cy2
print '\nCirculo1 + Circulo 2:'
c3.printc()
print 'Cilindro 1 + Cilindro 2:'
cy3.printcy()

c3 = c1 - c2
cy3 = cy1 - cy2
print '\nCirculo1 - Circulo 2:'
c3.printc()
print 'Cilindro 1 - Cilindro 2:'
cy3.printcy()

c3 = c1 * c2
cy3 = cy1 * cy2
print '\nCirculo1 * Circulo 2:'
c3.printc()
print 'Cilindro 1 * Cilindro 2:'
cy3.printcy()

c3 = c1 / c2
cy3 = cy1 / cy2
print '\nCirculo 1 / Circulo 2:'
c3.printc()
print 'Cilindro 1 / Cilindro 2:'
cy3.printcy()

cy3 += 3

raw_input()
system('cls')
