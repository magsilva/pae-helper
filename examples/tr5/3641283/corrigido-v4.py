class Ponto:

    def __init__(self, x=0, y=0):
        self.x=x
        self.y=y

    def set_ponto(self, x, y):
        self.x=x
        self.y=y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def __add__(self, other):
        return Ponto(self.x + other.x,self.y + other.y)

    def __sub__(self, other):
        try :
            x=Ponto(self.x - other.x,self.y - other.y)
	except typeerror :
            print " operacao com erro"
        else :
            return x

    def __mul__(self, other):
        return self.x * other.x + self.y * other.y

    def __rmul__(self,other):
        return Ponto(other * self.x , other * self.y)

    def __div__(self,other):
        try :
            x = Ponto(other / self.x , other / self.y)
        except TypeError :
            print " operacao com erro"
        else :
            return x


# ERRO 1 1 75
# ERRO 1 2 75
# ERRO 1 3 75
# ERRO 1 4 75

class Circle(Ponto):
    def __init__(self, raio=1, x=0, y=0):
        Ponto.__init__(self, x, y)
        self.raio=raio

    def printc (self):
        print self.getx()
        print self.gety()
        print self.raio

    def area(self):
        return 3.141592*self.raio*self.raio

    def set_circ(self,p):
        self.x=p.x
        self.y=p.y

    def __add__(self,other):
        return Circle(self.raio + other.raio)

    def __sub__(self, other):
        try :
            x = Circle(self.raio - other.raio)
        except typeerror :
            print " operacao com erro"
        else :
            return x

    def __mul__(self,other):
        return Circle(self.raio * other.raio)


    def __div__(self, other):
        try :
            x = Circle(self.raio / other.raio)
        except typeerror :
            print " operacao com erro"
        else :
            return x

# ERRO 1 5 75
# ERRO 1 6 75
# ERRO 1 7 75
# ERRO 1 8 75

class Cylinder(Circle):

    def __init__(self,alt=1, raio=1, x=0, y=0):
        circle.__init__(self, raio, x , y)
        self.alt=alt

    def printcy (self):
        print self.getx()
        print self.gety()
        print self.raio
        print self.alt

    def volume(self):
        return self.area()*self.alt

    def area(self):
        return self.area() * 2 + 2 * 3.141592 * self.raio * self.alt

    def __add__(self,other):
        return Cylinder(self.alt + other.alt)

    def __sub__(self, other):
        try :
            x = Cylinder(self.alt - other.alt)
        except typeerror :
            print " operacao com erro"
        else :
            return x

    def __mul__(self,other):
        return Cylinder(self.alt * other.alt)


    def __div__(self, other):
        try :
            x = Cylinedr(self.alt / other.alt)
        except typeerror :
            print " operacao com erro"
        else :
            return x

# ERRO 1 9 75
# ERRO 1 10 75
# ERRO 1 11 75
# ERRO 1 12 75

a = Cylinder()
b = Cylinder()
c = a / b

# ERRO 1 14 75
# ERRO 1 13 50
