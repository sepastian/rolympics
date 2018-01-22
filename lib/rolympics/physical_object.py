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
        dx, dy = other.x - self.x, other.y - self.y
        r = self.radius + other.radius
        d = dx**2 + dy**2
        if d > r**2:
            # No collision.
            return False, 0, 0
        # Compute overlap o;
        # compute correction vector (cx,cy)
        # as distance between objects,
        # scaled to half the overlap.
        d = math.sqrt(d)
        o = (r - d)/2
        return True, dx/d*o, dy/d*o
    
    def resolve_collisions(self):
        for other in res.game_objects:
            pass

    def update(self, dt):
        self.x += self.vx * dt
        self.y += self.vy * dt
