class Ray:

    def __init__(self, origin, direction):
        self.origin = origin
        self.direction = direction.normalize()

    def at(self, t):
        return self.origin + t * self.direction

    # TODO energy value
    # TODO phase Value


class RayHitData:

    def __init__(self, t, point, normal, material):
        self.t = t
        self.point = point
        self.normal = normal
        self.material = material
