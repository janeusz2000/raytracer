import math
import abc
import random
from Core.Vector import Vector
from Core.Ray import Ray

from Core.Ray import Ray


class Material(abc.ABC):

    def scatter(self, point, normal, ray_direction):
        pass


class MaterialDiffuse(Material):

    def __init__(self, color):
        self.color = color

    def scatter(self, point, normal, ray_direction):
        random_vec = Vector.random()
        if normal.scalar_product(random_vec) < 0:
            random_vec = - random_vec

        scatter_direction = normal + random_vec
        return scatter_direction, self.color


class MaterialGlass(Material):

    def __init__(self, color, coefficient_refract):
        self.coefficient_refract = coefficient_refract
        self.color = color

    def scatter(self, point, normal, ray_direction):

        # TODO fix glass material because it deosn work as it is supposed. Porobably condition
        #  normal.scalar_product(ray_direction) > 0:is not right

        if normal.scalar_product(ray_direction) > 0:
            etai_over_etat = 1.0 / self.coefficient_refract
        else:
            etai_over_etat = self.coefficient_refract

        cos_theta = min((-ray_direction).scalar_product(normal), 0.0)
        sin_theta = math.sqrt(1.0 - cos_theta*cos_theta)

        if etai_over_etat * sin_theta > 1.0:
            scatter_direction = (ray_direction - 2 * (normal.scalar_product(ray_direction)) * normal).normalize()
            return scatter_direction, self.color

        reflect_prob = self.schlick(cos_theta, etai_over_etat)
        if random.random() < reflect_prob:
            scatter_direction = (ray_direction - 2 * (normal.scalar_product(ray_direction)) * normal).normalize()
            return scatter_direction, self.color

        scatter_direction = self.refract(ray_direction, normal, etai_over_etat)
        return scatter_direction, self.color

    @staticmethod
    def refract(uv, normal, etai_over_etat):
        cos_theta = (-uv).scalar_product(normal)
        r_out_perp = etai_over_etat * (uv + cos_theta * normal)
        r_out_parallel = math.sqrt(abs(1.0 - r_out_perp.magnitude2())) * normal
        return r_out_perp + r_out_parallel

    @staticmethod
    def schlick(cosine, ref_idx):
        r0 = (1.0 - ref_idx) / (1.0 + ref_idx)**2
        return r0 + (1 - r0)*(1-cosine)**5


class MaterialMetal(Material):

    def __init__(self, color,  fuzz=0):
        self.color = color
        self.fuzz = fuzz

    def scatter(self, point, normal, ray_direction):
        random_vec = Vector.random()
        if random_vec.scalar_product(normal) < 0:
            random_vec = - random_vec

        scatter_direction = (ray_direction - 2 * (
            normal.scalar_product(ray_direction))*normal + self.fuzz * random_vec).normalize()
        return scatter_direction, self.color

