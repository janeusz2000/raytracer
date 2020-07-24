import pygame
import sys
import math
import contextlib

class GUI:

    def __init__(self, height, width, color_que):

        self.HEIGHT = height
        self.WIDTH = width
        self.color_que = color_que
        pygame.init()
        self.display_surface = pygame.display.set_mode((width, height))
        pygame.display.set_caption('Ray Tracer')
        self.screen = pygame.Surface((width, height))

    def quit(self):
        pygame.quit()

    def pixel_update(self, x, y, color):
        self.draw_pixel(x, y, color)

    def refresh(self):
        self.display_surface.blit(self.screen, (0, 0))
        pygame.display.update()

    def event_check(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

    @contextlib.contextmanager
    def locked(self):
        self.screen.lock()
        yield 
        self.screen.unlock()

    def draw_pixel(self, x, y, color):
        self.screen.set_at((x, y), self.get_color_py(color))

    def get_color_py(self, input_color):
        color = pygame.Color('black')
        color.r = round(math.sqrt(input_color.x) * 255)
        color.g = round(math.sqrt(input_color.y) * 255)
        color.b = round(math.sqrt(input_color.z) * 255)
        return color
