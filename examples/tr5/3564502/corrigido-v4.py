################################################################################
#                                                                              #
# Aula Pratica de P.O.O. - 29/04/2003 - Heranca para Ponto, Circulo e Cilindro #
#                                                                              #
# Alunos:                                                                      #
#           Jose Arnaldo Mascagni de Holanda   nroUSP: 3564502                 #
#           Marcus Vinicius Secato             nroUSP: 3285140                 #
#                                                                              #
################################################################################

class Ponto:

    def __init__(self,x=0,y=0):
        try:
            self.x = x
            self.y = y
        except:
            print " Valores nao validos. "

    def set_ponto(self,x,y):
        try:
            self.x = x
            self.y = y
        except:
            print " Valores nao validos. "

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def __add__(self,other):

        if (other.__class__ == Ponto):
            return Ponto(self.x + other.x, self.y + other.y)
        else:
            print " A soma deve ser feita entre dois Pontos validos."

    def __mul__(self,other):

        if (other.__class__ == Ponto):
            return self.x*other.x + self.y*other.y
        else:
            print " Multiplicacao somente entre 2 ptos validos."

    def __rmul__(self, other):

        try:
            float(other)
            return Ponto(other*self.x, other*self.y)
        except:
            print " O escalar deve ser um nro real."

    def __sub__(self,other):
        return Ponto(self.x - other.x, self.y - other.y)

    def __rsub__(self,other):
        return Ponto(self.x - other, self.y - other)

    def __div__(self, other):

            if (other.__class__ == Ponto):
                return self.x/other.x - self.y/other.y  
            else:
                print " A divisao deve ser feita entre dois Pontos validos."

    def __rdiv__(self, other):

        try:
            float(other)
            return Ponto(self.x/other, self.y/other)
        except:
            print " O escalar deve ser um nro real."

    
class Circle(Ponto):
    def __init__(self, raio = 1, x = 0, y = 0):
        Ponto.__init__(self,x,y)

        try:
            self.raio = float(raio)
        except:
            print " Valor invalido para raio."
            
    def printc(self):

        print self.get_x()
        print self.get_y()
        print self.raio

    def area(self):
        return 3.141592*self.raio*self.raio

    def set_circle(self,p):
        self.x= p.x
        self.y= p.y

    def __add__(self,other): # adiciona circulos concentricos
        if (other.__class__ == Circle):
            if (self.x == other.x) and (self.y == other.y):
                return Circle(self.raio+other.raio, self.x, self.y)
            else:
                print " Os circulos nao sao concentricos. "
    
        else:
            print " A soma deve ser entre circulos validos."


    def __mul__(self,other):
        if (other.__class__ == Circle):
            if (self.x == other.x) and (self.y == other.y):
                return Circle(self.raio*other.raio, self.x, self.y)
            else:
                print " Os circulos nao sao concentricos. "
    
        else:
            print " A multiplicacao deve ser entre circulos validos."

    def __rmul__(self, other):
        try:
            float(other)
            return Circle(self.raio,other*self.x, other*self.y)
        except:
            print " O escalar deve ser um numero real."

    def __sub__(self,other):
        if (other.__class__ == Circle):
            if (self.x == other.x) and (self.y == other.y):
                return Circle(abs(self.raio-other.raio), self.x, self.y)
            else:
                print " Os circulos nao sao concentricos. "
    
        else:
            print " A subtracao deve ser entre circulos validos."


    def __rsub__(self,other):
        try:
            float(other)
            return Circle(self.raio,self.x - other,self.y - other)
        except:
            print " O escalar deve ser um numero real."

    def __div__(self, other):
        if (other.__class__ == Circle):
            if (self.x == other.x) and (self.y == other.y):
                return Circle(self.raio/other.raio, self.x, self.y)
            else:
                print " Os circulos nao sao concentricos. "
    
        else:
            print " A divisao deve ser entre circulos validos."

    def __rdiv__(self, other):
        try:
            float(other)
            return Circle(self.raio/other,self.x,self.y)
        except:
            print " O escalar deve ser um numero real."

class Cylinder(Circle):
    def __init__(self,alt=1,raio=1,x=0,y=0):
        Circle.__init__(self,raio,x,y)
        try:        
            self.alt= alt
        except:
            print " Valor invalido para a altura."

    def printcy(self):
        print self.get_x()
        print self.get_y()
        print self.raio
        print self.alt

    def volume(self):
        return self.area()*self.alt

    def area(self):
        return self.area()*2 + 2*3.141592*self.raio*self.alt

    def __add__(self,other):
        if (self.x == other.x) or (self.y == other.y):
            return Cylinder(self.alt+other.alt,self.raio+other.raio,self.x,self.y)
        else:
            print " Os cilindros devem estar no mesmo eixo."
            
    def __sub__(self,other):
        if (self.x == other.x) or (self.y == other.y):
            return Cylinder(abs(self.alt-other.alt),abs(self.raio+other.raio),self.x,self.y)
        else:
            print " Os cilindros devem estar no mesmo eixo."

    def __rdiv__(self,other):
        try:
            float(other)
            return Cylinder(self.alt/other,self.raio/other,self.x,self,y)
        except:
            print " O escalar deve ser um nro real."

    def __rmul__(self,other):
        try:
            float(other)
            return Cylinder(self.alt*other,self.raio*other,self.x,self.y)
        except:
            print "O escalar deve ser um nro real."

a = Cylinder()
b = Cylinder()
c = a / b


# ERRO 1 5 10
# ERRO 1 6 10
# ERRO 1 7 10
# ERRO 1 8 10
# ERRO 1 9 10
# ERRO 1 10 10
# ERRO 1 11 10
# ERRO 1 12 10
# ERRO 1 13 50
