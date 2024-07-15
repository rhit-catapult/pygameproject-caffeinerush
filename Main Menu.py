import pygame
import sys
import random
import time
import subprocess
import os
import sysconfig


#hello caffeine Rushers



# hi
def main():
    # turn on pygame
    pygame.init()
    screen_width = 1000 #defines the width
    screen_height = 600 #defines the height
#hi
    # create a screen
    pygame.display.set_caption("Caffeine Rush")
    # TODO: Change the size of the screen as you see fit!
    screen = pygame.display.set_mode((screen_width, screen_height)) #sets the screen dimentions
    font = pygame.font.Font(None, 100) #creates the font
    font2 = pygame.font.SysFont('papyrus', 100)
    text_surface = font.render("PLAY", True, (0, 0, 0)) #creates text surface
    text_surfaceTitle = font2.render("Caffeine Rush", True, (255,255,255))
    text_rect = text_surface.get_rect() #get the rect of the play button
    text_rectTitle = text_surfaceTitle.get_rect()
    text_rect.center = (screen_width - 502, screen_height //2) #centers text
    text_rectTitle = (screen_width - 840, screen_height - 500)


    # let's set the framerate
    clock = pygame.time.Clock()
    clock.tick(60)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Check if the mouse click is on the button
                if text_rect.collidepoint(event.pos):
                    pygame.quit()
                    running = False

                    # Open Task1.py using subprocess
                    #python_executable = sys.executable
                    #subprocess.Popen([python_executable ,"Task 1.py"]) This is another way to open another program
                    #But it will not close the other program
                    os.execl(sys.executable, sys.executable, "Task 1.py")






            # TODO: Add you events code

        # TODO: Fill the screen with whatever background color you like!
        screen.fill((228, 190, 159))
        screen.blit(text_surface, text_rect) #"Play"
        screen.blit(text_surfaceTitle, text_rectTitle)
        pygame.draw.rect(screen, (0,0,0,), (400,250, 200, 90), 10)

        # TODO: Add your project code

        # don't forget the update, otherwise nothing will show up!
        pygame.display.update()


main()
