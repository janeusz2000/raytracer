import math
import random


class Vector:

    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return "Vector({}, {}, {})".format(self.x, self.y, self.z)

    def __add__(self, other):
        return self.__class__(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return self.__class__(self.x - other.x, self.y - other.y, self.z - other.z)

    def __truediv__(self, number):
        return self.__class__(self.x / number, self.y / number, self.z / number)

    def __mul__(self, number):
        return self.__class__(self.x * number, self.y * number, self.z * number)

    def __rmul__(self, number):
        return self.__mul__(number)

    def __eq__(self, other):
        return self.is_close(self.x, other.x) and self.is_close(self.y, other.y) and self.is_close(self.z, other.z)

    def __neg__(self):
        return self*(-1)

    def scalar_product(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    def cross_product(self, other):
        return self.__class__(self.y * other.z - self.z * other.y,
                              self.z * other.x - self.x * other.z, self.x * other.y - self.y * other.x)

    def magnitude(self):
        return math.sqrt(self.magnitude2())

    def magnitude2(self):
        return self.scalar_product(self)

    def normalize(self):
        return self / self.magnitude()

    @staticmethod
    def random():
        while True:
            random_vec3 = Vector(random.gauss(0, 1), random.gauss(0, 1), random.gauss(0, 1)).normalize()
            if random_vec3.magnitude() >= 0.001:
                return random_vec3

    @staticmethod
    def is_close(a, b, rel_tol=1e-09, abs_tol=0.0):
        return abs(a - b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol)




