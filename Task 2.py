import pygame
import sys
import math
import random


class Ball:
    def __init__(self, screen, color, x, y, radius, speed_x, speed_y):
        self.screen = screen
        colorr = random.randint(150, 170)
        colorg = random.randint(185, 200)
        colorb = random.randint(225, 250)
        self.color = (colorr, colorg, colorb)
        self.radius = random.randint(50, 55)
       # bubble_radius = self.radius
        self.x = random.randint(0 + self.radius, 1000 - self.radius)
        self.y = random.randint(0 + self.radius, 600 - self.radius)
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

def distance(point1, point2):
        point1_x = point1[0]
        point2_x = point2[0]
        point1_y = point1[1]
        point2_y = point2[1]

        # TODO 4: Return the actual distance between point 1 and point 2.
        #  Hint: you will need the math library for the sqrt function.
        #       distance = sqrt(   (delta x) ** 2 + (delta y) ** 2  )
        delta_x = point2_x - point1_x
        delta_y = point2_y - point1_y
        dist = math.sqrt(delta_x ** 2 + delta_y ** 2)
        return dist


def main():
    pygame.init()
    screen = pygame.display.set_mode((1000, 600))
    pygame.display.set_caption('Bouncing Ball')
    screen.fill(pygame.Color('gray'))
    clock = pygame.time.Clock()
    text_color = (0, 0, 0)
    screen_width = 1000
    screen_height = 600
    countdown_seconds = 6
    start_time = pygame.time.get_ticks()  # Get initial time in milliseconds
    timer_font = pygame.font.Font(None, 100)
    timer_text = ""

    balls = []
    for i in range(0,15):
        ball = Ball(screen, 'black', 150, 150, 150, 150, 150)
        balls.append(ball)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        elapsed_time = pygame.time.get_ticks() - start_time
        remaining_time = max(0, countdown_seconds * 1000 - elapsed_time)
        seconds = remaining_time // 1000

        seconds = seconds % 60
        timer_text = f"{seconds:7}"


        clock.tick(60)
        screen.fill(pygame.Color('lavender'))

        pos = pygame.mouse.get_pos()
        for ball in balls:
            ball.move()
            ball.draw()
            if pygame.mouse.get_pressed()[0] and distance((ball.x, ball.y), pos) < ball.radius:
                balls.remove(ball)





        timer_surface = timer_font.render(timer_text, True, text_color)
        timer_rect = timer_surface.get_rect(center=(5, 50))
        screen.blit(timer_surface, timer_rect)


        pygame.display.update()
        if remaining_time <= 0:
           # print("Countdown finished!")
            running = False


main()

