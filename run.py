import sys, os, random, math
import pyglet

sys.path.append(os.path.join(os.path.dirname(__file__), 'lib'))
from rolympics import resources as res
from rolympics import config
from rolympics.physical_object import PhysicalObject
from rolympics.robots import walker

gl_config = pyglet.gl.Config(sample_buffers=1, samples=2, double_buffer=True)
window = pyglet.window.Window(config.width, config.height, config=gl_config, vsync = False)

pyglet.gl.glClearColor(1,1,1,1)

def update(dt):
    for obj in res.game_objects:
        obj.update(dt)
    # detect collisions
    collisions = []
    i = 0
    while i < len(res.game_objects):
        obj1 = res.game_objects[i]
        j = i + 1
        while j < len(res.game_objects):
            obj2 = res.game_objects[j]
            d = obj1.distance_from(obj2)
            r = obj1.radius + obj2.radius
            overlap = r - d
            if overlap > 0:
                o = overlap/2
                dx, dy = (obj2.x - obj1.x)/d*o, (obj2.y - obj1.y)/d*o
                obj1.x -= dx
                obj1.y -= dy
                obj2.x += dx
                obj2.y += dy
            #if obj1.collides_with(obj2):
            #    collisions.append((obj1, obj2))
            j += 1
        i += 1
    # resolve collisions
    for collision in collisions:
        obj.resolve_collisions

fps_display = pyglet.clock.ClockDisplay()

@window.event
def on_draw():
    window.clear()
    pyglet.gl.glLineWidth(5)
    config.batch.draw()
    fps_display.draw()

if __name__ == '__main__':
    pyglet.clock.schedule_interval(update, config.spf)
    pyglet.app.run()
