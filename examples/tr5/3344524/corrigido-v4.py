class Ponto:
    def __init__(self, x=0, y=0):
        try:
            self.x = float(x)            
            self.y = float(y)
        except:
            print "Coordenadas invalidas"
    def set_ponto(self,x,y):
        try:
            self.x = float(x)
            self.y = float(y)
        except:
            print "Coordenadas Invalidas"
    def get_x(self):
        return self.x
    def get_y(self):
        return self.y
    def __add__(self,other):
        if (other.__class__ == Ponto):
            return Ponto(self.x + other.x, self.y + other.y)
        else:
            print "A soma nao e valida"
    def __mul__(self, other):
        if(other.__class__ == Ponto):
            return self.x * other.x + self.y * other.y
        else:
            print "A multiplicacao nao e valida"
    def __rmul__(self, other):
        try:
            float(other)
            return Ponto(other * self.x, other * self.y)
        except typeError:
            print "Multiplicacao invalida"
        
    def __div__(self,other):
        try:
            float(other)
            if(other == 0):
                print "Divizao por zero"
            else:
                return Ponto(self.x/other,self.y/other)
        except:
            print "Nao consegue dividir"
    def __str__(self):
        return "(%.2f,%.2f)"%(self.x,self.y)

class Circle(Ponto):
    def __init__(self, raio = 1, x = 0, y = 0):
        Ponto.__init__(self,x,y)
        self.raio = raio   
    def printc(self):
        print self.get_x()
        print self.get_y()
        print self.raio
    def area(self):
        return 3.141592*self.raio*self.raio
    def set_circ(self, p):
        try:
            self.x = p.x
            self.y = p.y
        except:
            print "ponto invalido"
# ERRO 1 5 15
# ERRO 1 6 15
# ERRO 1 7 15
# ERRO 1 8 15
    def __add__(self,other):
        try:
            a = self.raio + other.raio
            x = self.x + other.x
            y = self.y + other.y 
            return Circle(a,x,y)
        except:
            print "Nao foi possivel somar dois circulos"
    def __sub__(self,other):
        try:
            b = self.raio - other.raio
            c = self.x - other.x
            d = self.y - other.y
            return Circle(b,c,d)
        except ValueError:
            print "Valor de retorno negativo"
    def __div__(self,other):
        try:
            b = self.raio/other.raio
            c = self.x/other.y
            d = self.y/other.y
            return Circle(b,c,d)
        except ZeroDivisionError:
            print "Nao foi possivel dividir dois circulos"
    def __mul__(self,other):
        if(other.__class__ == Circle):
            return self.raio*other.raio
        else:
            print "Nao foi possivel multiplicar dois circulos"
        
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
        print self.get_x()
        print self.get_y()
        print self.raio
        print self.alt
    def volume(self):
        return self.area() *self.alt
    def area(self):
        return self.area()*2 + 2*3.141592*self.raio*self.alt
    def __add__(self,other):
        try:
            a = self.alt + other.alt
            b = self.raio + other.raio
            c = self.x + other.x
            d = self.y + other.y
            return Cylinder(a,b,c,d)
        except :
            print "Nao foi possivel adicionar dois cilindros"
    def __sub__(self,other):
        try:
            b = self.alt - other.alt
            c = self.raio - other.raio
            d = self.x - other.x
            e = self.y - other.y
            if b < 0:
                raise ArithmeticError, "Valor de retorno negativo"
            else:
                return Cylinder(b,c,d,e)
        except ArithmeticError, e:
            print "Valor de retorno negativo"
        except Exception, e:
            print "Nao foi possivel subtrair dois cilindros"
            print e.value
# ERRO 1 9 15
# ERRO 1 10 15
# ERRO 1 11 15
# ERRO 1 12 15
 
    def __div__(self,other):
        try:
            b = self.raio/other.raio
            c = self.x/other.y
            d = self.y/other.y
            e = self.alt/other.alt
            return Cylinder(e,b,c,d)
        except ZeroDivisionError:
            print "Nao foi possivel dividir dois circulos"
            
    def __mul__(self,other):
            try:
                float(other)
                return Cylinder(self.alt*other,self.raio*other,self.x*other,self.y*other)
            except ValueError:
                print "Nao foi possivel multiplicar dois cilindros"
            
              
p = Ponto(4,5)
d = Ponto(5,6)
c = p + d
print c.x
print c.y
c2 = Circle(20,44,55)
c2.printc()
c3 = Circle(30,50,60)
a = c2 + c3
print a.x
print a.y
print a.raio
b = c2 - c3
print b.x
print b.y
print b.raio
c = c2 / c3
print c.x
print c.y
print c.raio
d = c2 * c3
print d
m = Cylinder(5,60,50,10)
k = Cylinder(10,100,400,30)
l = m * 'a'
h = m / k
s = m - k

# ERRO 1 14 5
