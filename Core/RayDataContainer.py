
class RayDataContainer:

    def __init__(self):
        self.length_list = []
        self.point_list = []
        self.index_list = []

    def add_data(self, vector, index):
        self.length_list.append(vector.magnitude())
        self.point_list.append(vector)
        self.index_list.append(index)

    def get_closest_data(self):
        index = self.length_list.index(min(self.length_list))
        return (self.point_list[index], self.index_list[index])

    def __bool__(self):
        return bool(self.length_list)
