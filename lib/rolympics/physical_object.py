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
        self.name('')

    def name(self, value):
        """
        Set the name of this object.
        """
        self.label = pyglet.text.Label(value, anchor_x='center', anchor_y='center',
                                       batch=config.batch, color=(0,0,0,255))

    def collides_with(self, other):
        """
        Check, if this object collides with other.

        If yes, return a correction vector, telling how much 
        each of the two objects must move to resolve the collision.

        If no, the vector will be (0,0).

        Returns (Boolean, int, int).
        """
        dx, dy = other.x - self.x, other.y - self.y
        r = self.radius + other.radius
        d = dx**2 + dy**2
        if d > r**2:
            # No collision.
            return False, 0, 0
        # Compute:
        #   - overlap o;
        #   - correction vector (=dist scaled to half the overlap)
        #
        # Handle distance of zero (complete overlap).
        d = math.sqrt(d)
        o = (r - d)/2
        cx, cy = o, o
        if d > 0:
            # If two objects collide frontally moving along
            # the same axis, they would block each other indefinitely.
            # A a little bit of randomness to each collision, to
            # prevent dead locks. Add between +/- 0.5% to each axis
            # of the collision vector.
            ex = dx * 0.01 * random.random() - 0.005
            ey = dy * 0.01 * random.random() - 0.005
            cx, cy = ((dx/d)+ex)*o, ((dy/d)+ey)*o
        return True, cx, cy

    def handle_collision(self, cx, cy):
        self.x = int(self.x + cx)
        self.y = int(self.y + cy)

    def update(self, dt):
        self.x = int(self.x + self.vx * dt)
        self.y = int(self.y + self.vy * dt)

    def bounce_off_borders(self):
        """
        Bounce off borders.
        """
        r = self.radius
        minx, maxx, miny, maxy = config.fx0+r, config.fx1-r, config.fy0+r, config.fy1-r
        if not minx < self.x < maxx:
            self.vx *= -1
        if not miny < self.y < maxy:
            self.vy *= -1
        self.x = self.limit(self.x, config.fx0, config.fx1)
        self.y = self.limit(self.y, config.fy0, config.fy1)

    def limit(self, value, min_value, max_value):
        """
        Limit value such that min_value <= value <= max_value.
        """
        return min(max(value, min_value+self.radius), max_value-self.radius)
        
    def adjust(self, bx, by):
        pass
