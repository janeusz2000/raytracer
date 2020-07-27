import abc
from Core.Color import Color
from Core.Vector import Vector
from Core import Materials
from Core.Ray import RayHitData
import math


class Object(abc.ABC):

    @abc.abstractmethod
    def hit_object(self, ray):
        pass

    def normal(self, surface_point):
        pass

    # TODO make line hat works with .obj format


class Line:
    pass

    # TODO make Point class that is compatible with point object in .obj format


class Point(Vector):
    pass


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
            t = min(t1, t2)
            surface_point = ray.at(t)
            return RayHitData(t, surface_point, self.normal(surface_point), self.material)

    def normal(self, surface_point):
        """Return normal of the surface where object was hit"""
        assert isinstance(surface_point, Vector)
        return (surface_point - self.origin).normalize()


class TriangleFace(Object):

    def __init__(self, material=Materials.MaterialDiffuse(Color(0, 0, 0)), point_1=Vector(0, 0, 0),
                 point_2=Vector(0, 0, 0), point_3=Vector(0, 0, 0)):

        self.point_1 = point_1
        self.point_2 = point_2
        self.point_3 = point_3

        self._normal = (self.point_3 - self.point_2).cross_product(self.point_1 - self.point_2)
        self.material = material
        self.area = self._normal.magnitude() / 2.0
        self._normal = self._normal.normalize()
        # TODO create constructor that has all required properties to calculate object: lines, normal, material

    def hit_object(self, ray):

        if abs(ray.direction.scalar_product(self._normal)) <= 0.0001:
            return None

        t = (-(ray.origin - self.point_3)).scalar_product(self._normal) / (ray.direction.scalar_product(self._normal))
        if t < 0.01:
            return None

        debug = (t < 2.01)
        ray_hit_data = RayHitData(t, ray.at(t), self._normal, self.material)
        if self.does_hit(ray_hit_data.point, debug=debug):
            return ray_hit_data
        else:
            return None

    def does_hit(self, point, debug=False):

        vector_a = self.point_1 - point
        vector_b = self.point_2 - point
        vector_c = self.point_3 - point

        div = 2.0
        alpha = vector_b.cross_product(vector_c).magnitude() / div  # 2 and 3
        beta = vector_c.cross_product(vector_a).magnitude() / div  # 3 and 1
        gamma = vector_a.cross_product(vector_b).magnitude() / div  # 1 and 2

        if alpha + beta + gamma > self.area + 0.01:
            return False
        return True

    def normal(self, point):
        return self._normal


class Surface(Object):

    def __init__(self, material=Materials.MaterialDiffuse(Color(0, 0, 0)), point_1=Vector(1, 1, 0),
                 point_2=Vector(1, 0, 0), point_3=Vector(0, 1, 0)):
        self.point_1 = point_1
        self.point_2 = point_2
        self.point_3 = point_3
        self.material = material

        vector_a = point_2 - point_1
        vector_b = point_3 - point_1
        self._normal = (vector_a.cross_product(vector_b)).normalize()

    def normal(self, surface_point):
        return self._normal

    def hit_object(self, ray):

        if abs(ray.direction.scalar_product(self._normal)) <= 0.0001:
            return None

        t = (-(ray.origin - self.point_3)).scalar_product(self._normal) / (ray.direction.scalar_product(self._normal))

        if t < 0.01:
            return None

        return RayHitData(t,  ray.at(t), self._normal, self.material)



