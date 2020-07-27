from Core.Viewer import Viewer
from Core.Vector import Vector
from Core.Camera import Camera
from Core.ImageGrid import ImageGrid
from Core.Objects import Sphere
from Core.Objects import TriangleFace
from Core.Objects import Surface
from Graphics import GUI
from Core.Color import Color

from Core import Materials
import queue
import threading
import logging
import cProfile
import pstats


def main():
    height = 400
    aspect_ratio = 16.0 / 9
    width = round(height * aspect_ratio)

    samples_per_pixel = 2
    max_depth = 10

    print("rendering image with width: {}, height: {}, pixels: {}, aspect_ratio: {}, total number of rays: {}".format(
        width, height, width * height,
        aspect_ratio, height * width * samples_per_pixel * max_depth))

    color_que = queue.SimpleQueue()

    tile_size = 50
    image_grid = ImageGrid(width, height, tile_size=tile_size)
    cords_queue = image_grid.get_cord_queue()

    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

    # Scene:

    camera = Camera(aspect_ratio, 1.0, origin=Vector(0, 0, -1))
    viewer = Viewer(height, width, object_list=[], samples_per_pixel=samples_per_pixel,
                    camera=camera, color_que=color_que, max_depth=max_depth)

    green_diffuse_material = Materials.MaterialDiffuse(Color(0, 1, 0))
    triangle = TriangleFace(green_diffuse_material, Vector(0, 0, 4), Vector(0, 4, 4), Vector(3, 0, 2))
    viewer.add_object(triangle)

    red_diffuse_material = Materials.MaterialMetal(color=Color(1, 0, 0), fuzz=0.01)
    sphere1 = Sphere(origin=Vector(0, 1, 3), radius=1, material=red_diffuse_material)
    viewer.add_object(sphere1)

    blue_diffuse_material = Materials.MaterialMetal(color=Color(0, 0, 1), fuzz=0.1)
    sphere2 = Sphere(origin=Vector(0, -3, 3), radius=3, material= blue_diffuse_material)
    viewer.add_object(sphere2)

    glass_material = Materials.MaterialGlass(color=Color(1, 1, 1), coefficient_refract=1)
    sphere2 = Sphere(origin=Vector(0, 1, 2), radius=0.4, material=glass_material)
    viewer.add_object(sphere2)

    yellow_diffuse_material = Materials.MaterialMetal(color=Color(1, 0, 1), fuzz=0.1)
    surface = Surface(material=yellow_diffuse_material, point_1=Vector(
        0, 1, 0), point_2=Vector(0, 1, 3), point_3=Vector(2, 1, 3))
    viewer.add_object(surface)

    def core_loop():
        t = threading.current_thread()
        logging.info("Core thread %s started", t.getName())
        while True:
            try:
                (x0, x1, y0, y1) = cords_queue.get(block=False)
                viewer.render(x0, x1, y0, y1)
            except queue.Empty:
                break

        logging.info("Core thread %s finished", t.getName())

    gui = GUI.GUI(height=height, width=width, color_que=color_que)
    gui.refresh()
    gui.event_check()

    def gui_loop(gui):

        logging.info("GUI thread started")
        pixel_iteration = 1
        while True:
            with gui.locked():
                try:
                    while True:
                        [x, y, current_color] = color_que.get(block=False)
                        gui.draw_pixel(x, y, current_color)
                except queue.Empty:
                    pass

            gui.event_check()
            gui.refresh()

    thread_list = []
    for a in range(6):
        thread_list.append(threading.Thread(target=core_loop))

    for thread in thread_list:
        thread.start()

    gui_loop(gui)

    for thread in thread_list:
        thread.join()


if __name__ == "__main__":
    main()

