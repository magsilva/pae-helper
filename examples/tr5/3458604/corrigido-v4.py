############# Ponto #################   
   
class Ponto:   
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
        try:
            return Ponto(self.x + other.x, self.y + self.y)   
        except TypeError:
            print('tipos incompativeis para essa operacao')
    def __mul__(self, other):   
        try:
            return self.x * other.x + self.y * self.y   
        except TypeError:
            print('tipos incompativeis para essa operacao')
          
   
    def __rmul__(self, escalar):   
        try:
            return Ponto(escalar * self.x, escalar * self.y)   
        except TypeError:
            print('tipos incompativeis para essa operacao')
 
    ##### Modificacoes ##### 
 
    def __sub__(self, other):  
        try:
            return Ponto(self.x - other.x, self.y - other.y)  
        except TypeError:
            print('tipos incompativeis para essa operacao')
  
    def __rdiv__(self, escalar):  
        try:
            return Ponto(self.x / escalar, self.y / escalar)
        except TypeError:
            print('tipos incompativeis para essa operacao')
        except ZeroDivisionError:
            print('tentativa de divisao por zero')


# ERRO 1 1 75
# ERRO 1 2 75
# ERRO 1 3 50
# ERRO 1 4 75

a = Ponto()

############# Circle #################   
   
class Circle(Ponto):   
    def __init__(self, raio = 1, x = 0, y = 0):   
        Ponto.__init__(self, x, y)   
        self.raio = raio   
   
    def printc(self):   
        print self.raio   
        print self.get_x()   
        print self.get_y()   
   
    def area(self):   
        return 3.141592 * self.raio * self.raio   
   
    def set_circ(self, p):   
        self.x = p.x   
        self.y = p.y   
  
    ##### Modificacoes ##### 
 
    ### Soma os raios e mantem o centro do primeiro 
    def __add__(self, other):  
        try:
            return Circle(self.raio + other.raio, self.x, self.y)  
        except TypeError:
            print('tipos incompativeis para essa operacao')
  
    ### Subtrai os raios e mantem o centro do primeiro 
    def __sub__(self, other):  
        try:
            return Circle(self.raio - other.raio, self.x, self.y)  
        except TypeError:
            print('tipos incompativeis para essa operacao')
  
    ### Multiplica o raio do circulo por um escalar
    def __rmul__(self, escalar):  
        try:
            return Circle(self.raio * escalar, self.x, self.y)
        except TypeError:
            print('tipos incompativeis para essa operacao')

    ### Divide o raio do circulo por um escalar
    def __rdiv__(self, escalar):
        try:
            return Circle(self.raio / escalar, self.x, self.y)
        except TypeError:
            print('tipos incompativeis para essa operacao')
        except ZeroDivisionError:
            print('tentativa de divisao por zero')
    
# ERRO 1 1 75
# ERRO 1 2 75
# ERRO 1 3 50
# ERRO 1 4 75

############# Cylinder #################   
   
class Cylinder(Circle):   
    def __init__(self, alt = 1, raio = 1, x = 0, y = 0):   
        Circle.__init__(self, raio, x, y)   
        self.alt = alt   
   
    def printcy(self):   
        print self.alt   
        print self.raio   
        print self.get_x()   
        print self.get_y()   
   
    def volume(self):   
        return self.area() * self.alt   
   
    def __area__(self):   
        return self.area() * 2 + 2 * 3.141592 * self.raio * self.alt 
 
    ##### Modificacoes ##### 
 
    ### Soma os raios e as alturas e mantem o centro do primeiro
    def __add__(self, other): 
        try:
            return Cylinder(self.alt + other.alt, self.raio + other.raio, self.x, self.y) 
        except TypeError:
            print('tipos incompativeis para essa operacao')
 
    ### Subtrai os raios e as alturas e mantem o centro do primeiro
    def __sub__(self, other): 
        try:
            return Cylinder(self.alt - other.alt, self.raio - other.raio, self.x, self.y)
        except TypeError:
            print('tipos incompativeis para essa operacao')

    ### Multiplica a altura e o raio por um escalar
    def __rmul__(self, escalar):
        try:
            return Cylinder(self.alt * escalar, self.raio * escalar, self.x, self.y)
        except TypeError:
            print('tipos incompativeis para essa operacao')

    ### Divide a altura e o raio por um escalar
    def __rdiv__(self, escalar):
        try:
            return Cylinder(self.alt / escalar, self.raio / escalar, self.x, self.y)
        except TypeError:
            print('tipos incompativeis para essa operacao')
        except ZeroDivisionError:
            print('tentativa de divisao por zero')

# ERRO 1 1 75
# ERRO 1 2 75
# ERRO 1 3 50
# ERRO 1 4 75

a = Cylinder()
a.printcy()
a += 3

# ERRO 1 14 15
