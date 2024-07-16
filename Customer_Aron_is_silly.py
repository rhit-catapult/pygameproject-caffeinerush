import pygame
import sys
import random
import time
import subprocess
import os
import sysconfig

class Customer:
    def __init__(self, screen: pygame.Surface, x, y):
        self.screen = screen
        self.x = x
        self.y = y
        self.draw_banna = False
        self.image = pygame.image.load('GRIMACE.jpg')
        self.width = 100
        self.height = 100
        self.image = pygame.transform.scale(self.image, (self.width, self.height))

    def draw(self):


        self.screen.blit(self.image, (self.x, self.y))