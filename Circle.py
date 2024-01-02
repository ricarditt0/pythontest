import random
import pygame
import math

class Circle():
    def __init__(self,center,radius,speed,color):
        self.radius = radius
        self.speed = pygame.math.Vector2(speed)
        self.color = color
        self.center = pygame.math.Vector2(center)
        self.mass = radius

    def __str__(self) -> str:
        return f"{self.speed}"
    
    def distance(self ,another) -> float:
        deltaX = self.center.x - another.center.x
        deltaY = self.center.y - another.center.y
        distance = math.sqrt(deltaX**2 + deltaY**2)
        return distance

    def move(self):
       self.center = self.center + self.speed
    
    def randBalls(num) -> list:
        colors = ["red","green","purple","pink","blue","orange","brown","gray","cyan"]
        listBoll = []
        for i in range(0,num):
            listBoll.append(Circle(center=(random.randint(80,1200),random.randint(80,640)),radius=15,speed=(random.uniform(-2,2),random.uniform(-2,2)),color=random.choice(colors)))
        return listBoll
