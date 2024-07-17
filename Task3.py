


#def main:
import pygame
import sys
import math
import random
import os
import time
import subprocess
import sysconfig
import Task2
import MainMenu

class Mixer:
    def __init__(self, screen, x, y, leftimage, rightimage):
        """ Creates a Hero sprite (Mike) that does not move. If hit by rain he'll put up his umbrella. """
        # TODO 16: Initialize this Hero, as follows:
        #     - Store the screen.
        #     - Set the initial position of this Hero to x and y.
        #     - Create an image of this Hero WITH    an umbrella to the given with_umbrella_filename.
        #     - Create an image of this Hero WITHOUT an umbrella to the given without_umbrella_filename.
        #     - Set the "last hit time" to 0.
        #   Use instance variables:
        #      screen  x  y  image_umbrella   image_no_umbrella  last_hit_time.
        self.screen = screen
        self.x = x
        self.y = y
        self.Left = pygame.image.load(leftimage)
        self.Left = pygame.transform.scale(self.Left, (150,150))
        self.Right = pygame.image.load(rightimage)
        self.Right = pygame.transform.scale(self.Right, (150, 150))
        self.last_hit_time = 0
        self.show_left = False

    def draw(self):
        """ Draws this sprite onto the screen. """
        # TODO 17: Draw (blit) this Hero, at this Hero's position, WITHOUT an umbrella:

        # TODO 21: Instead draw (blit) this Hero, at this Hero's position, as follows:
        #     If the current time is greater than this Hero's last_hit_time + 1,
        #       draw this Hero WITHOUT an umbrella,
        #       otherwise draw this Hero WITH an umbrella.
        if self.show_left:
                self.screen.blit(self.Left, (self.x, self.y))
        else:
                self.screen.blit(self.Right, (self.x, self.y))

def main():
    pygame.init()
    screen = pygame.display.set_mode((1000, 600))
    pygame.display.set_caption('Winner Screen')
    screen.fill(pygame.Color('gray'))
    clock = pygame.time.Clock()

    counter = 0
    image2 = pygame.image.load("Spacebarbackground.jpeg")
    image2 = pygame.transform.scale(image2, (1000, 600))
    mix = Mixer(screen, 418, 317, "Rightmixer.jpeg", "Leftmixer.jpeg")
    font = pygame.font.Font("calibri-italic.ttf", 70)  # creates the font
    text_surface = font.render("Match Order To Customer", True, (25, 150, 20))  # creates text surface
    text_rect = text_surface.get_rect()  # get the rect of the play button
    text_rect.center = (500, 40)  # centers text
    text_color = (0, 0, 0)
    countdown_seconds = 6
    start_time = pygame.time.get_ticks()  # Get initial time in milliseconds
    timer_font = pygame.font.Font(None, 100)
    timer_text = ""
    task_font = pygame.font.Font('papyrus.ttf', 50)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                pressed_keys = pygame.key.get_pressed()
                if pressed_keys[pygame.K_SPACE]:
                   mix.show_left = not mix.show_left
                counter = counter + 1
                print("space_count =" + str(counter))
        if counter == 30:
            font = pygame.font.Font("calibri-italic.ttf", 100)
            text_surface = font.render("!YOU WIN!", True, (25, 150, 20))  # creates text surface
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()

                clock.tick(60)

                screen.fill(pygame.Color('lightblue'))
                task_text = "Task completed!"
                screen.blit(image2, (0, 0))
                screen.blit(text_surface, (50, 50))
                pygame.display.update()

        elapsed_time = pygame.time.get_ticks() - start_time
        remaining_time = max(0, countdown_seconds * 1000 - elapsed_time)
        seconds = remaining_time // 1000

        seconds = seconds % 60
        timer_text = f"{seconds:7}"

        screen.fill(pygame.Color('lightblue'))
        task_text = "Task completed!"
        screen.blit(image2, (0, 0))

        timer_surface = timer_font.render(timer_text, True, text_color)
        timer_rect = timer_surface.get_rect(center=(5, 50))
        screen.blit(timer_surface, timer_rect)
        if remaining_time < 1:
            screen.fill(pygame.Color('red'))
            task_text6 = "Task failed!"
            task_text7 = "RETRY!"
            task_text_surface6 = task_font.render(task_text6, True, (0, 0, 0))
            task_text_rect6 = task_text_surface6.get_rect(center=(500, 200))
            task_text_surface7 = task_font.render(task_text7, True, (0, 0, 0))
            task_text_rect7 = task_text_surface7.get_rect(center=(500, 300))
            screen.blit(task_text_surface7, task_text_rect7)
            screen.blit(task_text_surface6, task_text_rect6)
            task_rec = task_text_surface7.get_rect()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if task_text_rect7.collidepoint(event.pos):
                    pygame.quit()
                    MainMenu.main()

        # pygame.display.update()



        # TODO 15: Make a Hero, named alyssa, with appropriate images, starting at position x=700 y=400.

        mix.draw()
        pygame.display.update()

if __name__ == "__main__":
    main()