from Core.Viewer import Viewer
from Core.Vector import Vector
from Core.Camera import Camera
from Core.ImageGrid import ImageGrid
from Objects.Sphere import Sphere
from Objects.TriangleFace import TriangleFace
from Graphics import GUI
from Core.Color import Color

import time
import queue
import threading
import logging


def main():
    height = 400
    aspect_ratio = 16.0 / 9
    width = round(height * aspect_ratio)

    samples_per_pixel = 2
    max_depth = 1

    print("rendering image with width: {}, height: {}, pixels: {}, aspect_ratio: {}, total number of rays: {}".format(
        width, height, width * height,
        aspect_ratio, height * width * samples_per_pixel * max_depth))

    color_que = queue.SimpleQueue()

    tile_size = 50
    image_grid = ImageGrid(width, height, tile_size=tile_size)
    cords_queue = image_grid.get_cord_queue()

    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

    camera = Camera(aspect_ratio, 1.0, origin=Vector(0, 0, -1))
    viewer = Viewer(height, width, object_list=[], samples_per_pixel=samples_per_pixel,
                    camera=camera, color_que=color_que, max_depth=max_depth)

    triangle = TriangleFace(Color(1, 0, 0), Vector(1, 2, 1), Vector(2, 1, 1), Vector(1, 1, 1))
    viewer.add_object(triangle)

    # sphere1 = Sphere(origin=Vector(0, 1, 3), radius=1)
    # viewer.add_object(sphere1)
    #
    # sphere2 = Sphere(origin=Vector(0, -3, 3), radius=3)
    # viewer.add_object(sphere2)

    # TODO core_loop() should take input: [[xb, xe], [yb, ye]] where xb corresponds to beginning, xe - end
    # TODO Make n -1 threads tha calculates ray-tracing, where  n is number of thread available on CPU
    # TODO Viewer object should be outside the class
    def core_loop():
        logging.info("Core thread started")
        time.sleep(0.001)
        while not cords_queue.empty():
            (x0, x1, y0, y1) = cords_queue.get()
            viewer.render(x0, x1, y0, y1)

    def gui_loop():
        logging.info("GUI thread started")
        gui = GUI.GUI(height=height, width=width, color_que=color_que)
        pixel_iteration = 1
        while True:
            try:
                [x, y, current_color] = color_que.get(block=False)
                gui.draw_pixel(x, y, current_color)
            except queue.Empty:
                pass
            pixel_iteration += 1
            gui.event_check()
            if pixel_iteration % 30 == 0:
                gui.refresh()
                pixel_iteration = 1

    threading.Thread(target=gui_loop).start()

    thread_list = []
    for a in range(1):
        thread_list.append(threading.Thread(target=core_loop))

    for thread in thread_list:
        thread.start()


if __name__ == "__main__":
    main()
