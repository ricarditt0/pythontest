import math

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def distance(self ,point):
        deltaX = self.x - point.x
        deltaY = self.y - point.y
        distance = math.sqrt(deltaX**2 + deltaY**2)
        return distance