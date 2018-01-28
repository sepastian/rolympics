import sys, os, random, math
import pyglet

sys.path.append(os.path.join(os.path.dirname(__file__), 'lib'))
from rolympics import resources as res
from rolympics import config
from rolympics.physical_object import PhysicalObject

gl_config = pyglet.gl.Config(sample_buffers=1, samples=2, double_buffer=True)
window = pyglet.window.Window(config.width, config.height, config=gl_config, vsync = False)

pyglet.gl.glClearColor(1,1,1,1)

def update(dt):
    # Move all objects.
    for obj in res.game_objects:
        obj.update(dt)
    # Detect and resolve collisions.
    i = 0
    while i < len(res.game_objects):
        obj1 = res.game_objects[i]
        j = i + 1
        while j < len(res.game_objects):
            obj2 = res.game_objects[j]
            # Compute collision manifold between obj1 and obj2.
            collision, cx, cy = obj1.collides_with(obj2)
            if collision:
                obj1.handle_collision(-cx, -cy)
                obj2.handle_collision(cx, cy)
            j += 1
            obj2.label.x, obj2.label.y = obj2.x, obj2.y-30
        i += 1
        obj1.label.x, obj1.label.y = obj1.x, obj1.y-30
        # Make objects bounce off borders
        r = obj1.radius
        minx, maxx, miny, maxy = config.fx0+r, config.fx1-r, config.fy0+r, config.fy1-r
        if not minx < obj1.x < maxx:
            obj1.vx *= -1
        if not miny < obj1.y < maxy:
            obj1.vy *= -1
        obj1.x = min(max(obj1.x, minx), maxx)
        obj1.y = min(max(obj1.y, miny), maxy)
    for obj in res.game_objects:
        obj.adjust(res.ball.x, res.ball.y)

#fps_display = pyglet.clock.ClockDisplay()

@window.event
def on_draw():
    window.clear()
    pyglet.gl.glLineWidth(5)
    config.batch.draw()
    #fps_display.draw()
    #pyglet.image.get_buffer_manager().get_color_buffer().save(file=p.stdin)

if __name__ == '__main__':
    pyglet.clock.schedule_interval(update, config.spf)
    #from PIL import Image
    #from subprocess import Popen, PIPE
    #p = Popen(['ffmpeg', '-y', '-f', 'image2pipe', '-vcodec', 'mjpeg', '-r', '24', '-i', '-', '-f', 'mpegts', 'udp://localhost:1234'], stdin=PIPE)
    pyglet.app.run()
