import pyglet
import random
import math
from rolympics import config
from rolympics import resources as res
from rolympics.physical_object import PhysicalObject

class Robot(PhysicalObject):
    
    def adjust(self, bx, by):
        dx = config.fx1 - bx + 100
        dy = config.height//2 - by + 100
        tx = config.fx1 - dx
        ty = config.height//2 - dy
        print(tx, ty)
        self.vx = tx - self.x
        self.vy = ty - self.y

