#Lista 5 de Programcao orientada a objeto
#
#Autores: Lucas Antiqueira           NUSP: 3457180
#         Marco Aurelio Roncatti     NUSP: 3455855



class Ponto:
    def __init__(self, x=0,y=0):
        try:
            self.x = float(x)            
            self.y = float(y)
        except:
            print "Erro durante inicializacao de 'Ponto'"
    def set_ponto(self,x,y):
        try:
            self.x = float(x)
            self.y = float(y)
        except:
            print "Erro durante alteracao de 'Ponto'"
    def get_x(self):
        return self.x
    def get_y(self):
        return self.y
    def __add__(self,other):
        try:
            return Ponto(self.x + other.x, self.y + other.y)
        except:
            print "Erro durante a soma de pontos"
    def __sub__(self,other):
        try:
            return Ponto(self.x - other.x, self.y - other.y)
        except:
            print "Erro durante a subtracao de circulos"
            
    def __mul__(self,other):
        try:
            return self.x*other.x + self.y * other.y
        except:
            print "Erro durante o produto escalar de pontos"
    def __rmul__(self,other):
        try:
            float(other)
            return Ponto(other*self.x,other*self.y)
        except:
            print "Erro durante a multiplicacao de um ponto por um escalar"
    def __div__(self,other):
        try:
            float(other)
            if(other == 0):
                print "Erro durante a divizao de pontos: divizao por zero"
            else:
                return Ponto(self.x/other,self.y/other)
        except:
            print "Erro durante a divizao de pontos"


class Circle(Ponto):
    def __init__(self,raio=1,x=0,y=0):
        Ponto.__init__(self,x,y)
        try:
            self.raio = float(raio)
        except:
            print "Erro durante a inicializacao de 'Circle'"
    def printc (self):
        print self.get_x()
        print self.get_y()
        print self.raio
    def area(self):
        return 3.141592*self.raio*self.raio
    def set_circ(self,raio=1,x=0,y=0):
        try:
            self.x = float(x)
            self.y = float(y)
            self.raio = float(raio)
        except:
            print "Erro durante alteracao de 'Circle'"

    def __add__(self,other):
        try:    
            aux_x = self.x + other.x
            aux_y = self.y + other.y
            aux_r = self.raio + other.raio
            return Circle(aux_r,aux_x,aux_y)
        except:
            print "Erro durante a soma de circulos"
    def __sub__(self,other):
        try:
            aux_x = self.x - other.x
            aux_y = self.y - other.y
            aux_r = self.raio - other.raio
            return Circle(aux_r,aux_x,aux_y)
        except:
            print "Erro durante a subtracao de circulos"
    def __mul__(self,other):
        try:
            return self.x*other.x + self.y*other.y + self.raio*other.raio
        except:
            print "Erro durante o produto escalar de circulos"

    def __rmul__(self,other):
        try:
            float(other)
            return Circle(self.raio*other,self.x*other,self.y*other)
        except:
            print "Erro durante a multiplicacao de um circulo por um escalar"
    def __div__(self,other):
        try:
            float(other)
            if(other == 0):
                print "Erro durante a divizao de circulos: divizao por zero"
            else:
                return Circle(self.raio/other,self.x/other,self.y/other)
        except:
            print "Erro durante a divizao de circulos"
                  
class Cylinder(Circle):
    def __init__(self,alt=1,raio=1,x=0,y=0):
        Circle.__init__(self,raio,x,y)
        try:
            self.alt = alt
        except:
            print "Erro durante a inicializacao de 'Cylinder'"            
    def printcy(self):
        print "x:", self.get_x()
        print "y:", self.get_y()
        print "raio:", self.raio
        print "altura:", self.alt
    def volume(self):
        return self.area()*self.alt
    def area(self):
        return self.area()*2 + 2*3.141592*self.raio.self.alt
    def __add__(self,other):
        try:
            aux_raio = self.raio + other.raio
            aux_x = self.x + other.x
            aux_y = self.y + other.y
            aux_alt = self.alt + other.alt
            return Cylinder(aux_alt,aux_raio,aux_x,aux_y)
        except:
            print "Erro durante a soma de cilindros"
    def __sub__ (self,other):
        try:
            aux_raio = self.raio - other.raio
            aux_x = self.x - other.x
            aux_y = self.y - other.y
            aux_alt = self.alt - other.alt
            return Cylinder(aux_alt,aux_raio,aux_x,aux_y)
        except:
            print "Erro durante a subtracao de cilindros"
        
    def __rmul__(self,other):
        try:
            float(other)
            return Cylinder(self.alt*other, self.raio*other,self.x*other,self.y*other)
        except:
            print "Erro durante a multiplicacao de um cilindro por um escalar"
    def __div__(self,other):
        try:
            float(other)
            if(other == 0):
                print "Erro durante a divizao de cilindros: divizao por zero"
            else:
                return Cylinder(self.alt/other, self.raio/other,self.x/other,self.y/other)
        except:
            print "Erro durante a divizao de cilindros"


# ERRO 1 5 15
# ERRO 1 6 15
# ERRO 1 7 15
# ERRO 1 8 15
# ERRO 1 9 15
# ERRO 1 10 15
# ERRO 1 11 15
# ERRO 1 12 15

a = Cylinder()
a.printcy()
a += 1
