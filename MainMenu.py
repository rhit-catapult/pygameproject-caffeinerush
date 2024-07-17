import pygame
import sys
import random
import time
import subprocess
import os
import sysconfig

import Task3


def main():
    # turn on pygame
    pygame.init()
    screen_width = 1000 #defines the width
    screen_height = 600 #defines the height
    image1 = pygame.image.load("CaffeineCafe.jpeg")
    image1 = pygame.transform.scale(image1, (1000, 700))
    # create a screen
    pygame.display.set_caption("Caffeine Rush")
    # TODO: Change the size of the screen as you see fit!
    screen = pygame.display.set_mode((screen_width, screen_height)) #sets the screen dimentions
    font = pygame.sysfont.Font('calibri-bold.ttf', 50) #creates the font
    font2 = pygame.font.Font('papyrus.ttf', 100)
    text_surfont = pygame.font.Font(None, 100) #creates the font
    font2 = pygame.font.Font('papyrus.ttf', 100)
    text_surface = font.render("PLAY", True, (250, 209, 205)) #creates text surface
    text_surfaceTitle = font2.render("Caffeine Rush", True, (255,255,255))
    text_rect = text_surface.get_rect()  # get the rect of the play button
    text_rectTitle = text_surfaceTitle.get_rect()
    text_rect.center = (625, 456) #centers text/
    text_rectTitle = (screen_width - 840, screen_height - 500)
    #


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
                    running = False
                    pygame.quit()

                    # Open Task1.py using subprocess
                    # python_executable = sys.executable
                    # subprocess.Popen([python_executable ,"Task1.py"]) This is another way to open another program
                    # But it will not close the other program
                    Task3.main()
                    # os.execl(sys.executable, "testfile.py")
                    # os.execlp('python', 'python', "testfile.py", *sys.argv)

            # TODO: Add you events code

        # TODO: Fill the screen with whatever background color you like!
        screen.fill((228, 190, 159))
        screen.blit(image1, (0, -100))
        screen.blit(text_surface, text_rect)#"Play"


        # TODO: Add your project code

        # don't forget the update, otherwise nothing will show up!
        pygame.display.update()


print(pygame.font.get_fonts())
if __name__ == "__main__":
    main()

