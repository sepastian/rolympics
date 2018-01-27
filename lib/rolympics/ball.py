import pyglet
import random
import math
from rolympics import config
from rolympics import resources as res
from rolympics.physical_object import PhysicalObject

class Ball(PhysicalObject):

    def update(self, dt):
        super().update(dt)
        self.vx *= 1 - 1.0 * dt
        self.vy *= 1 - 1.0 * dt
        if abs(self.vx) < 2:
            self.vx = 0
        if abs(self.vy) < 2:
            self.vy = 0

    def handle_collision(self, cx, cy):
        super().handle_collision(cx, cy)
        d = math.sqrt(cx**2 + cy**2)
        self.vx = cx/d * 100
        self.vy = cy/d * 100
