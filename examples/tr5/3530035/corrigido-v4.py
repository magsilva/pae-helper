# ALUNOS Sergio P. Rossi 3530035  e Rafael Henrique Manoel 3285310 ##

### CLASSE PONTO ### 
class ponto: 
    def __init__(self, x = 0, y = 0): 
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
        return ponto(self.x + other.x, self.y + self.y) 
 
    def __mul__(self, other): 
        return self.x * other.x + self.y * self.y 
 
    def __rmul__(self, other): 
        return ponto(other * self.x, other * self.y)

    def __sub__(self, other):
        return ponto(self.x - other.x, self.y - other.y)

    def __rdiv__(self, other) :
        return ponto(self.x/other, self.y/other)

# ERRO 1 1 75
# ERRO 1 2 75
# ERRO 1 3 75
# ERRO 1 4 75
    
### CLASSE CIRCULO ###
class circle(ponto): 
    def __init__(self, raio = 1, x = 0, y = 0): 
        ponto.__init__(self,x, y ) 
        self.raio = raio 
 
    def printc(self): 
        print self.getx() 
        print self.gety() 
        print self.raio 
 
    def area(self): 
        return 3.141592 * self.raio * self.raio 
 
    def set_circ(self, p): 
        self.x = p.x 
        self.y = p.y 

    def __add__(self, other):
	try:
	    a = self.raio + other.raio
	    return circle(a,self.x,sel.y)
	except TypeError:
	    print " Nao foi possivel adicionar. "

    def __sub__(self, other):
	try:
	    a = self.raio - other.raio
	    return circle(a, self.x, self.y)
	except TypeError:
	    print " Nao foi possivel subtrair. "
	    
  
    def __mul__(self, other):
	try:
	    a = self.raio * other.raio
            return circle(a, self.x, self.y)
        except TypeError:
	    print "Nao foi possivel fazer a multiplicacao."
	    

    def __rmul__(self, other):
	try:
	    a = other * self.raio
	    return circle(a, sel.x, self,y)
	except TypeError:
	    print "Nao foi possivel fazer a multiplicacao."

    def __rdiv__(self, other):
	try:
	    a = self.raio/other.raio
            return circle(a, self.x, self.y)
        except ZeroDivisionError:
		print "Nao eh possivel dividir por zero"

    def __div__(self, other):
	try:
	    a = self.raio/other
	    return circle(a,self.x, self.y)
	except ZeroDivisionError:
	     print " Nao eh possivel dividir por zero"

# ERRO 1 5 75
# ERRO 1 6 75
# ERRO 1 7 75
# ERRO 1 8 75
    
###  CLASSE CILINDRO ###        
class cylinder(circle): 
    def __init__(self, alt = 1, raio = 1, x = 0, y = 0): 
        Circle.__init__(self, raio, x, y) 
        self.alt = alt 
 
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
        return cylinder(self.alt + other.alt, circle.__add__(other))

    def __sub__(self, other):
        return cylinder(self.alt - other.alt,self.raio - other.raio, self.x, self.y)

    def __mul__(self, other):
        try:
	    a = self.alt * other.alt
	    b = self.raio * other.raio
            return cylinder(a,b, self.x, self.y)
        except ValueError:
	    print " Nao foi possivel fazer a multiplicacao "

    def __rmul__(self, other):
        try:
	    a = self.alt * other
	    b = self.raio * other
            return cylinder(a,b, self.x, self.y)
        except ValueError:
	    print " Nao foi possivel fazer a multiplicacao "

    def __rdiv__(self, other):
	try :
	    a = self.alt / other
	    b = self.raio / other
            return cylinder(a,b, self.x, self.y)
        except ZeroDivisionError:
	   print "Nao foi possivel fazer a divisao"
	    
    def __div__(self, other):
        try :
	    a = self.alt / other.alt
	    b = self.raio / other.raio
            return cylinder(a,b, self.x, self.y)
        except ZeroDivisionError:
	   print "Nao foi possivel fazer a divisao"

# ERRO 1 9 75
# ERRO 1 10 75
# ERRO 1 11 75
# ERRO 1 12 75

a = cylinder()
a *= 2

# ERRO 1 14 50
