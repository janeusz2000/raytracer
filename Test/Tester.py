import unittest
from Core.Vector import Vector
from Objects.Sphere import Sphere
from Core.Ray import Ray


class TestMethods(unittest.TestCase):

    def test_scalar(self):
        a = Vector(1, 0, 0)
        b = Vector(0, 1, 1)
        self.assertEqual(a.scalar_product(b), 0)

    def test_Sphere(self):
        sphere = Sphere(origin=Vector(0, 0, 0), radius=1)
        ray = Ray(Vector(0, 0, 0), Vector(1, 0, 0).normalize())
        self.assertEqual(sphere.hit_object(ray), True)

if __name__ == "__main__":
    unittest.main()