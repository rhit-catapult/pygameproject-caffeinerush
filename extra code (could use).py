class Menu:
    def __init(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, 100)  # creates the font
        self.font2 = pygame.font.Font('papyrus.ttf', 100)

    def draw(self):
        screen.fill((228, 190, 159))
        screen.blit(text_surface, text_rect) #"Play"
        screen.blit(text_surfaceTitle, text_rectTitle)
        pygame.draw.rect(screen, (0,0,0,), (400,250, 200, 90), 10)

    showMenu = True
    menu = Menu(screen)
    if showMenu:
        menu.draw()