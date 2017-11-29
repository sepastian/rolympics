import sys
import pygame
from pygame.locals import *
import pymunk
from pymunk import pygame_util
import random

def main():
    pygame.init()
    screen = pygame.display.set_mode((600,600))
    pygame.display.set_caption("Blah!")
    clock = pygame.time.Clock()

    space = pymunk.Space()
    space.gravity = (0.0, -900.0)

    #lines = add_static_L(space)
    lines = add_L(space)
    balls = []
    print(dir(pymunk))
    draw_options = pymunk.pygame_util.DrawOptions(screen)

    ticks_to_next_ball = 10
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit(0)
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                sys.exit(0)

        ticks_to_next_ball -= 1
        if ticks_to_next_ball <= 0:
            ticks_to_next_ball = 25
            ball_shape = add_ball(space)
            balls.append(ball_shape)

        screen.fill((255,255,255))

        balls_to_remove = []
        for ball in balls:
            if ball.body.position.y < 150:
                space.remove(ball, ball.body)
                balls.remove(ball)
                
        space.debug_draw(draw_options)

        space.step(1/50.0)
        
        pygame.display.flip()
        clock.tick(50)

def add_ball(space):
    mass = 1
    radius = 14
    moment = pymunk.moment_for_circle(mass, 0, radius)
    body = pymunk.Body(mass, moment)
    x = random.randint(120,380)
    body.position = x, 550
    shape = pymunk.Circle(body,radius)
    space.add(body,shape)
    return shape

def draw_ball(screen, ball):
    p = int(ball.body.position.x), 600-int(ball.body.position.y)
    pygame.draw.circle(screen, (0,0,255), p, int(ball.radius), 2)

def add_static_L(space):
    body = pymunk.Body(body_type = pymunk.Body.STATIC)
    body.position = (300,300)
    l1 = pymunk.Segment(body, (-150,0), (255,0), 5)
    l2 = pymunk.Segment(body, (-150,0), (-150,50), 5)
    space.add(l1, l2)
    return l1, l2

def add_L(space):
    """Add a inverted L shape with two joints"""
    rotation_center_body = pymunk.Body(body_type = pymunk.Body.STATIC)
    rotation_center_body.position = (300,300)
    
    rotation_limit_body = pymunk.Body(body_type = pymunk.Body.STATIC)
    rotation_limit_body.position = (200,300)
    
    body = pymunk.Body(10, 10000)
    body.position = (300,300)
    l1 = pymunk.Segment(body, (-150, 0), (255.0, 0.0), 5.0)
    l2 = pymunk.Segment(body, (-150.0, 0), (-150.0, 50.0), 5.0)
    
    rotation_center_joint = pymunk.PinJoint(body, rotation_center_body, (0,0), (0,0))
    joint_limit = 25
    rotation_limit_joint = pymunk.SlideJoint(body, rotation_limit_body, (-100,0), (0,0), 0, joint_limit)
    
    space.add(l1, l2, body, rotation_center_joint, rotation_limit_joint)
    return l1,l2

if __name__ == '__main__':
    sys.exit(main())
