import abc


class Object(abc.ABC):

    @abc.abstractmethod
    def hit_object(self, ray):
        pass

    def get_material(self):
        pass

    def normal(self, surface_point):
        pass

    def random_in_unit(self):
        pass

