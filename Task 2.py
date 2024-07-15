import pygame
import sys
import random
import time
import subprocess
import sysconfig
import os


class Ball:
    def __init__(self, screen, x, y):
        self.x = random.randint(0, 1000)
        self.y = random.randint(0, 600)
        self.xspeed = random.randint(-5, 5)
        self.yspeed = random.randint(-5, 5)
        self.screen = screen
        self.radius = random.randint(1, 50)

        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        self.color = (r, g, b)

    def move(self):
        self.x = self.x +self.xspeed
        self.y = self.y + self.yspeed
        if self.x > 800 - self.radius or self.x < 0 + self.radius:
            self.xspeed *= -1
        if self.y > 800 - self.radius or self.y < 0 + self.radius:
            self.yspeed *= -1

    def draw(self):
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.radius)


#Clean the dishes (random bubble code)
def main():
    # turn on pygame
    pygame.init()
    screen_width = 1000 #defines the width
    screen_height = 600 #defines the height
    screen = pygame.display.set_mode((screen_width, screen_height))
    bg_color = (0, 0, 0)

    test_ball = Ball(screen, 100, 100)
    balls = []
    for i in range(0, 100):
        ball = Ball(screen, 'black', 150, 150, 150, 150, 150)
        balls.append(ball)

    pygame.display.set_caption("Caffeine Rush")
    # TODO: Change the size of the screen as you see fit!
    screen = pygame.display.set_mode((screen_width, screen_height))  # sets the screen dimentions

    font = pygame.font.Font(None, 100)  # creates the font
    text_surface = font.render("TEST 2", True, (255, 255, 255))  # creates text surface
    text_rect = text_surface.get_rect()  # get the rect of the play button
    text_rect.center = (screen_width // 2, screen_height // 2)  # centers text

    clock = pygame.time.Clock()
    clock.tick(60)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill((bg_color))
        screen.blit(text_surface, text_rect)  # "TEST"

        for ball in balls:
            ball.draw()
            ball.move()

        pygame.display.update()


main()