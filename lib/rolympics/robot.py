import pyglet
import random
import math
from rolympics import config
from rolympics import resources as res
from rolympics.physical_object import PhysicalObject

class Robot(PhysicalObject):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tx = self.x
        self.ty = self.y
        self.moving = False
        self.velocity = 150

    def update(self, dt):
        """
        Move towards target at set velocity.
        """
        if not self.moving:
            # Robobt has been paused, return.
            return
        # Get vector pointing towards target (direction of movement).
        dx, dy = self.tx - self.x, self.ty - self.y
        if abs(dx) < 1 and abs(dy) < 1:
            # Robot has reached its target, pause.
            # (Without this, robot will jump back and forth around target!)
            print('!', self.x, self.y, self.tx, self.ty, dx, dy)
            self.moving = False
            return
        # Normalize target vector to unit length.
        d = math.sqrt(dx**2 + dy**2)
        dx_norm, dy_norm = dx/d, dy/d
        # Update robot's position towards target at constant velocity.
        # Make sure to not move beyond target - robot would jump back and forth!
        mx, my = int(dx_norm * dt * self.velocity), int(dy_norm * dt * self.velocity)
        if abs(mx) > abs(dx):
            mx = dx
        if abs(my) > abs(dy):
            my = dy
        print(self.x, self.y, self.tx, self.ty, mx, my)
        self.x += mx
        self.y += my

    def adjust(self, bx, by):
        """
        Adjust robot's behavior by setting new target coordinates.
        """
        pass
