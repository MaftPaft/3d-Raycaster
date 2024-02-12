import pygame as pg
from math import *
from random import randint
from functions import *

white,black=(255,255,255),(0,0,0)
pg.init()
w,h=800,600
win=pg.display.set_mode((w,h))
fps=30
k=int(sqrt(w*h)/10)
s = CircleClass(w/2,h/2,10,white,500,90)
points=[]

for n in range(50):
    size=50
    x=randint(60,w-60)
    y=randint(60,h-60)
    points.append(((x,y),(x+50,y)))
    points.append(((x,y),(x,y-50)))
    points.append(((x,y-50),(x+50,y-50)))
    points.append(((x+50,y),(x+50,y-50)))
    


flat=[[0,0],[0,0]]

def reset(x1,y1):
    global points
    points.clear()
    for n in range(50):
        size=50
        x=randint(60,w-60)
        y=randint(60,h-60)
        amps=.1
        x-=(x-x1)*amps
        y-=(y-y1)*amps
        while x >= w+size:
            x=randint(60,w-60)
            x-=(x-x1)*amps
        while x <= size:
            x=randint(60,w-60)
            x-=(x-x1)*amps
        while y >= h+size:
            y=randint(60,h-60)
            y-=(y-y1)*amps
        while y <= size:
            y=randint(60,h-60)
            y-=(y-y1)*amps
        points.append(((x,y),(x+50,y)))
        points.append(((x,y),(x,y-50)))
        points.append(((x,y-50),(x+50,y-50)))
        points.append(((x+50,y),(x+50,y-50)))

angle=0
speed=5
turn=.05
wall=[]
run=True
clock=pg.time.Clock()
while run:
    mp=pg.mouse.get_pressed()
    mx,my=pg.mouse.get_pos()
    for i in pg.event.get():
        if i.type == pg.QUIT:
            run=False
    win.fill(black)

    if mp[0]:
        s.x,s.y=mx,my

    dt=fps/(1+clock.get_fps())

    # ARROW KEYS TO MOVE PLAYER
    kw=pg.key.get_pressed()[pg.K_UP]
    ka=pg.key.get_pressed()[pg.K_LEFT]
    kd=pg.key.get_pressed()[pg.K_RIGHT]
    if kw and not wall:
        s.x+=speed*sin(angle)
        s.y+=speed*cos(angle)
    if ka:
        angle-=turn
    if kd:
        angle+=turn
    if abs(angle) >= 6.2:
        angle=0

    
    if s.x > w+s.radius:
        reset(s.x,s.y)
        s.x=-s.radius
    if s.x < -s.radius:
        reset(s.x,s.y)
        s.x=w+s.radius
    if s.y > h+s.radius:
        reset(s.x,s.y)
        s.y=-s.radius
    if s.y < -s.radius:
        reset(s.x,s.y)
        s.y=h+s.radius
    for j in range(s.dy):
        #s.dx=max_ray_length
        #s.dy=FOV
        
        # Rays casted from the player
        P0,P1=rotate_transform(s.radius,radians(j)+angle-radians(s.dy/2),s.x,s.y),rotate_transform(s.dx,radians(j)+angle-radians(s.dy/2),s.x,s.y)
        
        # Collisions
        for p in points:
            clip = intersect_line_line_vec2(P0,P1,p[0],p[1])
            if clip:
                P1=clip
                d=hypot(s.x-clip[0],s.y-clip[1])
                nx=j*(w/s.dy)
                ny1=(h/100)/d*h
                ny0=-(h/100)/d*h
                colord=int(1/(d/255)*25)
                if colord >= 255:
                    colord =255
                elif colord <= 0:
                    colord = 0
                pg.draw.line(win,(colord,colord,colord),(nx,ny0+h/2),(nx,ny1+h/2),12)
                

    pg.display.update()
    clock.tick(fps)
