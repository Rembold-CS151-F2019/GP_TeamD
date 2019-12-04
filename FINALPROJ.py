
import graphics as g
import random

#henrietta radius is 70
#ground is 450

class Objects:
    def __init__(self,w,x,y,):
        self.w = w
        self.x = x
        self.y = y
        self.direction = int(-1)
        self.speed = float(0.5)
        self.draw()
        self.move()
    
    def draw(self):
        self.log = g.Circle(g.Point(self.x,485),35)
        self.cloud = g.Circle(g.Point(self.x,200),35)

        self.log.setFill('sienna4')
        self.cloud.setFill('snow')
        
        for obj in [self.log,self.cloud]:
            obj.draw(self.w)
    
    def move(self):
        dx = self.direction*5
        dy = 0
            
        for obj in [self.log,self.cloud]:
            obj.move(dx,dy)
            
        self.w.after(30, self.move)
    
    def hit(self,x,y):
        pass

def main():

    w = g.GraphWin("FINAL",1000,700)
    objects = Objects(w,450,450)
    w.getMouse()
        
    key = None
    while key != 'q':
        key = w.checkKey()
    w.close()

if __name__ == '__main__':
    main()