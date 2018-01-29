import math
from random import randint
from rolympics import config
from rolympics import resources as res
from rolympics.robot import Robot

class StraightEdge(Robot):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name('straight')
        self.vx = 105
        self.vy = 100
        
    def update(self, dt):
        self.x = int(self.x + self.vx * dt)
        self.y = int(self.y + self.vy * dt)
        
    def adjust(self, bx, by):
        """
        Adjust target coordinates.
        """
        pass
