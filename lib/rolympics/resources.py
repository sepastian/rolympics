import math, random
import pyglet
#import pymunk

from rolympics import config
from rolympics.robot import Robot
from rolympics.physical_object import PhysicalObject

pyglet.resource.path = ['./resources']
pyglet.resource.reindex()

def center_image(img):
    """
    Set pivot point to center of image.
    """
    img.anchor_x = img.width//2
    img.anchor_y = img.height//2
    return img

# Load resources.
#
# Rolympics logo.
logo = pyglet.sprite.Sprite(
    center_image(pyglet.resource.image('rolympic_games_200x138.png')),
    batch=config.batch, x=config.width//2, y=config.height//2)

# Playing field.
#x0, x1, y0, y1 = 50, config.width-50, 20, config.height-20
x0, x1, y0, y1 = config.fx0, config.fx1, config.fy0, config.fy1
config.batch.add(
    4, pyglet.gl.GL_LINE_LOOP, None,
    ('v2i', (
        x0, y0,
        x0, y1,
        x1, y1,
        x1, y0
    )),
    ('c3B',
     [ v for v in (200,200,200) for i in range(4) ]
    )
)
config.batch.add(
    2, pyglet.gl.GL_LINES, None,
    ('v2i', (
        config.width//2, y0,
        config.width//2, y1
    )),
    ('c3B', (
        [ v for v in (200,200,200) for i in range(2) ]
    ))
)
# Left-hand goal.
config.batch.add(
    6, pyglet.gl.GL_LINES, None,
    ('v2i', (
        x0, config.height//2-config.height//8,
        10, config.height//2-config.height//8,
        10, config.height//2-config.height//8,
        10, config.height//2+config.height//8,
        10, config.height//2+config.height//8,
        x0, config.height//2+config.height//8
    )),
    ('c3B', (
        [ v for v in (0,0,0) for i in range(6) ]
    ))
)
# Right-hand goal.
config.batch.add(
    6, pyglet.gl.GL_LINES, None,
    ('v2i', (
        x1, config.height//2-config.height//8,
        config.width-10, config.height//2-config.height//8,
        config.width-10, config.height//2-config.height//8,
        config.width-10, config.height//2+config.height//8,
        config.width-10, config.height//2+config.height//8,
        x1, config.height//2+config.height//8
    )),
    ('c3B', (
        [ v for v in (0,0,0) for i in range(6) ]
    ))
)

# Robot.
robot_animation = pyglet.image.Animation.from_image_sequence(
    [
        center_image(pyglet.resource.image('r_e_b_0.png')),
        center_image(pyglet.resource.image('r_e_b_1.png')),
        center_image(pyglet.resource.image('r_e_b_2.png')),
        center_image(pyglet.resource.image('r_e_b_3.png'))
    ],
    0.5/4.0,
    True)
x = config.width//2
y = config.height//2
#x, y = 0, 0
#robot = Robot(robot_animation, batch=config.batch, x=x, y=y)
#robot.rotation = random.randint(0,360)
game_objects = []
for i in range(50):
    robot = PhysicalObject(center_image(pyglet.resource.image('robot.png')), batch=config.batch, x=config.width//2+random.randint(-50,50), y=config.height//2+random.randint(-50,50))
    robot.rotation = 0
    robot.vx = random.randint(-100,100)
    robot.vy = random.randint(-100,100)
    game_objects.append(robot)

# #robot = Robot(robot_animation, batch=config.batch, x=config.width//2-100, y=config.height//2)
# robot = PhysicalObject(center_image(pyglet.resource.image('robot.png')), batch=config.batch, x=config.width//2-100, y=config.height//2)
# robot.rotation = 90
# robot.vx = 40
# robot.vy = 2
# game_objects.append(robot)
# #robot = Robot(robot_animation, batch=config.batch, x=config.width//2+100, y=config.height//2)
# robot = PhysicalObject(center_image(pyglet.resource.image('robot.png')), batch=config.batch, x=config.width//2+100, y=config.height//2)
# robot.rotation = -90
# robot.vx = -30
# robot.vy = -5
# game_objects.append(robot)

# robot = PhysicalObject(center_image(pyglet.resource.image('robot.png')), batch=config.batch, x=config.width//2, y=config.height//2-50)
# robot.rotation = -90
# robot.vx = -4
# robot.vy = 30
# game_objects.append(robot)

#radians = -math.radians(robot.rotation-90)
#robot.vx = math.cos(radians) * 60
#robot.vy = math.sin(radians) * 60
#robot.walk_to(100,100)

# Ball.
ball = PhysicalObject(center_image(pyglet.resource.image('ball.png')), batch=config.batch, x=config.width//2, y=config.height//2)
ball.vx = 20
ball.vy = 20
game_objects.append(ball)
