import pygame
import sys
import math
import random
import os

def main():
    pygame.init()
    screen = pygame.display.set_mode((1000, 600))
    pygame.display.set_caption('Winner Screen')
    screen.fill(pygame.Color('gray'))
    clock = pygame.time.Clock()
    font = pygame.font.Font("calibri-italic.ttf", 70)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        clock.tick(60)

        if True:  # task_screen = pygame.display.set_mode((1000, 600))
            screen.fill(pygame.Color('lightblue'))
            task_text = "Task completed!"

            task_text_surface = font.render(task_text, True, (0, 0, 0))
            task_text_rect = task_text_surface.get_rect(center=(500, 300))
            screen.blit(task_text_surface, task_text_rect)
       
        pygame.display.update()
main()