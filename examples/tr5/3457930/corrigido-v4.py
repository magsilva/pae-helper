# Alessandro G. Krempi


class Ponto:
    def __init__(self, x = 1, y = 1):
        self.x = x
        self.y = y
        try : self.x/self.y, self.y/self.x
        except (ZeroDivisionError,TypeError ), message : print message
        
    def set_ponto(self, x ,y):
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
    def __rmul__(self, other):
        return Ponto(other * self.x, other * self.y)
    def __div__(self, other):
        return Ponto(self.x/other.x, self.y/other.y)

# ERRO 1 1 75
# ERRO 1 2 75
# ERRO 1 3 75
# ERRO 1 4 75

class Circle(Ponto):
    ValueNegativeError = ''
    def __init__(self, raio = 1, x = 1, y = 1):
        Ponto.__init__(self, x, y)
        self.raio = raio
        try :
            if  self.raio/1 < 0 :
                raise ValueNegativeError,'negative value'
        except ValueNegativeError, message: print message
        
    def printc(self):
        print self.getx()
        print self.gety()
        print self.raio
    def area(self):
        return 3.141592*self.raio*self.raio
    def set_circ(self, p):
        self.x = p.x
        self.y = p.y
    def __add__(self, other):
        return Circle(self.raio + other.raio, self.x, self.y)
    def __sub__(self, other):
        return Circle(self.raio - other.raio, self.x, self.y)
    def __mul__(self, other):
        return Circle(self.raio * other.raio, self.x, self.y)
    def __rmul__(self, other):
        return Circle(other * self.raio, self.x, self.y)
    def __div__(self, other):
        return Circle(self.raio/other.raio, self.x, self.y)

# ERRO 1 1 75
# ERRO 1 2 75
# ERRO 1 3 75
# ERRO 1 4 75

class Cylinder(Circle):
    ValueNegativeError = ''
    def __init__(self, alt = 1, raio = 1, x = 1, y = 1):
        Circle.__init__(self, raio, x, y)
        self.alt = alt
        try :
            if  self.alt/1 < 0 :
                raise ValueNegativeError,'negative value'
        except ValueNegativeError, message: print message
    
    def printcy(self):
        print self.getx()
        print self.gety()
        print self.raio
        print self.alt
    def volume(self):
        return self.area() * self.alt
    def area(self):
        return self.area()*2 + 2* 3.141592*self.raio*self.alt
    def __add__(self, other):
        return Cylinder(self.alt + other.alt, self.raio + other.raio, self.x, self.y)
    def __sub__(self, other):
        return Cylinder(self.alt - other.alt, self.raio - other.raio, self.x, self.y)
    def __mul__(self, other):
        return Cylinder(self.alt * other.alt, self.raio * other.raio, self.x, self.y) 
    def __rmul__(self, other):
        return Cylinder(other * self.alt, other * self.raio, self.x, self.y)
    def __div__(self, other):
        return Cylinder(self.alt/other.alt, self.raio/other.raio, self.x, self.y)

# ERRO 1 1 75
# ERRO 1 2 75
# ERRO 1 3 75
# ERRO 1 4 75

a = Cylinder()
b = Cylinder()
c = a + b
c.printcy()
c += 1

# ERRO 1 14 15
