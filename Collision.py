from Circle import Circle
    


def wallCircle(Circle):

    if (Circle.x - Circle.radius <= 30) or (Circle.x + Circle.radius >= 1250):
        Circle.moveX = Circle.moveX*-1
    if (Circle.y - Circle.radius <= 30) or (Circle.y + Circle.radius >= 690):
        Circle.moveY  = Circle.moveY*-1

def ballBall(ball0,ball1):
    if ball0.distance(ball1) <= ball0.radius + ball1.radius:
        ball0.moveX = ball0.moveX * -1
        ball0.moveY = ball0.moveY * -1
        ball1.moveX = ball1.moveX * -1
        ball1.moveY = ball1.moveY * -1
