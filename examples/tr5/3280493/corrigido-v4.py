# AULA PRÁTICA ? TRATAMENTO DE EXECEÇÕES ? ENTREGA 29/04/2003
# 
# Eduardo Alves Ferreira
# Eduardo Martinelli Galvão de Queiroz
# Katsumi Arackawa Junior 

class Ponto:
    def __init__( self , x=0 , y=0 ) :
        self.x = x
        self.y = y
    def setponto ( self , x , y ) :
        self.x = x
        self.y = y
    def getx ( self ) :
        return self.x
    def gety ( self ) :
        return self.y
    def __add__ ( self , other) :
        return Ponto(self.x + other.x, self.y + other.y) 
    def __sub__ ( self , other) :
        return Ponto(self.x - other.x, self.y - other.y) 
    def __mul__ ( self , other ) :
        return self.x * other.x + self.y * other.y
    def __rmul__ ( self , constante ) :
        return Ponto(constante*self.x , constante*self.y)

# ERRO 1 1 75
# ERRO 1 2 75
# ERRO 1 3 50
# ERRO 1 4 75

    def __div__ ( self , other ) :
        try :
            return Ponto ( self.x / other.x , self.y / other.y)
        except ZeroDivisionError :
            print "Divisao por zero !!!"
            return Ponto ( self.x , self.y )
# Teste da classe Ponto

PA = Ponto()
PB = Ponto(3,1)
PA.setponto(2,2)
PA += PB
print " Valores de PA = PA + PB : "
print str(PA.getx())
print str(PA.gety())

PA = 2*PA
print " 2 * PA : "
print str(PA.getx())
print str(PA.gety())

PAB = PA * PB
print "PAB = PA * PB : "
print str(PAB)

PA -= PB
print " Valores de PA = PA - PB : "
print str(PA.getx())
print str(PA.gety())

PA = PA / PB 
print " Valores de PA = PA / PB : "
print str(PA.getx())
print str(PA.gety())

# Para gerar excecao :
PB.setponto(0,0)
PA = PA / PB 
print " Valores de PA = PA / PB : "
print str(PA.getx())
print str(PA.gety())

class Circle(Ponto) :
    def __init__ ( self , raio = 1 , x = 0 , y = 0 ):
        Ponto.__init__( self , x , y )
        self.raio = raio
    def printc ( self ) :
        print self.getx()
        print self.gety()
        print self.raio
    def area ( self ) :
        return 3.141592 * self.raio * self.raio
    def setcirc ( self , p ) :
        self.x = p.x
        self.y = p.y
    def __add__ ( self , outro ) :
        return Circle( self.raio + outro.raio , self.x + outro.x , self.y + outro.y )
    def __sub__ ( self , outro ) :
        return Circle( self.raio - outro.raio , self.x - outro.x , self.y - outro.y )
    def __mul__ ( self , outro ) :
        return  self.raio*outro.raio + self.x*outro.x + self.y*outro.y
    def __div__ ( self , other ) :
        try :
            return Circle ( self.x / other.x , self.y / other.y , self.raio / other.raio)
        except ZeroDivisionError :
            print "Divisao por zero !!!"
            return Circle ( self.x , self.y , self.raio)


# ERRO 1 5 75
# ERRO 1 6 75
# ERRO 1 7 50
# ERRO 1 8 75

# Teste da classe Circle
CA = Circle()
CB = Circle(2,1,1)
print "\n"

print "Circulo CA"
CA.printc()

print "Circulo CB"
CB.printc()

CA += CB
print "Circulo CA += CB"
CA.printc()

CA -= CB
print "Circulo CA -= CB"
CA.printc()

A = CA * CB
print "Escalar A = CA * CB"
print A

CA = CA / CB
print "Circulo CA = CA / CB"
CA.printc()

CA = CB / CA
print "Circulo CA = CB / CA"
CA.printc()

class Cylinder ( Circle ):
    def __init__ (self, alt = 1 , raio = 1 , x = 0 , y = 0):
        Circle.__init__(self,x,y)
        self.alt = alt
    def printcy (self):
        print self.getx()
        print self.gety()
        print self.raio
        print self.alt
    def volume (self):
        return self.area()*self.alt
    def carea (self):
        return self.area()*2 + 2*3.141592*self.raio*self.alt
# teste da classe Cylinder


# ERRO 1 9 100
# ERRO 1 10 100
# ERRO 1 11 100
# ERRO 1 12 100

# ERRO 1 13 75

ca = Cylinder()
cb = Cylinder(1,2,3,4)
cb.printcy()
print str(cb.carea())
