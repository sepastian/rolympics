import pyglet
import random
import math
from rolympics import config
from rolympics import resources as res

class PhysicalObject(pyglet.sprite.Sprite):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.vx, self.vy = 0.0, 0.0
        self.radius = self.image.width//2

    def distance_from(self, other):
        dx, dy = other.x - self.x, other.y - self.y
        d = math.sqrt(dx**2 + dy**2)
        return d

    def collides_with(self, other):
        #dx, dy = other.x - self.x, other.y - self.y
        r = self.radius + other.radius
        return self.distance_to(other) < r**2
        #return (self.x - other.x)**2 + (self.y - other.y)**2 < r**2
        d2 = dx**2 + dy**2 # distance squared
        if d2 > r**2:
            return false
        d = math.sqrt(d2) # distance
        if d != 0:
            return true, r-d, t/d
            penetration = r - d

    def resolve_collisions(self):
        for other in res.game_objects:
            pass

    def update(self, dt):
        self.x += self.vx * dt
        self.y += self.vy * dt
