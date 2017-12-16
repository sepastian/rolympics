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

    #func = walker.step(res.robot.position, ((0,0),(config.width,config.height)))
    #func[0](res.robot, *func[1:])
    #action(res.robot, *args)

fps_display = pyglet.clock.ClockDisplay()

@window.event
def on_draw():
    window.clear()
    fps_display.draw()
    config.batch.draw()
    pyglet.gl.glLineWidth(10)
    pyglet.graphics.draw(4, pyglet.gl.GL_LINES,
                         ('v2i', (
                             10, 10,
                             10, config.height-10,
                             config.width-10, config.height-10,
                             config.width-10, 10
                         )),
                         ('c3B', (
                             0, 0, 255,
                             0, 255, 0,
                             255, 0, 0,
                             0, 0, 255
                         ))
    )

if __name__ == '__main__':
    pyglet.clock.schedule_interval(update, config.spf)
    pyglet.app.run()
