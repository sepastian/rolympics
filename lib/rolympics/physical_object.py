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

    def collides_with(self, other):
        dx, dy = other.x - self.x, other.y - self.y
        r = self.radius + other.radius
        d = dx**2 + dy**2
        if d > r**2:
            # No collision.
            return False, 0, 0
        # Compute:
        #   - overlap o;
        #   - correction vector (=dist scaled to half the overlap)
        # Handle distance of zero (complete overlap).
        d = math.sqrt(d)
        o = (r - d)/2
        cx, cy = o, o
        if d > 0:
            cx, cy = dx/d*o, dy/d*o
        return True, cx, cy

    def handle_collision(self, cx, cy):
        self.x += cx
        self.y += cy

    def update(self, dt):
        self.x += self.vx * dt
        self.y += self.vy * dt

    def adjust(self, bx, by):
        pass
