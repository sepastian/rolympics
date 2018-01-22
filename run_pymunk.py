import sys, os, random, math
import pyglet
import pymunk, pymunk.pyglet_util
from pymunk.vec2d import Vec2d

sys.path.append(os.path.join(os.path.dirname(__file__), 'lib'))
from physical_object import PhysicalObject
from rolympics import resources as res
from rolympics import config

gl_config = pyglet.gl.Config(sample_buffers=1, samples=2, double_buffer=True)
window = pyglet.window.Window(config.width, config.height, config=gl_config, vsync = False)

#window = pyglet.window.Window(800,600)
pyglet.gl.glClearColor(1,1,1,1)

#fps = 5
#spf = 1/fps
#image = center_image(pyglet.resource.image('rolympic_games_200x138.png'))
#logo = pyglet.resource.image('rolympic_games_200x138.png')
#pyglet.sprite.Sprite(resources.logo, x=window.width//2, y=window.height//2, batch=config.batch)
#res.robot.velocity_x = 10
#res.robot.velocity_y = 10
#res.robot.rotation = random.randint(0,360)

def update(dt):
    r = 10
    for x in range(r):
        config.space.step(config.spf/r)
    res.robot.position = res.body.position
    res.robot.rotation = math.degrees(res.body.angle)

fps_display = pyglet.clock.ClockDisplay()
#options = pymunk.pyglet_util.DrawOptions(batch=config.batch)

@window.event
def on_draw():
    window.clear()
    fps_display.draw()
    config.batch.draw()
    #res.logo.draw()
    #print(res.robot.rotation)
    #config.space.debug_draw(options)

if __name__ == '__main__':
    pyglet.clock.schedule_interval(update, config.spf)
    pyglet.app.run()
