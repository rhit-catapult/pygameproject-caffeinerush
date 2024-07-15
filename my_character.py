import pygame
import sys


class Character:
    def __init__(self, screen: pygame.Surface, x, y):
        self.screen = screen
        self.x = x
        self.y = y
        self.draw_banna = False
        self.image = pygame.image.load('Apple-6.jpg')
        self.width = 80
        self.height = 80
        self.image = pygame.transform.scale(self.image, (self.width, self.height))

    def draw(self):
        if self.draw_banna:
            # draw bannana
            pass
        else:
            # draw apple
            pass

        self.screen.blit(self.image, (self.x, self.y))

    def move(self, deltax, deltay):
        self.x += deltax
        self.y += deltay


# This function is called when you run this file, and is used to test the Character class individually.
# When you create more files with different classes, copy the code below, then
# change it to properly test that class
def test_character():
    # TODO: change this function to test your class
    screen = pygame.display.set_mode((640, 480))
    character = Character(screen, 400, 400)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill("white")
        character.draw()
        pygame.display.update()


# Testing the classes
# click the green arrow to the left or run "Current File" in PyCharm to test this class
if __name__ == "__main__":
    test_character()