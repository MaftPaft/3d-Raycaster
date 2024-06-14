from math import *
from keyboard import is_pressed
from random import choice
import time

class display_print:
    def __init__(self,width,height,blanks=" ",border="*"):
        self.width=width
        self.height=height
        self.blanks=blanks
        self.border=border
        self.window=[["*" if w == 0 or w == self.width-1 or h == 0 or h == self.height-1 else self.blanks for w in range(self.width)] for h in range(self.height)]
        # self.fps=120
        
    def draw_poly(self,x,y,width,height,symbol="."):
        for h in range(height):
            for w in range(width):
                yy=y+h
                xx=x+w
                out=(yy<0 or yy >= self.height or xx < 0 or xx >= self.width)
                yy=0 if yy <= 0 else self.height-1 if yy >= self.height else yy
                xx=0 if xx <= 0 else self.width-1 if xx >= self.width else xx
                if not out:
                    self.window[yy][xx]=symbol
    def display(self):
        n=""
        for p in self.window:
            n+="".join(p)+"\n"
        print(n,end="\r")
    def refresh(self):
        for y in range(len(self.window)):
            for x in range(len(self.window[y])):
                self.window[y][x]=self.blanks
                self.window[0][x]=self.border
                self.window[self.height-1][x]=self.border
            self.window[y][0]=self.border
            self.window[y][self.width-1]=self.border
    def tick(self,fps):
        time.sleep(1/fps)

TS=10
MAP=[
    [1,1,1,1,1,1,1,1,1],
    [1,0,0,1,0,1,0,0,1],
    [1,0,1,1,0,1,1,0,1],
    [1,0,0,1,0,0,1,0,1],
    [1,0,0,0,0,0,0,0,1],
    [1,0,1,0,0,0,1,1,1],
    [1,0,1,1,1,0,0,0,1],
    [1,0,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1]
]
px,py=[len(MAP[0])/2*TS+TS/2,len(MAP)/2*TS+TS/2]
t=0
FOV=60
v=0
w,h=100,40
R=w
s=w/FOV

win=print_display(w,h)
run=True
while run:
    if is_pressed("a"):
        t-=.1
    elif is_pressed("d"):
        t+=.1
    if is_pressed("w"):
        v=1
    elif is_pressed("s"):
        v=-1
    else:
        v=0
    if v!=0:
        vx=px+sin(t)*v
        vy=py+cos(t)*v
        nx,ny=[int(vx/TS),int(vy/TS)]
        if nx >= 0 and nx < len(MAP[0]) and ny >= 0 and ny < len(MAP):
            if MAP[ny][nx]==0:
                px=vx
                py=vy
    for ray in range(FOV):
        for depth in range(R):
            # t=''
            angle=t+radians(ray)-radians(FOV/2)
            tx=depth*sin(angle)+px
            ty=depth*cos(angle)+py
            nx,ny=int(tx/TS),int(ty/TS)
            if nx >= 0 and nx < len(MAP[0]) and ny >= 0 and ny < len(MAP):
                if MAP[ny][nx] == 1:
                    a=atan2(tx-px,ty-py)
                    d=depth*cos(t-a)
                    wh=h*16/(d+.001)
                    x1=int(s*ray)
                    x2=int(s)+1
                    y1=int(h/2-wh/2)
                    y2=int(wh)
                    characters=list("@$KTMPRSUVWXYZOEANLktmprsuvwxyzoeanl!ʟᴋᴛᴍᴘʀsᴜᴠᴡxʏᴢᴏᴇᴀɴ,.^'ᵏᵗˡᵐᵖʳˢᵘᵛʷˣʸᶻᵒᵉᵃⁿ")
                    c=characters[0 if int(len(characters)/R*depth)-1 < 0 else int(len(characters)/R*depth)-1]
                    win.draw_poly(x1,y1,x2,y2,c)
                    break
    win.display()
    win.refresh()
    win.tick(10)
