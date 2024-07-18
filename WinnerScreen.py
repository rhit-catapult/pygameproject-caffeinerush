import pygame
import sys
import math
import random
import os
import MainMenu

def main():
    pygame.init()
    screen = pygame.display.set_mode((1000, 600))
    pygame.display.set_caption('Winner Screen')
    screen.fill(pygame.Color('gray'))
    clock = pygame.time.Clock()

    image1 = pygame.image.load("winnerscreen.jpeg")
    image1 = pygame.transform.scale(image1, (1000, 600))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            font2 = pygame.font.Font("calibri-italic.ttf", 80)
            text_surface2 = font2.render("Back to menu", True, (0, 0, 0))
            text_rect2 = text_surface2.get_rect(center=(500, 400))
            screen.blit(text_surface2, text_rect2)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if text_rect2.collidepoint(event.pos):
                    pygame.quit()
                    MainMenu.main()

        clock.tick(60)

        if True:  # task_screen = pygame.display.set_mode((1000, 600))
            screen.fill(pygame.Color('lightblue'))
            task_text = "Task completed!"
            screen.blit(image1, (0, 0))

       
        pygame.display.update()

if __name__ == "__main__":
    main()