import math
import random


class Vector:

    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return "({}, {}, {})".format(self.x, self.y, self.z)

    def __add__(self, other):
        assert isinstance(other, Vector)
        return self.__class__(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        #         assert isinstance(other, Vector)
        return self.__class__(self.x - other.x, self.y - other.y, self.z - other.z)

    def __truediv__(self, number):
        assert not isinstance(number, Vector)
        return self.__class__(self.x / number, self.y / number, self.z / number)

    def __mul__(self, number):
        assert not isinstance(number, Vector)
        return self.__class__(self.x * number, self.y * number, self.z * number)

    def __rmul__(self, number):
        return self.__mul__(number)

    def scalar_product(self, other):
        assert isinstance(other, Vector)
        return self.x * other.x + self.y * other.y + self.z * other.z

    def magnitude(self):
        return math.sqrt(self.scalar_product(self))

    def normalize(self):
        return self / self.magnitude()

    @staticmethod
    def random():

        # TODO gaussian random Vector generator normalised that return vector on the half-shpere of deflection

        return Vector(random.gauss(0, 1),
                      random.gauss(0, 1), random.gauss(0, 1))




