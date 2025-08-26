from math import sqrt

class EcuaionCuadratica():
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    def getDiscriminante(self):
        discriminante = sqrt((self.b**2) - (4 * self.a * self.c))
        return discriminante
    
    def getRaiz1(self, d):
        self.d = d
        r1 = (-self.b + self.d) / (2 * self.a)
        return r1
    
    def getRaiz2(self, d):
        self.d = d
        r2 = (-self.b - self.d) / (2 * self.a)
        return r2

print ("Ingrese los valores de a b c")
a, b, c = map(float,input().strip().split(" "))
ecuacioncuadratica = EcuaionCuadratica(a, b, c)
d = ecuacioncuadratica.getDiscriminante()
if d > 0:
    raiz1 = ecuacioncuadratica.getRaiz1(d)
    raiz2 = ecuacioncuadratica.getRaiz2(d)
    print (f"La ecuacion tiene dos raıces {raiz1:.0f} y {raiz2:.0f}")
elif d == 0:
    print (f"La ecuacion tiene una raız {ecuacioncuadratica.getRaiz2(d):0f}")
else:
    print ("La ecuacion no tiene raıces reales")
