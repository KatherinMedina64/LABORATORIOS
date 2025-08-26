from math import sqrt

class Estadistica():
    def __init__(self, num):
        self.nums = num
    
    def Promedio(self):
        sumadedatos=sum(self.nums)
        promedio = sumadedatos / len(self.nums)
        return promedio
    
    def Desviacion(self):
        prom = self.Promedio()
        suma = sum((x - prom)**2 for x in self.nums)
        return sqrt(suma / (len(self.nums) - 1))

print("Ingrese 10 numeros:")
notas=list(map(float,input().strip().split(" ")))
estadistica = Estadistica(notas)
print (f"El promedio es: {estadistica.Promedio():.2f}")
print (f"La desviacion estandar es: {estadistica.Desviacion():.5f}")