import abc


class Object(abc.ABC):

    @abc.abstractmethod
    def hit_object(self, ray):
        pass

    def normal(self, surface_point):
        pass


