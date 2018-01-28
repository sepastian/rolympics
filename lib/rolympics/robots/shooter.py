import math
from random import randint
from rolympics import config
from rolympics import resources as res
from rolympics.robot import Robot

class Shooter(Robot):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name('shooter')

    def adjust(self, bx, by):
        """
        Adjust target coordinates.
        """
        if not self.moving:
            self.tx = randint(config.fx0+self.radius+10, config.fx1-self.radius-10)
            self.ty = randint(config.fy0+self.radius+10, config.fy1-self.radius-10)
            self.moving = True
