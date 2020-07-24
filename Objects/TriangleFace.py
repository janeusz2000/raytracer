from Objects.Object import Object
from Core.Vector import Vector
from Core.Color import Color


class TriangleFace(Object):

    def __init__(self, material=Color(1, 0, 0), point_1=Vector(0, 0, 0),
                 point_2=Vector(0, 0, 0), point_3=Vector(0, 0, 0)):

        self.point_1 = point_1
        self.point_2 = point_2
        self.point_3 = point_3

        self._normal = (self.point_3 - self.point_1).cross_product(self.point_2 - self.point_1)
        self.material = material
        self.area = self._normal.magnitude() / 2.0
        self.area2 = self._normal.magnitude2()
        self._normal = self._normal.normalize()
        # TODO create constructor that has all required properties to calculate object: lines, normal, material

    def hit_object(self, ray):

        if abs(ray.direction.scalar_product(self._normal)) <= 0.0001:
            return None

        t = (-(ray.origin - self.point_1)).scalar_product(self._normal) / (ray.direction.scalar_product(self._normal))
        surface_point = ray.at(t)

        if self.does_hit(surface_point):
            return surface_point
        else:
            return None

    def does_hit(self, point):

        vector_a = self.point_1 - point
        vector_b = self.point_2 - point
        vector_c = self.point_3 - point

        alpha = vector_b.cross_product(vector_c).magnitude() / 2.0
        beta = vector_c.cross_product(vector_a).magnitude() / 2.0
        gamma = vector_a.cross_product(vector_b).magnitude() / 2.0

        if alpha + beta + gamma > self.area + 0.01:
            return False
        return True

    def normal(self, point):
        return self._normal



