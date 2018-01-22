import pyglet

fps = 20
spf = 1/fps
height = 768
width = 1024
#height = 480
#width = 600
vpad = 20
hpad = 50
fheight = height - 2 * vpad
fwidth = width - 2 * hpad
fx0, fx1, fy0, fy1 = hpad, hpad + fwidth, vpad, vpad + fheight

batch = pyglet.graphics.Batch()
