


#def main:
import pygame
import sys
import math
import random
import os
import time
import subprocess
import sysconfig
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

    def draw(self):
        """ Draws this sprite onto the screen. """
        # TODO 17: Draw (blit) this Hero, at this Hero's position, WITHOUT an umbrella:

        # TODO 21: Instead draw (blit) this Hero, at this Hero's position, as follows:
        #     If the current time is greater than this Hero's last_hit_time + 1,
        #       draw this Hero WITHOUT an umbrella,
        #       otherwise draw this Hero WITH an umbrella.
        if time.time() - self.last_hit_time < 1:
                self.screen.blit(self.Left, (self.x, self.y))
        else:
                self.screen.blit(self.Right, (self.x, self.y))

def main():
    pygame.init()
    screen = pygame.display.set_mode((1000, 600))
    pygame.display.set_caption('Winner Screen')
    screen.fill(pygame.Color('gray'))
    clock = pygame.time.Clock()

    image2 = pygame.image.load("Spacebarbackground.jpeg")
    image2 = pygame.transform.scale(image2, (1000, 600))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        clock.tick(60)
        mix = Mixer(screen, 418, 317, "Rightmixer.jpeg", "Leftmixer.jpeg")
        # TODO 15: Make a Hero, named alyssa, with appropriate images, starting at position x=700 y=400.


        if True:  # task_screen = pygame.display.set_mode((1000, 600))
            screen.fill(pygame.Color('lightblue'))
            task_text = "Task completed!"
            screen.blit(image2, (0, 0))

        mix.draw()
        pygame.display.update()

if __name__ == "__main__":
    main()