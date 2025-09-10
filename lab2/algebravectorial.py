import math

class AlgebraVectorial:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def producto_punto(self):
        resultado = 0
        for i in range(len(self.a)):
            resultado += self.a[i] * self.b[i]
        return resultado

    def norma(self, v):
        suma = 0
        for i in v:
            suma += i ** 2
        return math.sqrt(suma)

    def son_perpendiculares(self):
        return self.producto_punto() == 0

    def son_paralelos(self):
        try:
            razones = []
            for i in range(len(self.a)):
                if self.b[i] != 0:
                    razones.append(self.a[i] / self.b[i])
            for i in range(1, len(razones)):
                if razones[i] != razones[0]:
                    return False
            return True
        except ZeroDivisionError:
            return False

    def proyeccion_de_a_sobre_b(self):
        numerador = self.producto_punto()
        denominador = 0
        for i in self.b:
            denominador += i ** 2
        escalar = numerador / denominador
        resultado = []
        for i in range(len(self.b)):
            resultado.append(escalar * self.b[i])
        return resultado

    def componente_de_a_en_b(self):
        numerador = self.producto_punto()
        magnitud_b = self.norma(self.b)
        return numerador / magnitud_b

a = [2, 3]
b = [4, 6]

alg = AlgebraVectorial(a, b)

print("Perpendiculares", alg.son_perpendiculares())
print("Paralelos", alg.son_paralelos())
print("Proyección", alg.proyeccion_de_a_sobre_b())
print("Componente", alg.componente_de_a_en_b())
