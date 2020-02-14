import random
import Ball
import Brick

BallNum=3
sec=0.0
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
brickwidth = 0
brickheight = 0
result = True
PannelMove = False
    
def draw_rect_grey():
    fill(119, 117, 125)
    rect(0, black_rect_height, width, height - black_rect_height)

def draw_rect_blue():
    fill(23, 15, 87)
    rect(grey_frame_width, blue_grey_height, width - grey_frame_width * 2, height - blue_grey_height)

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
    global BallNum
    global ball
    global gamebegin
    global brickwidth
    global brickheight
    global sec
    global result
    
    textSize(16)
    score = 0
    #print(BallNum)
    if BallNum==3:
        circle(10,10,10)
        circle(30,10,10)
        circle(50,10,10)
    if BallNum==2:
        circle(10,10,10)
        circle(30,10,10)
    if BallNum==1:
        circle(10,10,10)
    
    global bricks
    NotOver=False
    count=0
    for j in range (brickheight):
       for i in range(brickwidth):
           if (bricks[j*brickwidth+i].active == False and bricks[j*brickwidth+i].colour=='r'):
               count+=1
               score+=200
           if (bricks[j*brickwidth+i].active == False and bricks[j*brickwidth+i].colour=='b'):
               count+=1
               score+=100    
           if bricks[j*brickwidth+i].active:
               NotOver=True
    #print(NotOver)             
    if ball.move == False and gamebegin:
        if BallNum==0:
            text("Game Over!", 220, 300)
    print(sec)    
    if NotOver==False:
        if result:
           sec=(millis()-sec)/1000
           result = False
        text("You Won in " + nf(sec, 0, 1) + "S!" , 220, 300) 
        text("You Cleared " + nf(count/sec,0,1) + "bricks/seconds", 220, 340)   
        gamebegin = False
        ball.move = False
    
    fill(255)
    text(score , 500, 20)  
       
       
         
def pannel(x):
    fill(255, 51, 0)
    rect(x, height * 0.9, pannel_red_width, pannel_height, 10, 10, 10, 10)
    fill(119, 117, 125)
    rect(x + 10, height * 0.9, pannel_grey_width, pannel_height)

def init():
    global ball
    ball.move = True
    global bricks
    global brickwidth
    global brickheight
    global BallNum
    global sec
    
    BallNum-=1
    if BallNum<0:
        BallNum=2
        sec=millis()*1.0
        result=True
        for j in range (brickheight):
            for i in range(brickwidth):
                if bricks[j*brickwidth+i].colour=='r' or bricks[j*brickwidth+i].colour=='b':
                    bricks[j*brickwidth+i].active = True

def setup():
    size(600, 600)
    global pannelX
    pannelX = width / 2 - pannel_red_width / 2
    global PrePannelX
    PrePannelX = pannelX
    frameRate(50)
    global brickwidth
    global brickheight  
    global lines
    lines = loadStrings("Brick.txt")
    brickheight=len(lines)
    for line in lines:
        if len(line)>brickwidth:
            brickwidth=len(line)
    global ball
    ball=Ball.Ball(pannel_red_width/2+pannelX,height * 0.9)
    global space 
    space = 1
    global brick_width 
    brick_width = ((width+0.1 - (grey_frame_width *2)) / brickwidth) 
    global bricks
    global brick_height 
    global lines
    brick_height = brick_width / 2
    bricks = []
    for j in range(brickheight):
        for i in range(brickwidth):
            if i<len(lines[j]) and (lines[j][i]=='r' or lines[j][i]=='b'):
               bricks.append(Brick.Brick((grey_frame_width + space) + i * (brick_width), blue_grey_height + j * (brick_height), brick_width - space, brick_height-space,lines[j][i],True))
            else:
               bricks.append(Brick.Brick((grey_frame_width + space) + i * (brick_width), blue_grey_height + j * (brick_height), brick_width - space, brick_height-space,'',False))
      
                  
def draw():
    global pannelX
    global PrePannelX
    global MouseMove
    delta = 5
    global space 
    global brick_width
    global brick_height
    global gamebegin
    global brickwidth
    global brickheight
    background(0, 0, 0)
    draw_rect_grey()
    draw_rect_blue()
    draw_star()
    pannel(pannelX) 
    global ball
    global PannelMove
    ball.update(pannelX,height * 0.9,grey_frame_width + 8,width - grey_frame_width - 8,blue_grey_height + 16,pannel_red_width,pannel_height,PannelMove)
    ball.draw()
    
    draw_show()
    
    global bricks
    for j in range (brickheight):
        for i in range(brickwidth):
            bricks[j*brickwidth+i].hit_test(ball.pos_x,ball.pos_y) 
            if bricks[j*brickwidth+i].active and bricks[j*brickwidth+i].colour=='r':
                fill(240, 10, 10)
                bricks[j*brickwidth+i].draw()
            if bricks[j*brickwidth+i].active and bricks[j*brickwidth+i].colour=='b':
                fill(51, 91, 255)
                bricks[j*brickwidth+i].draw()
    global sec
    if keyPressed:
        if gamebegin == False:
            sec=millis()*1.0
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
                if gamebegin == False:
                   sec=millis()*1.0
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

    if PrePannelX <> pannelX:
        PannelMove = True
        PrePannelX = pannelX
    else:
        PannelMove = False
    
    
    
    

    

        

        
        
    
