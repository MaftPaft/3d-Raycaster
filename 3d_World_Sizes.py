import pygame as pg
from math import *
from functions import *
from random import randint

white,black=(255,255,255),(0,0,0)
pg.init()
w,h=2000,1400
win=pg.display.set_mode((w,h))
fps=90
s=CircleClass(w/3,h/2,5,white,600,120)

objs=[CircleClass(randint(50,w-50),randint(50,h-50),randint(0,50),(randint(0,255),randint(0,255),randint(0,255)),randint(int(h/8),h*8),0) for _ in range(50)]




speed=1.25
turn=0.025
angle=0
run=True
clock=pg.time.Clock()
while run:
    mx,my=pg.mouse.get_pos()
    mouserect=pg.rect.Rect(mx,my,12,12)
    mp=pg.mouse.get_pressed()
    for i in pg.event.get():
        if i.type == pg.QUIT:
            run=False
    win.fill(black)
    dt=fps/(1+clock.get_fps())

    kr=pg.key.get_pressed()[pg.K_RIGHT]
    kl=pg.key.get_pressed()[pg.K_LEFT]
    ku=pg.key.get_pressed()[pg.K_UP]
    kd=pg.key.get_pressed()[pg.K_DOWN]
    if ku:
        s.x+=speed*sin(angle)*dt
        s.y+=speed*cos(angle)*dt
    if kd:
        s.x-=speed*sin(angle)*dt
        s.y-=speed*cos(angle)*dt
    if kl:
        angle-=turn*dt
    if kr:
        angle+=turn*dt

    # s.draw(win)
    
    for j in range(s.dy):
        t=radians(j)
        P0,P1=rotate_transform(s.radius,t+angle-radians(s.dy/2),s.x,s.y),rotate_transform(s.dx,t+angle-radians(s.dy/2),s.x,s.y)
        orgP1=rotate_transform(s.dx,t+angle-radians(s.dy/2),s.x,s.y)
        clipped=[]
        data=[]
        bound1,bound2=w,0
        for o in objs:
            clip=interectLineCircle(P0,P1,(o.x,o.y),o.radius)
            if clip:
                if len(clip) >= 2:
                    c1=hypot(s.x-clip[0][0],s.y-clip[0][1])
                    c2=hypot(s.x-clip[1][0],s.y-clip[1][1])
                    if c1 <= c2:
                        d=c1
                        nx=j*(w/s.dy)
                        # player's height
                        ny1=(h/100)/d*h
                        # obj height
                        ny0=-(h/100)/d*h*(o.dx/h)
                        colord1=int(1/(d/(1+o.color[0]))*o.color[0]/10)
                        colord2=int(1/(d/(1+o.color[1]))*o.color[1]/10)
                        colord3=int(1/(d/(1+o.color[2]))*o.color[2]/10)
                        if colord1 >= 255:
                            colord1 = 255
                        if colord1 <= 0:
                            colord1 = 0
                        if colord2 >= 255:
                            colord2 = 255
                        if colord2 <= 0:
                            colord2 = 0
                        if colord3 >= 255:
                            colord3 = 255
                        if colord3 <= 0:
                            colord3 = 0
                        colord=(colord1,colord2,colord3)
                        if nx <= bound1 and nx >= bound2:
                            data.append([d,nx,ny1,ny0,colord])
                    else:
                        d=c2
                        nx=j*(w/s.dy)
                        # player's height
                        ny1=(h/100)/d*h
                        # obj height
                        ny0=-(h/100)/d*h*(o.dx/h)
                        colord1=int(1/(d/(1+o.color[0]))*o.color[0]/10)
                        colord2=int(1/(d/(1+o.color[1]))*o.color[1]/10)
                        colord3=int(1/(d/(1+o.color[2]))*o.color[2]/10)
                        if colord1 >= 255:
                            colord1 = 255
                        if colord1 <= 0:
                            colord1 = 0
                        if colord2 >= 255:
                            colord2 = 255
                        if colord2 <= 0:
                            colord2 = 0
                        if colord3 >= 255:
                            colord3 = 255
                        if colord3 <= 0:
                            colord3 = 0
                        colord=(colord1,colord2,colord3)
                        if nx <= bound1 and nx >= bound2:
                            data.append([d,nx,ny1,ny0,colord])
                else:
                    d=hypot(s.x-clip[0][0],s.y-clip[0][1])
                    nx=j*(w/s.dy)
                    # player's height
                    ny1=(h/100)/d*h
                    # obj height
                    ny0=-(h/100)/d*h*(o.dx/h)
                    colord1=int(1/(d/(1+o.color[0]))*o.color[0]/10)
                    colord2=int(1/(d/(1+o.color[1]))*o.color[1]/10)
                    colord3=int(1/(d/(1+o.color[2]))*o.color[2]/10)
                    if colord1 >= 255:
                        colord1 = 255
                    if colord1 <= 0:
                        colord1 = 0
                    if colord2 >= 255:
                        colord2 = 255
                    if colord2 <= 0:
                        colord2 = 0
                    if colord3 >= 255:
                        colord3 = 255
                    if colord3 <= 0:
                        colord3 = 0
                    colord=(colord1,colord2,colord3)
                    if nx <= bound1 and nx >= bound2:
                        data.append([d,nx,ny1,ny0,colord])
            
                    
        data.sort(key=(lambda x: x[0]), reverse=True)
        
        for d in data:
            # d nx ny1 ny0 colord
            pg.draw.line(win,d[4],(d[1],d[3]+h/2),(d[1],d[2]+h/2),int(w/100))
            
        # pg.draw.line(win,white,P0,P1)
    

    for i, o in enumerate(objs):
        # o.draw(win)
        if hypot(s.x-o.x,s.y-o.y) < o.radius+s.radius+5:
            a=atan2(s.x-o.x,s.y-o.y)
            s.x=(o.radius+s.radius+5)*sin(a)+o.x
            s.y=(o.radius+s.radius+5)*cos(a)+o.y
        for k in range(i+1,len(objs)):
            to=objs[k]
            if hypot(to.x-o.x,to.y-o.y) < to.radius+o.radius:
                a=atan2(to.x-o.x,to.y-o.y)
                to.x=(to.radius+o.radius)*sin(a)+o.x
                to.y=(to.radius+o.radius)*cos(a)+o.y

    pg.display.update()
    clock.tick(fps)
