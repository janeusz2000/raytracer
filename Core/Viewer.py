from Core.Ray import Ray
import random
from Core import Color
from Core.Vector import Vector


class Viewer:

    def __init__(self, height, width, object_list, samples_per_pixel, camera, color_que, max_depth=50):

        self.WIDTH = width
        self.HEIGHT = height
        self.camera = camera
        self.object_list = object_list
        self.samples_per_pixel = samples_per_pixel
        self.scale = 1.0 / self.samples_per_pixel
        self.color_que = color_que
        self.max_depth = max_depth

    def render(self, x0, x1, y0, y1):

        for x in range(x0, x1):
            for y in range(y0, y1):
                current_color = Color.Color(0.0, 0.0, 0.0)
                for sample in range(0, self.samples_per_pixel):
                    v = (float(y) + (random.random() / 2 - 1)) / float(self.HEIGHT - 1)
                    u = (float(x) + (random.random() / 2 - 1)) / float(self.WIDTH - 1)
                    current_ray = Ray(self.camera.origin, self.camera.upper_left_corner +
                                      u * self.camera.horizontal + v * self.camera.vertical - self.camera.origin)
                    current_color += self.ray_color(current_ray, self.max_depth)
                self.color_update(x, y, current_color)

    def color_update(self, x, y, color):
        self.color_que.put([x, y, color * self.scale])

    def add_object(self, obj):
        self.object_list.append(obj)

    def ray_color(self, ray, depth):

        if depth <= 0:
            return Color.Color(0.0, 0.0, 0.0)

        current_index = 0

        closest_hit_data = None
        for obj in self.object_list:
            hit_data = obj.hit_object(ray)
            if (hit_data is not None) and (closest_hit_data is None or closest_hit_data.t > hit_data.t):
                closest_hit_data = hit_data
            current_index += 1

        if closest_hit_data is None:
            unit_direction = ray.direction.normalize()
            t = 0.5 * unit_direction.y + 1.0
            return (1.0 - t) * Color.Color(1.0, 1.0, 1.0) + t * Color.Color(0.5, 0.7, 1.0)

        else:
            target = (closest_hit_data.normal + Vector.random()).normalize()
            return 0.5 * self.ray_color(Ray(closest_hit_data.point, target), depth-1)

    @staticmethod
    def is_ray_inside(ray, normal):
        return ray.scalar_product(normal) > 0.0
