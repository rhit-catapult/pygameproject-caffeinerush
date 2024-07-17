


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
            if counter > 30:
                font = pygame.font.Font("calibri-italic.ttf", 100)
                text_surface = font.render("!YOU WIN!", True, (25, 150, 20))  # creates text surface
                while True:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            sys.exit()
                    clock.tick(60)
                    screen.fill("light Green")
                    text_rect = text_surface.get_rect()  # get the rect of the play button
                    text_rect.center = (300, 40)  # centers text
                    screen.blit(text_surface, text_rect.center)
                    task_text2 = "NEXT!"
                    task_text_surface2 = font.render(task_text2, True, (0, 0, 0))
                    task_text_rect2 = task_text_surface2.get_rect(center=(500, 300))
                    screen.blit(task_text_surface2, task_text_rect2)
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if task_text_rect2.collidepoint(event.pos):
                            pygame.quit()
                            Task2.main()
                    pygame.display.update()
        clock.tick(60)
        # TODO 15: Make a Hero, named alyssa, with appropriate images, starting at position x=700 y=400.


        if True:  # task_screen = pygame.display.set_mode((1000, 600))
            screen.fill(pygame.Color('lightblue'))
            task_text = "Task completed!"
            screen.blit(image2, (0, 0))

        mix.draw()
        pygame.display.update()

if __name__ == "__main__":
    main()