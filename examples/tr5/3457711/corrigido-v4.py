from __future__ import division
import math;
class ponto:
    def __init__(self, x=0, y=0):
        self.x =x;
        self.y = y;

    def set_ponto(self, x,y):
        self.x = x;
        self.y = y;
        
    def get_x (self):
        return self.x;

    def get_y (self):
        return self.y;

    def  __radd__ (self, other):
        raise NonSense;
    
    def __add__ (self, other):
        return ponto(self.x + other.x, self.y + other.y);

    def __sub__ (self, other):
        return ponto(self.x - other.x, self.y - other.y);

    def __rmul__(self, other):
        raise NonSense;

    def __mul__(self, other):
        return ponto(other.x*self.x, other.y*self.y);


    def __rdiv__(self, other):
        raise NonSense;
    
    def __div__(self, other):
        raise NonSense;

# ERRO 1 1 75
# ERRO 1 2 75
# ERRO 1 3 100
# ERRO 1 4 75

class circle(ponto):
    def __init__(self, raio = 1, x = 0, y = 0):
        if (raio <= 0):
            raise OutOf2D;
        ponto.__init__(self, x, y);
        self.raio = raio;
        
    def printc(self):
        print self.get_x();
        print self.get_y();
        print self.raio;

    def area(self):
        return math.pi*self.raio**2

    def set_circle(self,p):
        self.x = p.x;
        self.y = p.y;

    def __add__(self, other):
        if ((self.x == other.x) and (self.y == other.y)):
            return circle(self.raio+other.raio, self.x, self.y);
        else:
            raise NotSameCenter;
        
    def __sub__(self, other):
        if ((self.x == other.x) and (self.y == other.y)):
            return circle(self.raio-other.raio, self.x, self.y);
        else:
            raise NotSameCenter;

    def __mul__(self, other):
        if ((self.x == other.x) and (self.y == other.y)):
            return circle(self.raio*other.raio, self.x, self.y);
        else:
            raise NotSameCenter;
      
    def __rmul__(self, other):
        raise NonSense;

    def __rdiv__(self, other):
        raise NonSense;
    
    def __div__(self, other):
        raise NonSense;


# ERRO 1 5 75
# ERRO 1 6 75
# ERRO 1 7 100
# ERRO 1 8 75





class cylinder(circle):
    def __init__(self, alt = 1, raio = 1, x = 0, y = 0):
        if (alt <= 0):
            raise OutOf3D;
        circle.__init__(self, raio, x, y);
        self.alt = alt;
    def printcy(self):
        print self.get_x();
        print self.get_y();
        print self.raio;
        print self.alt;
    def volume(self):
        return self.area()*self.alt;
    def area(self):
        return self.area()*2 + 2*math.pi * self.raio*self.alt;
    
    def __add__(self, other):
        if ((self.x == other.x) and (self.y == other.y) and (self.raio == other.raio)):
            return cylinder(self.alt +  other.alt, self.raio, self.x, self.y);
        else:
            raise NotSameCenterOrRaio;
        
    def __sub__(self, other):
        if ((self.x == other.x) and (self.y == other.y) and (self.raio == other.raio)):
            return cylinder(self.alt -  other.alt, self.raio, self.x, self.y);
        else:
            raise NotSameCenterOrRaio;
        

    def __mul__(self, other):
        if ((self.x == other.x) and (self.y == other.y) and (self.raio == other.raio)):
            return cylinder(self.alt *  other.alt, self.raio, self.x, self.y);
        else:
            raise NotSameCenterOrRaio;
        
      
    def __rmul__(self, other):
        raise NonSense;

    def __rdiv__(self, other):
        raise NonSense;
    
    def __div__(self, other):
        raise NonSense;

# ERRO 1 9 75
# ERRO 1 10 75
# ERRO 1 11 100
# ERRO 1 12 75

a = cylinder(10, 3, 8, 2)
b = cylinder(5, 3, 1, 2)
a.printcy()
b.printcy()
try:
    c = a * b
except:
    print " You fuckin' Dumb"
c.printcy()
a +- 1
