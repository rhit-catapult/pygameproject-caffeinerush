import pygame
import sys
import random
import time
#hello caffeine Rushers

def main():
    # turn on pygame
    pygame.init()

    # create a screen
    pygame.display.set_caption("Caffeine Rush")
    # TODO: Change the size of the screen as you see fit!
    screen = pygame.display.set_mode((1920, 1080))

    # let's set the framerate
    clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            # TODO: Add you events code

        # TODO: Fill the screen with whatever background color you like!
        screen.fill((255, 255, 255))

        # TODO: Add your project code

        # don't forget the update, otherwise nothing will show up!
        pygame.display.update()

main()
