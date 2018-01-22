from rolympics.moves import rotate, move
import random

def step(position, bounds):
    print(position, bounds)
    x, y = position
    mx, my = bounds[1]
    if 0 < x < mx and 0 < y < my:
        if random.random() < 0.9:
            return move,
        else:
            return rotate, 10
    else:
        return rotate, random.randint(0,90)
