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
# ERRO 1 4 50

    def __rmul__(self, other):
        return Ponto(other*self.x, other*self.y)

    def __div__(self, other):
        return self.x / other.x - self.y / other.y

    def __rdiv__(self, other):
        return Ponto(other/self.x, other/self.y)

class Circle(Ponto):
    def __init__(self, raio=1, x=0, y=0):
        Ponto.__init__(self, x, y)
        self.raio = raio

    def printc(self):
        print self.getx()
        print self.gety()
        print self.raio()

    def area(self):
        return 3.141592*self.raio*self.raio

    def set_circ(self, p):
        self.x = p.x
        self.y = p.y
        
    def __add__(self, other):
            try:
                self + other
            except:
                return "ouutro"
            else:
                return self.raio + other.raio

    def __sub__(self, other):
        return Ponto(self.x - other.x, self.y - other.y, self.raio - other.raio)

# ERRO 1 5 100
# ERRO 1 7 100
# ERRO 1 8 100
# ERRO 1 6 100

    def __mul__(self, other):
        return self.x * other.x + self.y * other.y + self.raio * other.raio

    def __rmul__(self, other):
        return Ponto(other*self.x, other*self.y, self.raio*other)

    def __div__(self, other):
        return self.x / other.x - self.y / other.y

    def __rdiv__(self, other):
        return Ponto(other/self.x, other/self.y)


class Cylinder(Circle):
    def __init__(self, alt = 1, raio = 1, x = 0, y = 0):
        Circle.__init__(self,raio,x,y)
        self.alt = alt

    def printcy(self):
        print self.getx()
        print self.gety()
        print self.raio()
        print self.alt()

    def volume(self):
        return self.area() * self.alt

    def area(self):
        return self.area()*2 + 2*3.141592*self.raio*self.alt

    def __add__(self, other):
        return Ponto(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Ponto(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return self.x * other.x + self.y * other.y

    def __rmul__(self, other):
        return Ponto(other*self.x, other*self.y)

    def __div__(self, other):
        return self.x / other.x - self.y / other.y

    def __rdiv__(self, other):
        return Ponto(other/self.x, other/self.y)

# ERRO 1 9 100
# ERRO 1 10 100
# ERRO 1 11 100
# ERRO 1 12 100
# ERRO 1 13 90
# ERRO 1 14 100
    
        
