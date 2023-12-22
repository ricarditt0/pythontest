from Point import Point
import random

class Circle(Point):
    def __init__(self,x,y,radius,moveX,moveY,color):
        self.radius = radius
        self.moveX = moveX
        self.moveY = moveY
        self.color = color
        Point.__init__(self,x,y)

    def move(self):
        self.x = self.x + self.moveX
        self.y = self.y + self.moveY

    def getCenter(self):
        return [self.x,self.y]
    
    def randBalls(num):
        colors = ["red","green","purple","pink","blue","orange","brown","gray","cyan"]
        listBoll = []
        for i in range(0,num):
            listBoll.append(Circle(x=random.randint(30,1250),y=random.randint(30,690),radius=12,moveX=random.uniform(-2,2),moveY=random.uniform(-2,2),color=random.choice(colors)))
        return listBoll
