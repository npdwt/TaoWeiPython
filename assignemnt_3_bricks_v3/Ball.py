class Ball:
    def __init__(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.speed_x = 4
        self.speed_y = -4
        self.move = False
    
    def update(self,Px,Py,Wxmin,Wxmax,Wymin,Pw,Ph,Pm):
            # updates the position of the ball according to game physics.
            if (self.pos_x>Wxmax) or (self.pos_x<Wxmin):  
                self.speed_x*=-1
       
            if (self.pos_y<Wymin):  
                self.speed_y=4
            
            if (self.pos_y>Py) and (self.pos_y<Py+Ph) and (self.pos_x>Px) and (self.pos_x<Px+Pw) : 
                self.pos_y=Py 
                if Pm:
                    self.speed_y=-10
                else:
                    self.speed_y=-4
       
            if (self.pos_y>Py+Ph) or self.move == False:
                self.pos_x = Pw/2+Px
                self.pos_y = Py
                self.speed_y = -4 
                self.move = False
         
            if (self.move):
                self.pos_x += self.speed_x 
                self.pos_y += self.speed_y 
                
        
    def draw(self):
        # Draws the ball on the screen
        fill(255)
        circle(self.pos_x,self.pos_y,10)
