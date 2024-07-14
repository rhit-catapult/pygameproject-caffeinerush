import pygame
import sys
import random
import time
import subprocess
import sysconfig
import os

def main():
    # turn on pygame
    pygame.init()
    screen_width = 1000 #defines the width
    screen_height = 600 #defines the height
    screen = pygame.display.set_mode((screen_width, screen_height))
    bg_color = (0, 0, 0)
#hi
    # create a screen
    pygame.display.set_caption("Caffeine Rush")
    # TODO: Change the size of the screen as you see fit!
    screen = pygame.display.set_mode((screen_width, screen_height)) #sets the screen dimentions

    clock = pygame.time.Clock()
    clock.tick(60)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill((bg_color))
        pygame.display.update()
main()