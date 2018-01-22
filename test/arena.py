import sys
import pygame
from pygame.locals import *
import pymunk
from pymunk import pygame_util
import random
from itertools import chain

WIDTH=800
HEIGHT=600

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH,HEIGHT))
    pygame.display.set_caption("Arena!")
    clock = pygame.time.Clock()

    space = pymunk.Space()
    space.gravity = (0.0, -0.0)

    lines = add_borders(space)
    #xs = list(chain(*[ ((l.body.position + l.a).x, (l.body.position + l.b).x) for l in borders ]))
    #ys = list(chain(*[ ((l.body.position + l.a).y, (l.body.position + l.b).y) for l in borders ]))
    #border_rect = pygame.Rect(min(xs), min(ys), max(xs), max(ys))
    draw_options = pymunk.pygame_util.DrawOptions(screen)

    for i in range(10):
        add_vehicle(space)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit(0)
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                sys.exit(0)
        screen.fill((255,255,255))
        #space.debug_draw(draw_options)
        draw_arena(screen, lines)
        draw_vehicles(screen, vehicles)
        space.step(1/50.0)
        pygame.display.flip()
        clock.tick(50)

def draw_arena(screen, lines):
    """
    Draw borders of arena and middle line.
    """
    points = []
    color_white = Color(250,250,250)
    color_gray = Color(128,128,128)
    pygame.draw.line(screen, color_gray, (WIDTH/2,10), (WIDTH/2,HEIGHT-10), 1)
    pygame.draw.circle(screen, color_gray, (int(WIDTH/2),int(HEIGHT/2)), int(HEIGHT/8), 1)
    for l in lines:
        pygame.draw.line(screen, color_white, l.body.position+l.a, l.body.position+l.b, 4)

def draw_vehicles(screen, vehicles):
    for v in vehicles:
        p = (int(v.body.position.x), int(HEIGHT - v.body.position.y))
        pygame.draw.circle(screen, (0,0,255), p, int(v.radius), 2)

def add_vehicle(space):
    mass = 10
    radius = 14
    moment = pymunk.moment_for_circle(mass, 0, radius)
    body = pymunk.Body(mass, moment)
    body.position = random.randint(0,WIDTH), random.randint(0,HEIGHT)
    body.velocity = (-20+random.randint(0,40)*10, -20+random.randint(0,40)*10)
    shape = pymunk.Circle(body, radius)
    space.add(body, shape)
    return shape

def add_borders(space):
    """
    Draw a playing field with 2 goals (holes):

    +-----------+
    |           |

    |           |
    +-----------+
    """
    body = pymunk.Body(body_type=pymunk.Body.STATIC)
    body.position = (WIDTH/2,HEIGHT/2)
    # left, right, top, bottom, center, middle
    l,r,t,b,c,m = -WIDTH/2+10, WIDTH/2-10, -HEIGHT/2+10, HEIGHT/2-10, 0, 0
    size_of_goal = HEIGHT/3
    # top/bottom of goals
    gt, gb = m - size_of_goal/2, m + size_of_goal/2
    lines = [
        pymunk.Segment(body, (l,t), (r,t), 4.0),
        pymunk.Segment(body, (r,t), (r,gt), 4.0),
        pymunk.Segment(body, (r,gb), (r,b), 4.0),
        pymunk.Segment(body, (r,b), (l,b), 4.0),
        pymunk.Segment(body, (l,b), (l,gb), 4.0),
        pymunk.Segment(body, (l,gt), (l,t), 4.0)
    ]
    for line in lines:
        space.add(line)
    return lines

if __name__ == '__main__':
    sys.exit(main())
