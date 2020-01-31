class Brick:
    def __init__(self, pos_x, pos_y, w, h):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.w = w
        self.h = h
        self.active = True
        
    def hit_test(self, x, y):
        # Returns true if the coordinate x, y is within the brick.
        if (x>self.pos_x) and (x<self.pos_x+self.w) and (y>self.pos_y) and (y<self.pos_y+self.h):
            self.active = False
    
    def draw(self):
        # Draws the brick on the screen
        fill(240, 10, 10)
        rect( self.pos_x,self.pos_y,self.w,self.h)
