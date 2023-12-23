from Circle import Circle

def wallCircle(Circle):

    if (Circle.center.x - Circle.radius <= 30) or (Circle.center.x + Circle.radius >= 1250):
        Circle.speed.x = Circle.speed.x*-1
    if (Circle.center.y - Circle.radius <= 30) or (Circle.center.y + Circle.radius >= 690):
        Circle.speed.y  =  Circle.speed.y*-1

def ballBall(ball0,ball1):
    if ball0.distance(ball1) <= ball0.radius + ball1.radius:
        ball0.speed = ball0.speed * -1
        ball1.speed = ball1.speed * -1
