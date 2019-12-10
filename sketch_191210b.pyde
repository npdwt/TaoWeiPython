import random
char_width=20

def setup():
    size(640, 640)


def draw():
    for j in range(height/char_width):
       for i in range(width/char_width):
          draw_slash( random.random()>0.5 , char_width*i ,char_width*j)
          noLoop()
       
def draw_slash ( fwd_slash, top, left):
     if fwd_slash:
        line(left+char_width/2, top, left+char_width/2, top+char_width )
     else:
        line(left, top+char_width/2, left+char_width, top+char_width/2)
