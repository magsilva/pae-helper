class ponto:
    
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y

    def set_ponto(self,x,y):
        self.x=x
        self.y=y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def __add__(self,other):
        return ponto(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return ponto(self.x - other.x, self.y - other.y)
    
    def __mul__(self,other):
        return self.x * other.x + self.y * other.y


# ERRO 1 1 50
# ERRO 1 2 50
# ERRO 1 4 50

    def __rmul__(self,other):
        return ponto(other * self.x, other * self.y)
    
    def __div__(self, other):
        print "Erro!- N√£o √© poss√≠vel divis√£o de pontos"
        return ponto(self.x, self.y)

# ERRO 1 3 100

class circle(ponto):
    
    def __init__(self, raio=1, x=0, y=0):
        ponto.__init__(self,x,y)
        self.raio=raio
        
    def printc(self):
        print self.getx()
        print self.gety()
        print self.raio
        
    def area(self):
        return 3.141592 * self.raio * self.raio
    
    def set_circ(self,p):
        self.x=p.x
        self.y=p.y
        
    def __add__(self, other):
        return circle((self.raio + other.raio), self.x, self.y)

# ERRO 1 5 75 N„o trata caso o objeto n„o seja do tipo Circle.
    
    def __sub__(self, other):
        if ((other.raio <> self.raio) and (other.raio < self.raio)):
            return circle ((self.raio - other.raio), self.x, self.y)
        else:
            print "Erro!- O valor do raio eh maior ou igual ao outro raio"
            return circle (self.raio, self.x, self.y)

# ERRO 1 6 75 N„o trata caso o objeto n„o seja do tipo Circle.
        
    def __rsub__(self, other):
        if ((other <> self.raio) and (other < self.raio)):
            return circle ((self.raio - other), self.x, self.y)
        else:
            print "Erro!- O valor digitado eh maior ou igual ao raio"
            return (self.raio, self.x, self.y)

    def __mul__(self, other):
        if other.raio > 0:
            return circle((self.raio * other.raio), self.x, self.y)
        else:
            print "Erro!- O valor do raio È negativo ou igual a zero"
            return circle(self.raio, self.x, self.y)

# ERRO 1 8 75

    def __rmul__(self, other):
        if other > 0:
            return circle((self.raio * other), self.x, self.y)
        else:
            print "Erro!- O valor do raio È negativo ou igual a zero"
            return circle(self.raio, self.x, self.y)

    def __div__(self, other):
        if other.raio > 0:
            return circle((self.raio / other.raio), self.x, self.y)
        else:
            print "Erro!- O valor do raio È zero ou menor que zero"
            return circle(self.raio, self.x, self.y)

# ERRO 1 7 75

    def __rdiv__(self, other):
        if other > 0:
            return circle((self.raio / other), self.x, self.y)
        else:
            print "Erro!- O valor do raio È zero ou menor que zero"
            return circle(self.raio, self.x, self.y)

class cylinder(circle):
    
    def __init__(self, alt=1, raio=1, x=0, y=0):
        circle.__init__(self, raio, x,y)
        self.alt=alt
        
    def printcy(self):
        print self.getx()
        print self.gety()
        print self.raio
        print self.alt
        
    def volume(self):
        return self.area() * self.alt
    
    def area(self):
        return self.area() * 2 + 2 * 3.141592 * self.raio * self.alt

    def __add__(self, other):
        return cylinder((self.alt + other.alt), self.raio, self.x, self.y)

# ERRO 1 9 75

    def __sub__(self, other):
        if ((other.alt <> self.alt) and (other.alt < self.alt)):
            return cylinder((self.alt - other.alt), self.raio, self.x, self.y)
        else:
            print "Erro!- A altura digitada È maior ou igual √† altura"
            return cylinder(self.alt, self.raio, self.x, self.y)

# ERRO 1 10 75

    def __mul__(self, other):
        if other.alt > 0:
	    return cylinder ((self.alt * other.alt), self.raio, self.x, self.y)
        else:
            print "Erro!- A altura digitada È menor ou igual a zero"
            return cylinder(self.alt, self.raio, self.x, self.y)

    def __rmul__(self, other):
        if other > 0:
	    return cylinder ((other * self.alt), self.raio, self.x, self.y)
        else:
            print "Erro!- A altura digitada È menor ou igual a zero"
            return cylinder(self.alt, self.raio, self.x, self.y)
# ERRO 1 12 75
# ERRO 1 11 75

    def __div__(self, other):
         if ((other.alt <> self.alt) and (other.alt < self.alt)):
            return cylinder((self.alt / other.alt), self.raio, self.x, self.y)
         else:
            print "Erro!- A altura digitada È maior ou igual √† altura"
            return cylinder(self.alt, self.raio, self.x, self.y)
            
# ERRO 1 13 100

cilindro = cylinder (6, 4, 0, 0)
print "Cilindro 1: X =",cilindro.x, ", Y =",cilindro.y, ", Raio =",cilindro.raio, ", Altura =",cilindro.alt, "\n"
cilindro2 = cylinder (5, 3, 0, 0)
print "Cilindro 2: X =",cilindro2.x, ", Y =",cilindro2.y, ", Raio =",cilindro2.raio, ", Altura =",cilindro2.alt, "\n"
cilindro3 = cilindro / cilindro2
print "Cilindro 3 (Cilindro 1 / Cilindro 2): X =",cilindro3.x, ", Y =",cilindro3.y, ", Raio =",cilindro3.raio, ", Altura =",cilindro3.alt, "\n"
cilindro4 = cilindro2 * cilindro3
print "Cilindro 4 (Cilindro 2 * Cilindro 3): X =",cilindro4.x, ", Y =",cilindro4.y, ", Raio =",cilindro4.raio, ", Altura =",cilindro4.alt, "\n"
cilindro5 = cilindro4 + cilindro
print "Cilindro 5 (Cilindro 1 + Cilindro 4): X =",cilindro5.x, ", Y =",cilindro5.y, ", Raio =",cilindro5.raio, ", Altura =",cilindro5.alt, "\n"
