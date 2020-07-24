import unittest
from Core.Vector import Vector
from Objects.Sphere import Sphere
from Core.Ray import Ray
from Core.Color import Color
from Objects.TriangleFace import TriangleFace
import random
import math


class TestMethods(unittest.TestCase):

    def test_scalar(self):
        a = Vector(1, 0, 0)
        b = Vector(0, 1, 1)
        c = Vector(123.123, 543.234, 123.345)
        d = Vector(234.123, 123.123, 5234.123)
        self.assertEqual(a.scalar_product(b), 0)
        self.assertEqual(a.cross_product(b), Vector(0, -1, 1))
        self.assertEqual(c * 3.15, Vector(387.83745, 1711.1871, 388.53675))
        self.assertEqual(Vector(math.sqrt(2), 0, 0) * math.sqrt(2), Vector(2, 0, 0))

    def test_Surface_Area(self):
        triangle = TriangleFace(Color(1, 0, 0), Vector(1, 2, 1), Vector(1, 1, 1), Vector(2, 1, 1))

        hits = 0
        missed = 0
        for a in range(100000):
            random_point = Vector(random.uniform(0, 3), random.uniform(0, 3), 1)
            if triangle.does_hit(random_point):
                hits += 1
            else:
                missed += 1
        print("hits: {}, missed: {}".format(hits, missed))
        ratio = float(hits) / (hits + missed)
        area_ratio = 0.5/9.0
        self.assertAlmostEqual(area_ratio, ratio, 3)


if __name__ == "__main__":
    unittest.main()


