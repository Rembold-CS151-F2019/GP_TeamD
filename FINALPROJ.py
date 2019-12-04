
import graphics as g


class Objects:
    def __init__(self,w,x,y):
        self.w = w
        self.x = x
        self.y = y
        self.direction = int(-1)
        self.speed = float(0.5)
        self.draw()
        self.offscreen()


    def offscreen(self):
    
        if self.obj.getCenter().getX()+35 < 0:
            self.obj.undraw()
            return True

        dx = self.direction*5
        dy = 0
        self.obj.move(dx,dy)
        self.w.after(30, self.offscreen)

    def faster(self):
        pass

    def hit(self,H):
        if self.obj.getCenter() - H.body.getCenter() <= 105:
            return True
        else:
            return False

class Log(Objects):
    def draw(self):
            self.obj = g.Circle(g.Point(self.x,415),35)

            self.obj.setFill('sienna4')
            self.obj.draw(self.w)


class Cloud(Objects):
    def draw(self):
            
            self.obj = g.Circle(g.Point(self.x,330),35)
            self.obj.setFill('snow')          
            self.obj.draw(self.w)

#w = g.GraphWin("FINAL",1000,700)
#objects = Log(w,450,450)
#objects = Cloud(w,250,450)
#key = None
#while key != 'e':
#    key = w.checkKey()
#w.close()
