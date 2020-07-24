import queue


class ImageGrid:

    def __init__(self, width, height, tile_size=50):
        self.width = width
        self.height = height
        self.tile_index = [0, 0]
        self.tile_size = tile_size

    def get_cord_queue(self):
        output_queue = queue.SimpleQueue()
        for y_index in range(int(self.height/self.tile_size)):
            for x_index in range(int(self.width/self.tile_size)):

                x0 = x_index * self.tile_size
                x1 = x0 + self.tile_size
                y0 = y_index * self.tile_size
                y1 = y0 + self.tile_size

                output_queue.put((x0, x1, y0, y1))

        return output_queue
