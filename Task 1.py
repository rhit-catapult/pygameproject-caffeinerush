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

    font = pygame.font.Font(None, 100)  # creates the font
    text_surface = font.render("TEST", True, (255, 255, 255))  # creates text surface
    text_rect = text_surface.get_rect()  # get the rect of the play button
    text_rect.center = (screen_width // 2, screen_height // 2)  # centers text
    Image1 = pygame.image.load ('Apple-6.jpg')
    Image1 = pygame.transform.scale(Image1, (80, 80))
    clock = pygame.time.Clock()
    clock.tick(60)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill((bg_color))
        screen.blit(text_surface, text_rect)  # "TEST"
        screen.blit(Image1, (0, 0))
        pygame.display.update()
main()