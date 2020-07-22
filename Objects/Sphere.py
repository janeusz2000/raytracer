from Objects.Object import Object
from Core.Vector import Vector
from Core.Color import Color
import math


class Sphere(Object):

    def __init__(self, origin=Vector(0, 0, 0), radius=0.5,
                 material=Color(1.0, 0.0, 0.0)):
        self.origin = origin
        self.radius = radius
        self.radius_square = radius ** 2
        self.material = material

    def hit_object(self, ray):

        """Returns Vector() with coordinate where ray hit the object"""

        # TODO make model that creates 4-5 additional rays that origin is
        #  at hit point and direction is based on statistic model that represent how sound is reflecting

        oc = ray.origin - self.origin
        a = 1
        b = 2.0 * oc.scalar_product(ray.direction)
        c = oc.scalar_product(oc) - self.radius_square
        discriminant = b * b - 4 * a * c
        if discriminant < 0:
            return None
        else:
            temp = math.sqrt(discriminant)
            t1 = (-b - temp) / (2.0 * a)
            t2 = (-b + temp) / (2.0 * a)
            if t1 < 0 and t2 < 0:
                return None
            elif t1 < 0:
                return None
            else:
                return ray.at(min(t1, t2))

    def get_material(self):
        return self.material

    def normal(self, surface_point):
        """Return normal of the surface where object was hit"""

        assert isinstance(surface_point, Vector)
        return (surface_point - self.origin).normalize()

    def random_in_unit(self):

        # TODO Delete this function when Vector random is done

        while True:
            random_vec3 = self.origin.random()
            if random_vec3.magnitude() >= 0.001:
                return random_vec3.normalize()


