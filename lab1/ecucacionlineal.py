class EcuacionLineal:
    def __init__(self, a=9.0, b=4.0, c=3.0, d=-5.0, e=-6.0, f=-21.0): #construcotor
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.f = f
        
    def tieneSolucion(self):
        sol=True
        if self.a*self.d - self.b*self.c == 0:
            sol=False
        return sol
    
    def getX(self):
        x=(self.e*self.d - self.b*self.f)/(self.a*self.d - self.b*self.c)
        return x
    
    def getY(self):
        y=(self.a*self.f - self.e*self.c)/(self.a*self.d - self.b*self.c)
        return y

ecuacionlineal = EcuacionLineal()
if ecuacionlineal.tieneSolucion() == False:
    print ("La ecuacion no tiene solucion")
else:
    print (f"x = {ecuacionlineal.getX()}, y = {ecuacionlineal.getY()}")