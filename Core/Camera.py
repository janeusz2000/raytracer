from Core.Vector import Vector


class Camera:
    """
    X = left/right
    Y when increaead we go down, when decrease we go up
    Z when increased we go forward, when decreased we go back
    """
    def __init__(self, aspect_ratio=16.0 / 9.0, focal_length=1.0, origin=Vector(0, 0, -1)):

        self.aspect_ratio = aspect_ratio
        self.focal_length = focal_length
        self.origin = origin
        self.horizontal = Vector(aspect_ratio, 0, 0)
        self.vertical = Vector(0, 1.0, 0)
        self.upper_left_corner = origin - self.horizontal / 2.0 - self.vertical / 2.0 + Vector(0, 0, self.focal_length)
