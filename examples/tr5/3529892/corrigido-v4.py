"""
Exercicio POO - profa. Renata Pontin
Sobrecarga de funcao e polimorfismo

Lucas Shindi Shimo - 3529892 - lshimo@grad.icmc.usp.br
Marcelo Kenji Hotta - 3460142 - kenji@grad.icmc.usp.br
"""



import math

class Ponto:
    def __init__(self, x=0,y=0):
        try:
            self.x = float(x)            
            self.y = float(y)
        except:
            print "Coordenadas Invalidas"
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
            print "A soma deve ser entre dois pontos validos"
    def __mul__(self,other):
        if (other.__class__ == Ponto):
            return self.x*other.x + self.y * other.y
        else:
            print "Multiplicacao escalar deve ser entre dois ponto validos"
    def __rmul__(self,other):
        try:
            float(other)
            return Ponto(other*self.x,other*self.y)
        except:
            "Multiplicacao por escalar invalida"
    def __div__(self,other):
        try:
            float(other)
            if(other == 0):
                print "Divizao por zero"
            else:
                return Ponto(self.x/other,self.y/other)
        except:
            print "Divisor escalar invalido"
    def __str__(self):
        return "(%.3f,%.3f)"%(self.x,self.y)


class Circle(Ponto):
    def __init__(self,raio=1,x=0,y=0):
        Ponto.__init__(self,x,y)
        try:
            self.raio = float(raio)
        except:
            print "Valor do raio invalido"
    def printc (self):
        print self.get_x()
        print self.get_y()
        print self.raio
    def area(self):
        return 3.141592*self.raio*self.raio
    def set_circ(self,p):
        try:
            self.x = p.x
            self.y = p.y
        except:
            print "Ponto dado invalido"
    def __str__(self):
        return "(x-%.3f)**2 + (y - %.3f)**2 = %.3f**2"%(self.x,self.y,self.raio)

    def __add__(self,other): #como somar circulos? -> inventar
        try:    
            aux_x = self.x + other.x
            aux_y = self.y + other.y
            aux_r = math.sqrt(self.raio**2 + other.raio**2)
            return Circle(aux_r,aux_x,aux_y)
        except:
            print "Deve ser dado um cilindro valido"
    def __sub__(self,other): #idem
        try:
            aux_x = self.x - other.x
            aux_y = self.y - other.y
            aux_r = math.sqrt(self.raio**2 - other.raio**2)
            return Circle(aux_r,aux_x,aux_y)
        except ValueError:
            print "Valor de retorno negativo"
        except AttributeError:
            print "Deve ser dado um circulo valido"
    def __mul__(self,other): #affe.. sem ideia..
        if(other.__class__ == Circle):
            return self.x*other.x + self.y*other.y + self.raio*other.raio
        else:
            print "Deve ser dada um circulo valido"

    def __rmul__(self,other): #esse dah para ter ideia
        try:
            float(other)
            return Circle(self.raio*other,self.x*other,self.y*other)
        except:
            print "Multiplicacao por escalar invalida"
    def __div__(self,other):
        try:
            float(other)
            if(other == 0):
                print "Divizao por zero"
            else:
                return Circle(self.raio/other,self.x/other,self.y/other)
        except:
            print "Divisor escalar invalido"
                  
class Cylinder(Circle):
    def __init__(self,alt=1,raio=1,x=0,y=0):
        Circle.__init__(raio,x,y)
        try:
            self.alt = alt
        except:
            print "Valor da altura invalido"            
    def printcy(self):
        print self.get_x()
        print self.get_y()
        print self.raio
        print self.alt
    def volume(self):
        return self.area()*self.alt
    def area(self):
        return self.area()*2 + 2*3.141592*self.raio.self.alt
    def __add__(self,other):
        try:
            a=Circle(self.raio,self.x,self.y)
            b=Cirlce(other.raio,other.x,other.y)
            aux_alt = math.pow(self.alt**3 + other.alt**3, 1/3)
            return Cylinder(aux_alt,(a+b).raio,(a+b).x,(a+b).y)
        except:
            "Deve ser dado um cilindro valido"
    def __sub__ (self,other):
        try:
            a=Circle(self.raio,self.x,self.y)
            b=Cirlce(other.raio,other.x,other.y)
            aux_alt = math.pow(self.alt**3 - other.alt**3, 1/3)
            return Cylinder(aux_alt,(a-b).raio,(a-b).x,(a-b).y)
        except ValueError:
            print "Valor de retorno negativo"
        except AttributeError:
            print "Deve ser dado um cilindro valido"

    def __rmul__(self,other): #esse dah para ter ideia
        try:
            float(other)
            return Cylinder(self.alt*other, self.raio*other,self.x*other,self.y*other)
        except:
            print "Multiplicacao por escalar invalida"
    def __div__(self,other):
        try:
            float(other)
            if(other == 0):
                print "Divizao por zero"
            else:
                return Cylinder(self.alt/other, self.raio/other,self.x/other,self.y/other)
        except:
            print "Divisor escalar invalido"


# ERRO 1 5 10
# ERRO 1 6 10
# ERRO 1 7 10
# ERRO 1 8 10
# ERRO 1 9 10
# ERRO 1 10 10
# ERRO 1 11 10
# ERRO 1 12 10

# ERRO 1 14 15
