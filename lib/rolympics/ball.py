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
        # Make sure ball will never rest too close to border.
        if self.x <= config.fx0+self.radius or self.x >= config.fx1-self.radius:
            self.vx = (self.x - config.width//2) * 0.5
        if self.y <= config.fy0+self.radius or self.y >= config.fy1-self.radius:
            self.vy = (self.y - config.height//2) * 0.5

    def handle_collision(self, cx, cy):
        """
        Unlike a robot, the ball should bounce off,
        if a collision occured.
        """
        super().handle_collision(cx, cy)
        d = math.sqrt(cx**2 + cy**2)
        if d == 0:
            d = 1.0
        self.vx = cx/d * 100
        self.vy = cy/d * 100
