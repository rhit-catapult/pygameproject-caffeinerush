import pygame
import sys
import math
import random
import os
import MainMenu
import time
import Task3


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
    task_font = pygame.font.Font('papyrus.ttf', 50)
    image1 = pygame.image.load("biggersink.jpeg")
    image1 = pygame.transform.scale(image1, (1000, 300))

    balls = []
    for i in range(0,15):
        ball = Ball(screen, 'black', 150, 150, 150, 150, 150)
        balls.append(ball)
    in_game = True
    task_completed = False



    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        clock.tick(60)

        if not task_completed:
            if not balls:
                task_completed = True
                in_game = False



            elapsed_time = pygame.time.get_ticks() - start_time
            remaining_time = max(0, countdown_seconds * 1000 - elapsed_time)
            seconds = remaining_time // 1000

            seconds = seconds % 60
            timer_text = f"{seconds:7}"


            screen.fill(pygame.Color('lavender'))
            screen.blit(image1, (0, 300))
            pos = pygame.mouse.get_pos()
            for ball in balls:
                ball.move()
                ball.draw()
                if pygame.mouse.get_pressed()[0] and distance((ball.x, ball.y), pos) < ball.radius:
                    balls.remove(ball)

            timer_surface = timer_font.render(timer_text, True, text_color)
            timer_rect = timer_surface.get_rect(center=(5, 50))
            screen.blit(timer_surface, timer_rect)
            if remaining_time < 1:
                screen.fill(pygame.Color('red'))
                task_text = "Task failed!"
                task_text2 = "RETRY!"
                task_text_surface = task_font.render(task_text, True, (0, 0, 0))
                task_text_rect = task_text_surface.get_rect(center=(500, 200))
                task_text_surface2 = task_font.render(task_text2, True, (0,0,0))
                task_text_rect2 = task_text_surface2.get_rect(center=(500,300))
                screen.blit(task_text_surface2, task_text_rect2)
                screen.blit(task_text_surface, task_text_rect)
                task_rec = task_text_surface2.get_rect()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if task_text_rect2.collidepoint(event.pos):
                        pygame.quit()
                        MainMenu.main()




        else:
            # task_screen = pygame.display.set_mode((1000, 600))
            screen.fill(pygame.Color('lightblue'))
            task_text = "Task completed!"
            task_text3 = "NEXT!"
            task_text3_surface = task_font.render(task_text3, True, (0,0,0))
            task_text_rect3 = task_text3_surface.get_rect(center=(500,300))
            task_text_surface = task_font.render(task_text, True, (0, 0, 0))
            task_text_rect = task_text_surface.get_rect(center=(500, 200))
            screen.blit(task_text3_surface, task_text_rect3)
            screen.blit(task_text_surface, task_text_rect)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if task_text_rect3.collidepoint(event.pos):
                    pygame.quit()
                    Task3.main()



        pygame.display.update()

#Thanks winston you the real G.O.A.T
# we <3 winstin
if __name__ == "__main__":
    main()