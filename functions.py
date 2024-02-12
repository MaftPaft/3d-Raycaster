import pygame as pg
from math import *

## FUNCTIONS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_collision_and_intesection.md {
def intersect_line_line_vec2(startObs, endObs, origin, endpoint):
    P = pg.Vector2(startObs)
    R = (endObs - P)
    Q = pg.Vector2(origin)
    S = (endpoint - Q)
    d = R.dot((S.y, -S.x))
    if d == 0:
        return None
    t = (Q-P).dot((S.y, -S.x)) / d 
    u = (Q-P).dot((R.y, -R.x)) / d
    if 0 <= t <= 1 and 0 <= u <= 1:
        X  =  P + R * t
        return (X.x, X.y)
    return None
# ------------ }

#https://stackoverflow.com/questions/74592905/line-collision-detector-with-circles {
def sign(x):
    return -1 if x < 0 else 1

def interectLineCircle(l1, l2, cpt, r):
    x1 = l1[0] - cpt[0]
    y1 = l1[1] - cpt[1]
    x2 = l2[0] - cpt[0]
    y2 = l2[1] - cpt[1]
    dx = x2 - x1
    dy = y2 - y1
    dr = sqrt(dx*dx + dy*dy)
    D = x1 * y2 - x2 * y1
    discriminant = r*r*dr*dr - D*D
    if discriminant < 0:
        return []
    if discriminant == 0:
        xa = (D * dy ) /  (dr * dr)
        ya = (-D * dx ) /  (dr * dr)
        ta = (xa-x1)*dx/dr + (ya-y1)*dy/dr
        return [(xa + cpt[0], ya + cpt[1])] if 0 < ta < dr else []
    
    xa = (D * dy + sign(dy) * dx * sqrt(discriminant)) / (dr * dr)
    ya = (-D * dx + abs(dy) * sqrt(discriminant)) / (dr * dr)
    ta = (xa-x1)*dx/dr + (ya-y1)*dy/dr
    xpt = [(xa + cpt[0], ya + cpt[1])] if 0 < ta < dr else []
    
    xb = (D * dy - sign(dy) * dx * sqrt(discriminant)) / (dr * dr) 
    yb = (-D * dx - abs(dy) * sqrt(discriminant)) / (dr * dr)
    tb = (xb-x1)*dx/dr + (yb-y1)*dy/dr
    xpt += [(xb + cpt[0], yb + cpt[1])] if 0 < tb < dr else []
    return xpt
# } --------------


def rotate_transform(length,angle,x,y):
    x1 = length*sin(angle)+x
    y1 = length*cos(angle)+y
    return [x1,y1]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class CircleClass(object):
    data={}
    def __init__(self, x, y, radius, color, dex, dey):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.dx = dex
        self.dy = dey


    #draw your circle class on the screen
    def draw(self, window):
        pg.draw.circle(window, self.color, (self.x, self.y), self.radius)
