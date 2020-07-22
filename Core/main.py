from Core.Viewer import Viewer
from Objects.Sphere import Sphere
from Core.Vector import Vector
from Core.Camera import Camera
from Graphics import GUI

import queue
import threading
import logging


def main():

    height = 400
    aspect_ratio = 16.0/9
    width = round(height * aspect_ratio)
    samples_per_pixel = 4
    color_que = queue.SimpleQueue()

    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

    # TODO core_loop() should take input: [[xb, xe], [yb, ye]] where xb corresponds to beginning, xe - end
    # TODO Make n -1 threads tha calculates ray-tracing, where  n is number of thread available on CPU
    # TODO Viewer object should be outside the class

    def core_loop():
        logging.info("thread_1 start")
        camera = Camera(aspect_ratio, 1.0, origin=Vector(0, 0, -1))
        viewer = Viewer(height, width, object_list=[], samples_per_pixel=samples_per_pixel,
                        camera=camera, color_que=color_que, max_depth=5)

        sphere1 = Sphere(origin=Vector(0, 1, 3), radius=1)
        viewer.add_object(sphere1)

        sphere2 = Sphere(origin=Vector(0, -3, 3), radius=3)
        viewer.add_object(sphere2)

        viewer.render()
        logging.info("thread_1 end")

    def gui_loop():
        logging.info("thread_2 start")
        gui = GUI.GUI(height=height, width=width, color_que=color_que)
        pixel_iteration = 1
        while True:
            [x, y, current_color] = color_que.get()
            pixel_iteration += 1
            if current_color is not None:
                gui.draw_pixel(x, y, current_color)
            if pixel_iteration % 30 == 0:
                gui.refresh()
                pixel_iteration = 1
            gui.event_check()

    thread_1 = threading.Thread(target=core_loop)
    thread_2 = threading.Thread(target=gui_loop)
    thread_1.start()
    thread_2.start()


if __name__ == "__main__":
    main()







