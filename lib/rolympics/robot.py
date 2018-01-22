import math
import random
import pyglet
from rolympics.physical_object import PhysicalObject

class Robot(PhysicalObject):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.w = self.image.get_max_width()
        self.h = self.image.get_max_height()

    def walk_to(self, x, y):
        self.vx = (x - self.x) * 0.5
        self.vy = (y - self.y) * 0.5
        self.rotation = math.degrees(math.atan(self.vy/self.vx))
