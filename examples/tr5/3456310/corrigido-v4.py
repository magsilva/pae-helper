#Chen Xu Sheng                Nusp: 3456310
#Hugo Degiovanni Junior       Nusp: 3530230


class Ponto:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
    def set_ponto(self,x,y):
        if ((type(x)!=int)and(type(x)!=real))or((type(y)!=int)and(type(y)!=real)):
            print "Os valores de x e y devem ser inteiros ou reais"
            print "Entre com os valores do ponto novamente"
        else:
            self.x=x
            self.y=y
    def get_x(self):
        return self.x
    def get_y(self):
        return self.y
    def __add__(self,other):
        return Ponto(self.x+other.x,self.x+other.y)         
    def __sub__(self,other):
        return Ponto(self.x-other.y,self.x-other.y)
    def __mul__(self,other):
        return self.x*other.x+self.y*other.y
    def __rmul__(self,valor):
        return Ponto(valor*self.x,valor*self.y)
    def __div__(self,other):
        if (other==0):
            print "o valor do divideno é igual a 'zero'."
            print "Por favor, entre com outro valor" 
        else:
            return Ponto(self.x/other,self.y/other)
    def __str__(self):
        x= "Ponto(" + str(self.x) + "," + str(self.y)+ ")"
        return x

# ERRO 1 1 75
# ERRO 1 2 75
# ERRO 1 3 50
# ERRO 1 4 75


class Circle(Ponto):        
    def __init__(self,raio=1,x=0,y=0):
        if(type(raio)!=int)and(type(raio)!=float):
            print "O valor do raio não é um numero"
            print "Por favor, entre com um valor inteiro ou real"
        else:
            Ponto.__init__(self,x,y)
            self.raio=raio
    def printc(self):
        print self.get_x()
        print self.get_y()
        print self.raio
    def area(self):
        return 3.141592*self.raio*self.raio
    def set_circ(self,p):
        self.x=p.x
        self.y=p.y
    def __add__(self,other):
        import math
        novaarea=self.area()+other.area()
        aux=novaarea/3.141592
        print "O Novo ciculo tem centro: x=%f , y=%f e raio=%f"%(self.x,self.y,math.sqrt(aux))
    def __sub__(self,other):
        import math
        if(self.area()>other.area()):
            novaarea=self.area()-other.area()
        else:
            novaarea=other.area()-self.area()
        aux=novaarea/3.141592
        print "O Novo ciculo tem centro: x=%f , y=%f e raio=%f"%(self.x,self.y,math.sqrt(aux))
    def __rmul__(self,valor):
        self.raio=self.raio*valor
        return self.raio
    def __div__(self,valor):
        if valor==0:
            print "O valor do dividendo é 'zero'.Entre com outro valor"
        else:
            self.raio=self.raio/valor
        return self.raio
  
# ERRO 1 5 75
# ERRO 1 6 75
# ERRO 1 7 50
# ERRO 1 8 75

        
class Cylinder(Circle):
    def __init__(self,alt=1,raio=1,x=0,y=0):
        if ((type(alt)!= int)and(type(alt)!=real))or((type(raio)!=int)and(type(raio)!=real)):
            print "O valor do raio ou da altura não é um numero"
            print "Entre com um valor real ou inteiro para raio e altura"
        else:
            Circle.__init__(self,raio,x,y,)
            self.alt=alt
    def printc(self):
        print self.get_x()
        print self.get_y()
        print self.raio
        print self.alt
    def area(self):
        return ((2*3.141592*self.raio*self.alt) + (2*3.141592*self.raio*self.raio))
    def volume(self):
        return self.alt*(3.141592*self.raio*self.raio)
    def __add__(self,other):
        novoraio=self.raio+other.raio
        novaalt=self.alt+other.alt
        return "O Novo cilindro tem centro da base x=%f , y=%f , raio=%f e altura=%f"%(self.x,self.y,novoraio,novaalt)
    def __sub__(self,other):
        import math
        if (self.volume()>other.volume()):
            novovol=self.volume()-other.volume()
        else:
            novovol=other.volume()-self.volume()
        novoraio=min(self.raio,other.raio)
        novaalt=novovol/(3.141592*novoraio*novoraio)
        return "O Novo Cilindro tem centro da base x=%f ,y=%f ,volume=%f raio=%f e altura=%f"%(self.x,self.y, novovol,novoraio,novaalt)
    def __rmul__(self,valor):
        self.raio=self.raio*valor
        self.alt=self.alt*valor
        print "O Novo Cilindro tem altura=%f e raio=%f"%(self.alt,self.raio)
    def __div__(self,valor):
        if valor==0:
            print "O valor do dividendo é 'zero'.Entre com outro valor"
        else:
            self.raio=self.raio/valor
            self.alt=self.alt/valor
        return "O Novo Cilindro tem centro da base raio=%f e altura=%f"%(self.raio,self.alt)

# ERRO 1 9 75
# ERRO 1 10 75
# ERRO 1 11 50
# ERRO 1 12 75

# ERRO 1 13 100

p1=Ponto(2,2)
p2=Ponto(5,5)

c1=Circle(5,1,1)
c2=Circle(2,2,2)

d1=Cylinder(2,2,0,0)        
d2=Cylinder(4,3,1,1)        
