# Quinta lista de exercicios de P.O.O
# Professora Renata Pontin M. Fortes
# Anderson Sumitomo Otuka -- 3542803

class Ponto:

    def __init__(self, x=0, y=0):
        try:
            self.x = float(x)
            self.y = float(y)
        except Exception:
            self.x = 0
            self.y = 0
            print 'Entrada invalida. Esperados valores reais.'

    def set_ponto(self, x, y):
        try:
            self.x = float(x)
            self.y = float(y)
        except Exception:
            self.x = 0
            self.y = 0
            print 'Entrada invalida. Esperados valores reais.'

    def getx(self):
        return self.x

    def gety(self):
        return self.y

    def __str__(self):
        return '(x = %f, y = %f)' % (self.x, self.y)

    def __add__(self, other):
        try:
            if (other.__class__ == Ponto().__class__):
                return Ponto(self.getx() + other.getx(),
                             self.gety() + other.gety())
            else:
                print 'Esperado: Ponto1(x1, y1) + Ponto2(x2, y2).'
        except Exception:
            print 'Esperado: Ponto1(x1, y1) + Ponto2(x2, y2).'

    def __sub__(self, other):
        try:
            if (other.__class__ == Ponto().__class__):
                return Ponto(self.getx() - other.getx(),
                             self.gety() - other.gety())
            else:
                print 'Esperado: Ponto1(x1, y1) - Ponto2(x2, y2).'
        except Exception:
            print 'Esperado: Ponto1(x1, y1) - Ponto2(x2, y2).'

    def __mul__(self, other):
        try:
            if (other.__class__ == Ponto().__class__):
                return (self.getx() * other.getx() +
                        self.gety() * other.gety())
            elif ((type(other) == type(1.0)) or (type(other) == type(1))):
                return Ponto(other * self.getx(),
                             other * self.gety())
            else:
                print 'Esperado: Ponto1(x1, y1) * Ponto2(x2, y2) ou'
                print '          Ponto1(x1, y1) * Float(x) ou'
                print '          Float(x) * Ponto1(x1, y1).'
        except Exception:
            print 'Esperado: Ponto1(x1, y1) * Ponto2(x2, y2) ou'
            print '          Ponto1(x1, y1) * Float(x) ou'
            print '          Float(x) * Ponto1(x1, y1).'

    def __rmul__(self, other):
        try:
            return Ponto(other * self.getx(),
                         other * self.gety())
        except Exception:
            print 'Esperado: Ponto1(x1, y1) * Ponto2(x2, y2) ou'
            print '          Ponto1(x1, y1) * Float(x) ou'
            print '          Float(x) * Ponto1(x1, y1).'

    def __div__(self, other):
        try:
            if (other.__class__ == Ponto().__class__):
                return (self.getx() / other.getx() +
                        self.gety() / other.gety())
            elif ((type(other) == type(1.0)) or type(other) == type(1)):
                return Ponto(self.getx() / float(other),
                             self.gety() / float(other))
            else:
                print 'Esperado: Ponto1(x1, y1) / Ponto2(x2, y2) ou'
                print '          Ponto1(x1, y1) / Float(x) ou'
                print '          Float(x) / Ponto1(x1, y1).'
                
        except Exception:
            print 'Esperado: Ponto1(x1, y1) / Ponto2(x2, y2) ou'
            print '          Ponto1(x1, y1) / Float(x) ou'
            print '          Float(x) / Ponto1(x1, y1).'

    def __rdiv__(self, other):
        try:
            return Ponto(float(other) / self.getx(),
                         float(other) / self.gety())
        except Exception:
            print 'Esperado: Ponto1(x1, y1) / Ponto2(x2, y2) ou'
            print '          Ponto1(x1, y1) / Float(x) ou'
            print '          Float(x) / Ponto1(x1, y1).'


class Circle(Ponto):

    def __init__(self, raio=1, x=0, y=0):
        try:
            self.raio = float(raio)
            Ponto.__init__(self, x, y)
        except Exception:
            self.raio = 1
            Ponto.__init__(self, 0, 0)
            print 'Entrada invalida. Esperados valores reais.'

    def set_circ(self, raio, x, y):
        try:
            self.x = float(x)
            self.y = float(y)
            self.raio = float(raio)
        except Exception:
            self.x = 0
            self.y = 0
            self.raio = 1
            print 'Entrada invalida. Esperados valores reais.'

    def printc(self):
        print self.getr()
        print self.getx()
        print self.gety()
        
    def getr(self):
        return self.raio

    def area(self):
        return 3.141592 * self.getr() * self.getr()

    def __str__(self):
        return '(raio = %f, x = %f, y = %f)' % (self.getr(), self.getx(), self.gety())

    def __add__(self, other):
        try:
            if (other.__class__ == Circle().__class__):
                return Circle(self.getr() + other.getr(),
                              self.getx() + other.getx(),
                              self.gety() + other.gety())
            elif (other.__class__ == Ponto().__class__):
                return Circle(self.getr(),
                              self.getx() + other.getx(),
                              self.gety() + other.gety())
            elif ((type(other) == type(1)) or (type(other) == type(1.0))):
                return Circle(self.getr() + other,
                              self.getx(),
                              self.gety())
            else:
                print 'Esperado: Circle(r1, x1, y1) + Circle(r2, x2, y2) ou'
                print '          Circle(r1, x1, y1) + Ponto(x2, y2) ou'
                print '          Circle(r1, x1, y1) + Float(r2).'
        except Exception:
            print 'Esperado: Circle(r1, x1, y1) + Circle(r2, x2, y2) ou'
            print '          Circle(r1, x1, y1) + Ponto(x2, y2) ou'
            print '          Circle(r1, x1, y1) + Float(r2).'
        
    def __sub__(self, other):
        try:
            if (other.__class__ == Circle().__class__):
                return Circle(self.getr() - other.getr(),
                              self.getx() - other.getx(),
                              self.gety() - other.gety())
            elif (other.__class__ == Ponto().__class__):
                return Circle(self.getr(),
                              self.getx() - other.getx(),
                              self.gety() - other.gety())
            elif ((type(other) == type(1)) or (type(other) == type(1.0))):
                return Circle(self.getr() - other,
                              self.getx(),
                              self.gety())
            else:
                print 'Esperado: Circle(r1, x1, y1) - Circle(r2, x2, y2) ou'
                print '          Circle(r1, x1, y1) - Ponto(x2, y2) ou'
                print '          Circle(r1, x1, y1) - Float(r2).'
        except Exception:
            print 'Esperado: Circle(r1, x1, y1) - Circle(r2, x2, y2) ou'
            print '          Circle(r1, x1, y1) - Ponto(x2, y2) ou'
            print '          Circle(r1, x1, y1) - Float(r2).'

    def __mul__(self, other):
        try:
            if (other.__class__ == Circle().__class__):
                return (self.getr() * other.getr() +
                        self.getx() * other.getx() +
                        self.gety() * other.gety())
            elif ((type(other) == type(1.0)) or type(other) == type(1)):
                return Circle(other * self.getr(),
                              other * self.getx(),
                              other * self.gety())
            else:
                print 'Esperado: Circle1(r1, x1, y1) * Circle2(r2, x2, y2) ou'
                print '          Circle1(r1, x1, y1) * Float(x) ou'
                print '          Float(x) * Circle1(r1, x1, y1).'
        except Exception:
            print 'Esperado: Circle1(r1, x1, y1) * Circle2(r2, x2, y2) ou'
            print '          Circle1(r1, x1, y1) * Float(x) ou'
            print '          Float(x) * Circle1(r1, x1, y1).'

    def __rmul__(self, other):
        try:
            return Circle(self.getr() * other,
                          self.getx() * other,
                          self.gety() * other)
        except Exception:
            print 'Esperado: Circle1(r1, x1, y1) * Circle2(r2, x2, y2) ou'
            print '          Circle1(r1, x1, y1) * Float(x) ou'
            print '          Float(x) * Circle1(r1, x1, y1).'

    def __div__(self, other):
        try:
            if (other.__class__ == Circle().__class__):
                return (self.getr() / other.getr() +
                        self.getx() / other.getx() +
                        self.gety() / other.gety())
            elif ((type(other) == type(1.0)) or type(other) == type(1)):
                return Circle(self.getr() / float(other),
                              self.getx() / float(other),
                              self.gety() / float(other))
            else:
                print 'Esperado: Circle1(r1, x1, y1) / Circle2(r2, x2, y2) ou'
                print '          Circle1(r1, x1, y1) / Float(x) ou'
                print '          Float(x) / Circle1(r1, x1, y1).'
        except Exception:
            print 'Esperado: Circle1(r1, x1, y1) / Circle2(r2, x2, y2) ou'
            print '          Circle1(r1, x1, y1) / Float(x) ou'
            print '          Float(x) / Circle1(r1, x1, y1).'

    def __rdiv__(self, other):
        try:
            return Circle(float(other) / self.getr(),
                          float(other) / self.getx(),
                          float(other) / self.gety())
        except Exception:
            print 'Esperado: Circle1(r1, x1, y1) / Circle2(r2, x2, y2) ou'
            print '          Circle1(r1, x1, y1) / Float(x) ou'
            print '          Float(x) / Circle1(r1, x1, y1).'


class Cylinder(Circle):

    def __init__(self, alt=1, raio=1, x=0, y=0):
        try:
            self.alt = alt
            Circle.__init__(self, raio, x, y)
        except Exception:
            self.alt = 0
            Circle.__init__(self, 0, 0, 0)
            print 'Entrada invalida. Esperados valores reais.'

    def set_cyl(self, alt, raio, x, y):
        try:
            self.alt = float(alt)
            self.raio = float(raio)
            self.x = float(x)
            self.y = float(y)
        except Exception:
            self.alt = float(1)
            self.raio = 1
            self.x = 0
            self.y = 0
            print 'Entrada invalida. Esperados valores reais.'
        
    def printcy(self):
        print self.getx()
        print self.gety()
        print self.getr()
        print self.geta()
        
    def geta(self):
        return self.alt

    def volume(self):
        return self.area() * self.geta()
    
    def area(self):
        return self.area() * 2 + 2 * 3.141592 * self.raio * self.alt

    def __str__(self):
        return '(alt = %f, raio = %f, x = %f, y = %f)' % (self.geta(), self.getr(), self.getx(), self.gety())

    def __add__(self, other):
        try:
            if (other.__class__ == Cylinder().__class__):
                return Cylinder(self.geta() + other.geta(),
                                self.getr() + other.getr(),
                                self.getx() + other.getx(),
                                self.gety() + other.gety())
            elif (other.__class__ == Circle().__class__):
                return Cylinder(self.geta(),
                                self.getr() + other.getr(),
                                self.getx() + other.getx(),
                                self.gety() + other.gety())
            elif (other.__class__ == Ponto().__class__):
                return Cylinder(self.geta(),
                                self.getr(),
                                self.getx() + other.getx(),
                                self.gety() + other.gety())
            elif ((type(other) == type(1)) or (type(other) == type(1.0))):
                return Circle(self.geta() + other,
                              self.getr(),
                              self.getx(),
                              self.gety())
            else:
                print 'Esperado: Cylinder(a1, r1, x1, y1) + Cylinder(a2, r2, x2, y2) ou'
                print '          Cylinder(a1, r1, x1, y1) + Circle(r2, x2, y2) ou'
                print '          Cylinder(a1, r1, x1, y1) + Ponto(x2, y2) ou'
                print '          Cylinder(a1, r1, x1, y1) + Float(r2).'
        except Exception:
                print 'Esperado: Cylinder(a1, r1, x1, y1) + Cylinder(a2, r2, x2, y2) ou'
                print '          Cylinder(a1, r1, x1, y1) + Circle(r2, x2, y2) ou'
                print '          Cylinder(a1, r1, x1, y1) + Ponto(x2, y2) ou'
                print '          Cylinder(a1, r1, x1, y1) + Float(r2).'
        
    def __sub__(self, other):
        try:
            if (other.__class__ == Cylinder().__class__):
                return Cylinder(self.geta() - other.geta(),
                                self.getr() - other.getr(),
                                self.getx() - other.getx(),
                                self.gety() - other.gety())
            elif (other.__class__ == Circle().__class__):
                return Cylinder(self.geta(),
                                self.getr() - other.getr(),
                                self.getx() - other.getx(),
                                self.gety() - other.gety())
            elif (other.__class__ == Ponto().__class__):
                return Cylinder(self.geta(),
                                self.getr(),
                                self.getx() - other.getx(),
                                self.gety() - other.gety())
            elif ((type(other) == type(1)) or (type(other) == type(1.0))):
                return Circle(self.geta() - other,
                              self.getr(),
                              self.getx(),
                              self.gety())
            else:
                print 'Esperado: Cylinder(a1, r1, x1, y1) - Cylinder(a2, r2, x2, y2) ou'
                print '          Cylinder(a1, r1, x1, y1) - Circle(r2, x2, y2) ou'
                print '          Cylinder(a1, r1, x1, y1) - Ponto(x2, y2) ou'
                print '          Cylinder(a1, r1, x1, y1) - Float(r2).'
        except Exception:
                print 'Esperado: Cylinder(a1, r1, x1, y1) - Cylinder(a2, r2, x2, y2) ou'
                print '          Cylinder(a1, r1, x1, y1) - Circle(r2, x2, y2) ou'
                print '          Cylinder(a1, r1, x1, y1) - Ponto(x2, y2) ou'
                print '          Cylinder(a1, r1, x1, y1) - Float(r2).'

    def __mul__(self, other):
        try:
            if (other.__class__ == Cylinder().__class__):
                return (self.geta() * other.geta() +
                        self.getr() * other.getr() +
                        self.getx() * other.getx() +
                        self.gety() * other.gety())
            elif ((type(other) == type(1.0)) or type(other) == type(1)):
                return Cylinder(other * self.geta(),
                                other * self.getr(),
                                other * self.getx(),
                                other * self.gety())
            else:
                print 'Esperado: Cylinder(a1, r1, x1, y1) * Cylinder(a2, r2, x2, y2) ou'
                print '          Cylinder(a1, r1, x1, y1) * Float(x) ou'
                print '          Float(x) * Cylinder(a1, r1, x1, y1).'
        except Exception:
                print 'Esperado: Cylinder(a1, r1, x1, y1) * Cylinder(a2, r2, x2, y2) ou'
                print '          Cylinder(a1, r1, x1, y1) * Float(x) ou'
                print '          Float(x) * Cylinder(a1, r1, x1, y1).'

    def __rmul__(self, other):
        try:
            return Cylinder(other * self.geta(),
                            other * self.getr(),
                            other * self.getx(),
                            other * self.gety())
        except Exception:
            print 'Esperado: Cylinder(a1, r1, x1, y1) * Cylinder(a2, r2, x2, y2) ou'
            print '          Cylinder(a1, r1, x1, y1) * Float(x) ou'
            print '          Float(x) * Cylinder(a1, r1, x1, y1).'

    def __div__(self, other):
        try:
            if (other.__class__ == Cylinder().__class__):
                return (self.geta() / other.geta() +
                        self.getr() / other.getr() +
                        self.getx() / other.getx() +
                        self.gety() / other.gety())
            elif ((type(other) == type(1.0)) or type(other) == type(1)):
                return Cylinder(self.geta() / float(other),
                                self.getr() / float(other),
                                self.getx() / float(other),
                                self.gety() / float(other))
            else:
                print 'Esperado: Cylinder(a1, r1, x1, y1) / Cylinder(a2, r2, x2, y2) ou'
                print '          Cylinder(a1, r1, x1, y1) / Float(x) ou'
                print '          Float(x) / Cylinder(a1, r1, x1, y1).'
        except Exception:
            print 'Esperado: Cylinder(a1, r1, x1, y1) / Cylinder(a2, r2, x2, y2) ou'
            print '          Cylinder(a1, r1, x1, y1) / Float(x) ou'
            print '          Float(x) / Cylinder(a1, r1, x1, y1).'

    def __rdiv__(self, other):
        try:
            return Cylinder(float(other) / self.getr(),
                            float(other) / self.getx(),
                            float(other) / self.gety())
        except Exception:
            print 'Esperado: Cylinder(a1, r1, x1, y1) / Cylinder(a2, r2, x2, y2) ou'
            print '          Cylinder(a1, r1, x1, y1) / Float(x) ou'
            print '          Float(x) / Cylinder(a1, r1, x1, y1).'

a = Cylinder()
b = Cylinder()
c = a + b
c.printcy()
c += 3

# ERRO 1 5 10
# ERRO 1 6 10
# ERRO 1 7 10
# ERRO 1 8 10
# ERRO 1 9 10
# ERRO 1 10 10
# ERRO 1 11 10
# ERRO 1 12 10
