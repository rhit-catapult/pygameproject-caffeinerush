import pygame
import sys
import random


# You will implement this module ENTIRELY ON YOUR OWN!

# TODO: Create a Ball class.
# TODO: Possible member variables: screen, color, x, y, radius, speed_x, speed_y
# TODO: Methods: __init__, draw, move
class Ball:
    def __init__(self, screen, color, x, y, radius, speed_x, speed_y):
        self.screen = screen
        colorr = random.randint(100, 200)
        colorg = random.randint(150, 200)
        colorb = random.randint(200, 250)
        self.color = (colorr, colorg, colorb)
        self.x = x
        self.y = y
        self.radius = random.randint(7, 40)
        self.speed_x = random.randint(1, 7)
        self.speed_y = random.randint(-1, 5)

    def move(self):
        self.y = self.y + self.speed_y
        self.x = self.x + self.speed_x
        if self.x - self.radius < 0 or self.x + self.radius > self.screen.get_width():
            self.speed_x = -self.speed_x
        if self.y - self.radius < 0 or self.y + self.radius > self.screen.get_height():
            self.speed_y = -self.speed_y

    def draw(self):
        pygame.draw.circle(self.screen, self.color, (self.x + self.speed_x, self.y + self.speed_y), self.radius)

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 800))
    pygame.display.set_caption('Bouncing Ball')
    screen.fill(pygame.Color('gray'))
    clock = pygame.time.Clock()

    balls = []
    for i in range(0,10000):
        ball = Ball(screen, 'black', 150, 150, 150, 150, 150)
        balls.append(ball)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        clock.tick(60)
        screen.fill(pygame.Color('lavender'))

        for ball in balls:
            ball.move()
            ball.draw()

        pygame.display.update()


main()

