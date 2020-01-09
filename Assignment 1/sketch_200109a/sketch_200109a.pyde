import random
x = 0
MouseMove = False
lpointX = list()
lpointY = list()
lSz = list()
black_rect_height = 25
grey_frame_width = 8
blue_grey_height = black_rect_height + grey_frame_width

pannel_red_width = 100
pannel_grey_width = 80
pannel_height = 20


def setup():
    background(0, 0, 0)
    size(600, 600)
    global x
    x = width / 2 - pannel_red_width / 2
    frameRate(50)
    
    
def draw_rect_grey():
    fill(119, 117, 125)
    rect(0, black_rect_height, width, height - black_rect_height)

def draw_rect_blue():
    fill(23, 15, 87)
    rect(grey_frame_width, blue_grey_height, width - grey_frame_width * 2, height - blue_grey_height)

def draw_rect_small_red():
    fill(240, 10, 10)
    rect(grey_frame_width, blue_grey_height,(width - grey_frame_width * 2) / 10, (width - grey_frame_width * 2) / 10 / 2)

def draw_sparkle(i):
    fill(i)
    rect(-2,-2,4,4)

def draw_star():
    global lpointX 
    global lpointY 
    global lSz

    col2=-1676082
    #something special here to translte 
    #at random
    x=map(random.random(),0,1,8,580)
    y=map(random.random(),0,1,40,600)
    pushMatrix()
    translate(x,y)
    rotate(PI/4)
    sz=map(random.random(),0,1,0.5,1)
    scale(sz,sz)
    draw_sparkle(255)
    popMatrix()
    lpointX.append(x)
    lpointY.append(y)
    lSz.append(sz)

    for i in range(len(lpointX)-1):
        #something special here to translte 
        #at random
        x=lpointX[len(lpointX)-i-1]
        y=lpointY[len(lpointX)-i-1]
        if get(int(x),int(y)) == col2:
            continue
        #print(get(int(x),int(y)))
        pushMatrix()
        translate(x,y)
        rotate(PI/4)
        sz=lSz[len(lpointX)-i-1]
        scale(sz,sz)
        draw_sparkle(255-i)
        popMatrix()
        
    if len(lpointX)>100:
        lpointX.pop(0)
        lpointY.pop(0)
        lSz.pop(0)
        
def draw():
    global x
    global MouseMove
    delta = 5
    space = 1
    brick_width = ((width - grey_frame_width *2) / 10) + 0.3
    brick_height = brick_width / 2


    draw_rect_grey()
    draw_rect_blue()
    draw_star()
    draw_rect_small_red()
    
    
    for j in range (8):
        for i in range(10):
            rect((grey_frame_width + space) + i * (brick_width), blue_grey_height + j * (brick_height), brick_width - space, brick_height-space)


    if keyPressed:
        if keyCode == LEFT:
            x-=delta
        if keyCode == RIGHT:
            x+=delta
        MouseMove=False
    else:
        if mousePressed:
            if mouseButton == LEFT:
                MouseMove=True
                
    if MouseMove:
        x=mouseX 

    if x > width - grey_frame_width - pannel_red_width:
        x = width - grey_frame_width - pannel_red_width
    if x < grey_frame_width:
        x = grey_frame_width

    pannel(x) 

def pannel(x):
    fill(255, 51, 0)
    rect(x, height * 0.9, pannel_red_width, pannel_height, 10, 10, 10, 10)
    fill(119, 117, 125)
    rect(x + 10, height * 0.9, pannel_grey_width, pannel_height)
