from Circle import Circle
import pygame

def wallCircle(Circle):

    if (Circle.center.x - Circle.radius <= 30) or (Circle.center.x + Circle.radius >= 1250):
        Circle.speed.x = Circle.speed.x*-1
    if (Circle.center.y - Circle.radius <= 30) or (Circle.center.y + Circle.radius >= 690):
        Circle.speed.y  =  Circle.speed.y*-1

def ballBall(ball0,ball1)->bool:
    if ball0.distance(ball1) <= ball0.radius + ball1.radius:
        return True
    else:
        return False
        # ball0.speed = ball0.speed * -1
        # ball1.speed = ball1.speed * -1

def elasticCollision(ball0,ball1):
    print((ball0.center - ball1.center))
    velocity0 = (
        ball0.speed - ((2*ball1.mass)/(ball0.mass + ball1.mass))*
        (pygame.math.Vector2.dot((ball0.speed - ball1.speed),(ball0.center - ball1.center))/
            pygame.math.Vector2.magnitude_squared(ball0.center - ball1.center)) * (ball0.center - ball1.center)
    )
    velocity1 = (
        ball1.speed - ((2*ball0.mass)/(ball0.mass + ball1.mass))*
        (pygame.math.Vector2.dot((ball1.speed - ball0.speed),(ball1.center - ball0.center))/
            pygame.math.Vector2.magnitude_squared(ball1.center - ball0.center)) * (ball1.center - ball0.center)
    )
    ball0.speed = velocity0
    ball1.speed = velocity1