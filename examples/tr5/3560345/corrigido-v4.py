###### LISTA 5 #######
#Nomes:
#Cleber Castro Hage ........ Nro USP: 3560345
#Glauco Becaro ........Nro USP: 2955079
#OBS: Todas as condicoes de existencia foram levadas em conta para todos os atributos



class Ponto:
    def __init__(self,x=0, y=0):
        self.x=x
        self.y=y
    def set_ponto(self, x, y):
        self.x=x
        self.y=y
    def get_x(self):
        return self.x
    def get_y(self):
        return self.y
    def __add__(self,other):
        try:
            return Ponto(self.x + other.x, self.y + other.y)
        except Exception, E:
            print 'Nao pode'
    def __sub__(self,other):
        try:
            return Ponto(self.x - other.x, self.y - other.y)
        except Exception, E:
            print 'Nao pode'
    def __mul__(self, other):
        try:
            return Ponto(self.x * other.x, self.y * other.y)
        except Exception, E:
            print 'Nao pode'
    def __div__(self, other):
        try:
            return Ponto(self.x / other.x, self.y / other.y)
        except Exception, E:
            print 'Nao pode'
    def __rmul__(self, other):
        try:
            return Ponto(other * self.x  , other * self.y)
        except Exception, E:
            print 'Nao pode'
    def __rdiv__(self, other):
        try:
            return Ponto(other / self.x  , other / self.y)
        except Exception, E:
            print 'Nao pode'
class Circle(Ponto):
    def __init__(self, raio, x=0, y=0):
        Ponto.__init__(self, x, y)
    def set_raio(raio):
        if self.raio >= 0:
            self.raio = raio
        self.raio = raio
    def printc (self):
        print self.getx( )
        print self.gety( )

        print self.raio
    def area(self):
        return 3.141592*self.raio*self.raio
    def set_circ(self, p):
        self.x=p.x
        self.y=p.y
    def __addcircle__(self,other,r):
        try:
            if r>=0:
                return Circle(Ponto(self.x + other.x, self.y + other.y),self.raio + r)
        except Exception, E:
            print 'Nao pode'
    def __subcircle__(self,other,r):
        try:
            if (self.raio > r) and (r>=0):
                return Circle(Ponto(self.x - other.x, self.y - other.y),self.raio - r)
        except Exception, E:
            print 'Nao pode'
    def __mulcircle__(self, other):
        try:
            if r>=0:
                return Circle(Ponto(self.x * other.x, self.y * other.y),self.raio * r)
        except Exception, E:
            print 'Nao pode'
    def __divcircle__(self, other):
        try:
            if r>0:
                return Circle(Ponto(self.x / other.x, self.y / other.y),self.raio / r)
        except Exception, E:
            print 'Nao pode'
    def __rmulcircle__(self, other):
        try:
            if r>=0:
                return Circle(Ponto(other * self.x  , other * self.y),self.raio * r)
        except Exception, E:
            print 'Nao pode'
    def __rdivcircle__(self, other):
        try:
            if r>0:
                return Circle(Ponto(other / self.x  , other / self.y),self.raio / r)
        except Exception, E:
            print 'Nao pode'

# ERRO 1 5 10
# ERRO 1 6 10
# ERRO 1 7 10
# ERRO 1 8 10

class Cylinder(Circle):
    def __init__(self, altura =1, raio = 1, x=0,y=0):
        Circle.__init__(self, raio,x,y)
        self.altura=altura
    def set_raio(self, raio):
        if raio > 0:
            self.raio=raio
    def set_altura(self, altura):
        if altura > 0:
            self.altura=altura
    def printcy(self):
        print self.get_x()
        print self.get_y()
        print self.raio
        print self.alt
    def volume(self):
        return (self.area() * self.alt)
    def area(self):
        return (self.area()*2 + 2*141592*self.raio*self.alt)
    def addAltura(self, other):
        return alt - alt + other
    def __addcilin__(self,other,r,H):
        try:
            if (r>=0) and (H>=0):
                return Cylinder(Ponto(self.x + other.x, self.y + other.y),self.raio + r, self.altura + H)
        except Exception, E:
            print 'Nao pode'
    def __subcilin__(self,other,r,H):
        try:
            if (self.raio > r) and (r>=0) and (self.altura >= H)and (H>=0):
                return Cylinder(Ponto(self.x - other.x, self.y - other.y),self.raio - r, self.altura - H)
        except Exception, E:
            print 'Nao pode'
    def __mulcilin__(self, other,r,H):
        try:
            if (r>=0) and (H>=0):
                return Cylinder(Ponto(self.x * other.x, self.y * other.y),self.raio * r, self.altura * H)
        except Exception, E:
            print 'Nao pode'
    def __divcilin__(self, other,r,H):
        try:
            if (r>0) and (H>0):
                return Cylinder(Ponto(self.x / other.x, self.y / other.y),self.raio / r, self.altura / H)
        except Exception, E:
            print 'Nao pode'
    def __rmulcilin__(self, other,r,H):
        try:
            if (r>=0) and (H>=0):
                return Cylinder(Ponto(other * self.x  , other * self.y),self.raio * r, self.altura * H)
        except Exception, E:
            print 'Nao pode'
    def __rdivcilin__(self, other,r,H):
        try:
            if (r>0) and (H>0):
                return Cylinder(Ponto(other / self.x  , other / self.y),self.raio / r, self.altura / H)
        except Exception, E:
            print 'Nao pode'

# ERRO 1 9 50 Usou Circle ao invés de Cylinder
# ERRO 1 10 50
# ERRO 1 11 50
# ERRO 1 12 50

# ERRO 1 14 50

a = Cylinder()
b = Cylinder()
c = a * b
c.printcy()
c += 3
