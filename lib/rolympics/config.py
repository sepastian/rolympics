import pyglet

fps = 20
spf = 1/fps

# Screen.
height = 768
width = 1024

# Playing field.
vpad = 20
hpad = 50
fheight = height - 2 * vpad
fwidth = width - 2 * hpad
fx0, fx1, fy0, fy1 = hpad, hpad + fwidth, vpad, vpad + fheight

# Goal lines (lefthand/righthand).
glx0, gly0, glx1, gly1 = fx0, height//2-height//8, fx0, height//2+height//8
grx0, gry0, grx1, gry1 = fx1, height//2-height//8, fx1, height//2+height//8

batch = pyglet.graphics.Batch()
