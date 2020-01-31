import random
import Ball
import Brick

pannel_red_width = 100
pannel_grey_width = 80
pannel_height = 20

gamebegin = False
MouseMove = False
lpointX = list()
lpointY = list()
lSz = list()
black_rect_height = 25
grey_frame_width = 8
blue_grey_height = black_rect_height + grey_frame_width

    
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

def draw_show():
    global ball
    global gamebegin
    textSize(32)
    if ball.move == False and gamebegin:
       text("Game Over!", 220, 300)
    else:
       global bricks
       score = 0
       for j in range (8):
         for i in range(10):
            if (bricks[j*10+i].active == False):
                score+=1
                
       if score==len(bricks):
          text("You Win!!!" , 220, 300)
          gamebegin = False
          ball.move = False
       else:
          text(score , 220, 300)   
          text("  /80" , 240, 300) 
       
         
def pannel(x):
    fill(255, 51, 0)
    rect(x, height * 0.9, pannel_red_width, pannel_height, 10, 10, 10, 10)
    fill(119, 117, 125)
    rect(x + 10, height * 0.9, pannel_grey_width, pannel_height)

def init():
    global ball
    ball.move = True
    global bricks
    for j in range (8):
        for i in range(10):
            bricks[j*10+i].active = True

def setup():
    background(0, 0, 0)
    size(600, 600)
    global pannelX
    pannelX = width / 2 - pannel_red_width / 2
    frameRate(50)
    
    global ball
    ball=Ball.Ball(pannel_red_width/2+pannelX,height * 0.9)
    global space 
    space = 1
    global brick_width 
    brick_width = ((width - grey_frame_width *2) / 10) + 0.3
    global bricks
    global brick_height 
    brick_height = brick_width / 2
    
    bricks = []
    for j in range (8):
        for i in range(10):
            bricks.append(Brick.Brick((grey_frame_width + space) + i * (brick_width), blue_grey_height + j * (brick_height), brick_width - space, brick_height-space))
               
def draw():
    global pannelX
    global MouseMove
    delta = 5
    global space 
    global brick_width
    global brick_height
    global gamebegin
    
    draw_rect_grey()
    draw_rect_blue()
    draw_star()
    pannel(pannelX) 
    global ball
    ball.update(pannelX,height * 0.9,grey_frame_width + 8,width - grey_frame_width - 8,blue_grey_height + 16,pannel_red_width,pannel_height)
    ball.draw()
    
    draw_show()
    
    global bricks
    for j in range (8):
        for i in range(10):
            bricks[j*10+i].hit_test(ball.pos_x,ball.pos_y) 
            if bricks[j*10+i].active:
                bricks[j*10+i].draw()
           

    if keyPressed:
        gamebegin = True
        if ball.move == False:
           init()
        if keyCode == LEFT:
            pannelX-=delta
        if keyCode == RIGHT:
            pannelX+=delta
        MouseMove=False
    else:
        if mousePressed:
            if mouseButton == LEFT:
                gamebegin= True
                MouseMove=True
                if ball.move == False:
                   init()
                
    if MouseMove:
        pannelX=mouseX 

    if pannelX > width - grey_frame_width - pannel_red_width:
        pannelX = width - grey_frame_width - pannel_red_width
    if pannelX < grey_frame_width:
        pannelX = grey_frame_width

    
    
    
    
    

    

        

        
        
    
