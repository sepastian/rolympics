import pyglet
import random
import math
from rolympics import config
from rolympics import resources as res
from rolympics.physical_object import PhysicalObject

class Ball(PhysicalObject):

    def update(self, dt):
        """
        """
        super().update(dt)
        # Did the ball pass the goal line?
        
        # Decrease ball's velocity.
        self.vx *= 1 - 1.0 * dt
        self.vy *= 1 - 1.0 * dt
        if abs(self.vx) < 0.1:
            self.vx = 0
        if abs(self.vy) < 0.1:
            self.vy = 0
        # Bounce the ball off any border to prevent dead locks.
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

    def bounce_off_borders(self):
        """
        Bounce off borders as other objects;
        do not bounce, when passing the goal line.
        """
        r = self.radius
        minx, maxx, miny, maxy = config.fx0+r, config.fx1-r, config.fy0+r, config.fy1-r
        if self.x <= minx and config.gly0 < self.y < config.gly1:
            res.score[0] += 1
            res.score_labels[0].text= str(res.score[0])
            res.scored = True
        elif self.x >= maxx and config.gry0 < self.y < config.gry1:
            res.score[1] += 1
            res.score_labels[1].text = str(res.score[1])
            res.scored = True
        super().bounce_off_borders()
