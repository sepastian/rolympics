import math

def rotate(robot, angle):
    robot.rotation += angle

def move(robot):
    radians = -math.radians(robot.rotation)
    robot.x += int(math.cos(radians))*5
    robot.y += int(math.sin(radians))*5
