import math
from multimethod import multimethod

class Vector3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vector3D(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Vector3D(self.x * other, self.y * other, self.z * other)
        raise TypeError("Solo se permite multiplicación escalar")

    def __rmul__(self, other):
        return self.__mul__(other)

    def __abs__(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def __invert__(self):
        m = abs(self)
        if m == 0:
            raise ValueError("Vector nulo")
        return Vector3D(self.x / m, self.y / m, self.z / m)

    def __matmul__(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    def __xor__(self, other):
        return Vector3D(
            self.y * other.z - self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.x * other.y - self.y * other.x
        )

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"

    @multimethod
    def producto(a: 'Vector3D', b: 'Vector3D'):
        return a @ b

    @multimethod
    def producto(a: 'Vector3D', escalar: float):
        return a * escalar


a = Vector3D(2, -1, 3)
b = Vector3D(1, 4, -2)
r = 3

print("Suma: ", a + b)        
print("Multipliacaion: ", r * a)        
print("Longitud: ", abs(a))         
print("Normal: ", ~a)              
print("Producto escalar: ", a @ b)        
print("Productovectorial: ", a ^ b)        
