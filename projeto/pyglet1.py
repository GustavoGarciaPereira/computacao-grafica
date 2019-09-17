import math
import pyglet
import numpy as np
from pyglet.gl import *

win = pyglet.window.Window()

# get all the points in a circle centered at 0.
def PointsInCircum(r, n=25, pi=3.14):
    return [(math.cos(2*pi/n*x)*r,math.sin(2*pi/n*x)*r) for x in range(0,n+1)]
pts = np.array(PointsInCircum(90))


def PointsInCircum2(r, n=50, pi=3.14):
    return [(math.cos(2*pi/n*x)*r,math.sin(2*pi/n*x)*r) for x in range(0,n+1)]
pts2 = np.array(PointsInCircum2(40))


# function that increments to the next
# point along a circle
frame = 0
def update_frame(x, y):
    global frame
    if frame == None or frame == pts.shape[0]-1:
        frame = 0
    else:
        frame += 1

@win.event
def on_draw():
    # clear the screen
    glClear(GL_COLOR_BUFFER_BIT)
    # draw the next line
    # in the circle animation
    # circle centered at 100,100,0 = x,y,z
    glBegin(GL_LINES)
    glVertex3f(100,100,0)
    glVertex3f(pts[frame][1]+100,pts[frame][0]+100,0)

    glVertex3f(400,400,0)
    glVertex3f(pts[frame][1]+400,pts[frame][0]+400,0)

    glVertex3f(100,300,0)
    glVertex3f(pts[frame][1]+100,pts[frame][0]+300,0)

    glEnd()


# every 1/10 th get the next frame
pyglet.clock.schedule(update_frame, 5/10.0)

pyglet.app.run()