#*****************************************************#
#                                                     #
#  Exercicio 5 - alterar o programa dado              #
#                                                     #
#  Alunos:                                            #
#                                                     # 
#      Marco Aurelio Rescia Alher 3560481             #
#      Santiago de Moura Luz      3560495             # 
#                                                     #
#*****************************************************#

import math

class ponto:
    def __init__(self, x=0,y=0):
        try:
            self.x = float(x)            
            self.y = float(y)
        except:
            print("Coordenadas Incorretas")

    def set_ponto(self,x,y):
        try:
            self.x = float(x)
            self.y = float(y)
        except:
            print("Coordenadas Incorretas")

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def __add__(self,other):
        if (other.__class__ == ponto):
            return ponto(self.x + other.x, self.y + other.y)
        else:
            print("A soma deve estar entre dois pontos validos")

    def __mul__(self,other):
        if (other.__class__ == ponto):
            return self.x * other.x + self.y * other.y
        else:
            print("A multiplicacao escalar deve ser entre dois ponto validos")

    def __rmul__(self,other):
        try:
            float(other)
            return ponto(other * self.x, other * self.y)
        except:
            print("Multiplicacao por escalar incorreta")

    def __div__(self,other):
        try:
            float(other)
            if(other == 0):
                print("Divisao por zero")
            else:
                return ponto(self.x / other, self.y / other)
        except:
            print("Divisor escalar incorreto")
    def __str__(self):
        return "(%.3f,%.3f)"%(self.x,self.y)

#******************************************************************************

class circle(ponto):
    def __init__(self, raio=1, x=0, y=0):
        ponto.__init__(self, x, y)
        try:
            self.raio = float(raio)
        except:
            print("Valor do raio incorreto")

    def printc (self):
        print self.get_x()
        print self.get_y()
        print self.raio

    def area(self):
        return 3.141592 * self.raio * self.raio

    def set_circ(self,p):
        try:
            self.x = p.x
            self.y = p.y
        except:
            print("ponto dado incorreto")

    def __str__(self):
        return "(x-%.3f)**2 + (y - %.3f)**2 = %.3f**2"%(self.x,self.y,self.raio)

    def __add__(self,other): 
        try:    
            auxiliar_x = self.x + other.x
            auxiliar_y = self.y + other.y
            auxiliar_r = math.sqrt(self.raio**2 + other.raio**2)
            return circle(auxiliar_r, auxiliar_x, auxiliar_y)
        except:
            print("Deve ser dado um valor de cilindro valido")

    def __sub__(self,other):
        try:
            auxiliar_x = self.x - other.x
            auxiliar_y = self.y - other.y
            auxiliar_r = math.sqrt(self.raio**2 - other.raio**2)
            return circle(auxiliar_r, auxiliar_x, auxiliar_y)
        except ValueError:
            print("Valor de retorno eh negativo")
        except AttributeError:
            print("Deve ser dado um circulo valido")

    def __mul__(self,other):
        if(other.__class__ == circle):
            return self.x * other.x + self.y * other.y + self.raio * other.raio
        else:
            print("Deve ser dada um circulo valido")

    def __rmul__(self,other):
        try:
            float(other)
            return circle(self.raio * other,self.x * other,self.y * other)
        except:
            print("Multiplicacao por escalar incorreto")

    def __div__(self,other):
        try:
            float(other)
            if (other == 0):
                print("Divizao por zero")
            else:
                return circle(self.raio/other,self.x/other,self.y/other)
        except:
            print("Divisor escalar incorreto")

#***********************************************************************************
                  
class cylinder(circle):
    def __init__(self,alt=1,raio=1,x=0,y=0):
        circle.__init__(raio,x,y)
        try:
            self.alt = alt
        except:
            print("Valor da altura invalido")            

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
            a = circle(self.raio,self.x,self.y)
            b = circle(other.raio,other.x,other.y)
            auxiliar_alt = math.pow(self.alt**3 + other.alt**3, 1/3)
            return cylinder(auxiliar_alt,(a+b).raio,(a+b).x,(a+b).y)
        except:
            print("Deve ser dado um cilindro valido")

    def __sub__ (self,other):
        try:
            a = circle(self.raio,self.x,self.y)
            b = circle(other.raio,other.x,other.y)
            auxiliar_alt = math.pow(self.alt**3 - other.alt**3, 1/3)
            return cylinder(auxiliar_alt,(a-b).raio,(a-b).x,(a-b).y)
        except ValueError:
            print("Valor de retorno negativo")
        except AttributeError:
            print("Deve ser dado um cilindro valido")

    def __rmul__(self,other):
        try:
            float(other)
            return cylinder(self.alt * other, self.raio * other, self.x * other, self.y * other)
        except:
            print("Valor do escalar eh invalido para a multiplicacao")

    def __div__(self,other):
        try:
            float(other)
            if(other == 0):
                print("Divizao por zero")
            else:
                return cylinder(self.alt / other, self.raio / other,self.x / other,self.y / other)
        except:
            print("Valor do escalar eh invalido para a divisao")

a = cylinder()
b = cylinder()
c = a + b
c.printcy()
c += 3


# ERRO 1 5 10
# ERRO 1 6 10
# ERRO 1 7 10
# ERRO 1 8 10
# ERRO 1 9 10
# ERRO 1 10 10
# ERRO 1 11 10
# ERRO 1 12 10

# ERRO 1 14 50
