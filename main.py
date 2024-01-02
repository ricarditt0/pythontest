import pygame
import Collision
from Circle import Circle

pygame.init()
screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()

numballs = 100
balls = Circle.randBalls(numballs)
hitbox = [(30,30),(30,690),(1250,690),(1250,30)]


while True:
    # Process player inputs.
    pressed = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
        if event.type == pygame.KEYDOWN:
            pass


    # Do logical updates here.
    for ball in balls:
        ball.move()
        Collision.wallCircle(ball)
        for b in balls[1:]:
            if (b != ball) and Collision.ballBall(ball,b):
                Collision.elasticCollision(ball,b)


    screen.fill("black")  # Fill the display with a solid color

    # Render the graphics here.
    pygame.draw.polygon(surface=screen,color="white",points=hitbox,width=3)

    for ball in balls:
        pygame.draw.circle(surface = screen, color=ball.color,center=(ball.center),radius=ball.radius, width=0)

    pygame.display.flip()  # Refresh on-screen display
    clock.tick(60)         # wait until next frame (at 60 FPS)