#Andreza Miqueletti  3672701
#Alexandre Viriato   3167972
#Rodrigo Oshiro      3528863

class Ponto:
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
    def set_ponto(self,x,y):
        self.x = x
        self.y = y
    def get_x(self):
        return self.x
    def get_y(self):
        return self.y
    def __add__(self,other):
        return Ponto(self.x+other.x,self.y+other.y)
    def __sub__(self,other):
        return Ponto(self.x-other.x,self.y-other.y)
    def __mul__(self,other):
        return self.x*other.x+self.y*other.y
    def __rmul__(self,other):
        return Ponto(self.x*other,self.y*other)
    def __div__(self,other):
        try:
            self.x/other.x+self.y/other.y
        except ZeroDivisionError:
            print "Erro de divisao por zero"  
        else:
            return self.x/other.x+self.y/other.y
    def __rdiv__(self,other):
        try:
            self.x/other+self.y/other
        except ZeroDivisionError:
            print "Erro de divisao por zero"  
        else:
            return Ponto(self.x/other,self.y/other)

# ERRO 1 1 75
# ERRO 1 1 75
# ERRO 1 1 50
# ERRO 1 1 75

class Circle(Ponto):
    def __init__(self,raio=1,x=0,y=0):
        Ponto.__init__(self,x,y)
        self.raio = raio
    def printc(self):
        print self.get_x()
        print self.get_y()
        print self.raio
    def area(self):
        return 3.141592*self.raio*self.raio
    def set_circ(self,p):
        self.x = p.x
        self.y = p.y
    def __add__(self,other):
        return Circle(self.raio+other.raio,self.x+other.x,self.y+other.y)
    def __sub__(self,other):
        return Circle(self.raio-other.raio,self.x-other.x,self.y-other.y)
    def __mul__(self,other):
        return Circle(self.raio*other.raio,self.x*other.x,self.y*other.y)
    def __rmul__(self, other):
        return Circle(self.raio*other,self.x*other,self.y*other)
    def __div__(self, other):
        try:
            c = Circle(self.raio/other.raio, self.x/other.x, self.y/other.y)
        except ZeroDivisionError:
            print "Erro de divisao por zero"
            c = self
        return c
    def __idiv__(self, other):
        try:
            c = Circle(self.raio/other, self.x/other, self.y/other)
        except ZeroDivisionError:
            print "Erro de divisao por zero"
            c = self
        return c

# ERRO 1 5 75
# ERRO 1 6 75
# ERRO 1 7 50
# ERRO 1 8 75
        
class Cilinder(Circle):
    def __init__(self,alt=1,raio=1,x=0,y=0):
        Circle.__init__(self,raio,x,y)
        self.alt = alt
    def printcy(self):
        print self.get_x()
        print self.get_y()
        print self.raio
        print self.alt
    def volume(self):
        return self.area()*self.alt
    def area(self):
        return self.area()*2+2*3.141592*self.raio*self.alt
    def __add__(self, other):
        return Cilinder(self.alt+other.alt, self.raio+other.raio, self.x+other.x, self.y+other.y)
    def __sub__(self,other):
        return Cilinder(self.alt-other.alt, self.raio-other.raio, self.x-other.x, self.y-other.y)
    def __mul__(self, other):
        return Cilinder(self.alt*other.alt, self.raio*other.raio, self.x*other.x, self.y*other.y)
    def __rmul__(self, other):
        return Cilinder(self.alt*other, self.raio*other, self.x*other, self.y*other)
    def __div__(self, other):
        try:
            c = Cilinder(self.alt/other.alt, self.raio/other.raio, self.x/other.x, self.y/other.y)
        except ZeroDivisionError:
            print "Erro de divisao por zero"
            c = self
        return c
    def __idiv__(self, other):
        try:
            c = Cilinder(self.alt/other, self.raio/other, self.x/other, self.y/other)
        except ZeroDivisionError:
            print "Erro de divisao por zero"
            c = self
        return c
 
# ERRO 1 9 75
# ERRO 1 10 75
# ERRO 1 11 50
# ERRO 1 12 75

# ERRO 1 13 50

a = Cilinder()
b = Cilinder()
c = a / b
c += 2 
