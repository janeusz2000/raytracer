from Objects.Object import Object
from Core.Vector import Vector
from Core.Color import Color


class TriangleFace(Object):

    def __init__(self, material=Color(1, 0, 0), point_1=Vector(0, 0, 0),
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
            print ("wuut!")
            return None

        t = (-(ray.origin - self.point_3)).scalar_product(self._normal) / (ray.direction.scalar_product(self._normal))
        if t < 0.01:
            return None
        surface_point = ray.at(t)


        debug = (t < 2.01)
        if self.does_hit(surface_point, debug=debug):
            return surface_point
        else:
            return None

    def does_hit(self, point, debug=False):

        vector_a = self.point_1 - point
        vector_b = self.point_2 - point
        vector_c = self.point_3 - point

        div = 2.0
        alpha = vector_b.cross_product(vector_c).magnitude() / div  # 2 and 3
        beta = vector_c.cross_product(vector_a).magnitude() / div   # 3 and 1
        gamma = vector_a.cross_product(vector_b).magnitude() / div  # 1 and 2

        if alpha + beta + gamma > self.area:
            return False
        return True


    def normal(self, point):
        return self._normal



