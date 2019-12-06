
import graphics as g

class Objects:
    def __init__(self,w,x,y):
        self.w = w
        self.x = x
        self.y = y
        self.direction = int(-1) #so the cloud or log moves to the left
        self.speed = float(0.5)
        self.draw()
        self.move()
        self.offscreen()


    def offscreen(self):
    #function used to undraw the cloud or the log when they leave the screen. Measure 
    # when the center crossed the 0 and then added on the radius.
        if self.obj.getCenter().getX()+35 < 0:
            self.obj.undraw() 
            return True
        return False

    def move(self):
        dx = self.direction*5 
        dy = 0
        self.obj.move(dx,dy)
        self.w.after(30, self.move)

    def hit(self,H):
        DX = (self.obj.getCenter().getX() - H.body.getCenter().getX())**2
        DY = (self.obj.getCenter().getY() - H.body.getCenter().getY())**2
        HYP = (DX+DY)**0.5
    #hit function determines whether henrietta gets hit by the log or the cloud. 
    # We determined it by using the pythagreon thm to find the distance between
    # henrietta and the cloud or log by using the center points.
        if HYP <= 35+H.getr():
            return True
        else: 
            return False

class Log(Objects):
    def draw(self):
            self.obj = g.Circle(g.Point(self.x,415),35)

            self.obj.setFill('sienna4')
            self.obj.draw(self.w)
#Drawing the log objects

class Cloud(Objects):
    def draw(self):
            
            self.obj = g.Circle(g.Point(self.x,180),35)
            self.obj.setFill('snow')          
            self.obj.draw(self.w)
#drawing the cloud objects

#w = g.GraphWin("FINAL",1000,700)
#objects = Log(w,700,450)
#objectss = Cloud(w,700,450)
#key = None
#while key != 'e':
#    key = w.checkKey()
#w.close()