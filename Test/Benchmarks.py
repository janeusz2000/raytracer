from Objects.TriangleFace import TriangleFace
from Core.Color import Color
from Core.Vector import Vector
import timeit


def main():
    x = timeit.timeit(stmt="triangle.does_hit(Vector(1.25, 1.25, 1))",
                      setup="triangle = TriangleFace(Color(1, 0, 0), Vector(1, 2, 1), Vector(1, 1, 1), Vector(2, 1, 1))",
                      globals=globals(), number=1000000)
    print(x/1000.0)
    x = timeit.timeit(stmt="triangle.does_hit2(Vector(1.25, 1.25, 1))",
                      setup="triangle = TriangleFace(Color(1, 0, 0), Vector(1, 2, 1), Vector(1, 1, 1), Vector(2, 1, 1))",
                      globals=globals(), number=1000000)
    print(x / 1000.0)


if __name__ == "__main__":
    main()

