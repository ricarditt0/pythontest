import pygame
import Collision
from Circle import Circle

pygame.init()
screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()

numballs = 100
# balls = Circle.randBalls(numballs)
balls = []
hitbox = [(30,30),(30,690),(1250,690),(1250,30)]

# create a system cursor
system = pygame.cursors.Cursor(pygame.SYSTEM_CURSOR_HAND)
pygame.mouse.set_cursor(system)

run = True
while run:
    # Process player inputs.
    pressed = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
        if event.type == pygame.MOUSEBUTTONDOWN:
            match (event.button):
                case 1:
                    balls.append(Circle(center=pygame.mouse.get_pos(),radius=15,speed=(0,0),color="red"))
                case 2:
                    balls.clear()
                case 3:
                    direction = pygame.math.Vector2(pygame.mouse.get_pos())
                    if(balls):
                        if (direction - balls[-1].center):
                            balls[-1].speed = pygame.math.Vector2.normalize(direction - balls[-1].center)*10
                

    # Do logical updates here.
    for ball in balls:
        ball.move()
        Collision.wallCircle(ball)
        for b in balls:
            if (b != ball) and Collision.ballBall(ball,b):
                Collision.elasticCollision(ball,b)


    screen.fill("black")  # Fill the display with a solid color

    # Render the graphics here.
    pygame.draw.polygon(surface=screen,color="white",points=hitbox,width=3)

    for ball in balls:
        pygame.draw.circle(surface = screen, color=ball.color,center=(ball.center),radius=ball.radius, width=0)

    pygame.display.flip()  # Refresh on-screen display
    clock.tick(60)         # wait until next frame (at 60 FPS)