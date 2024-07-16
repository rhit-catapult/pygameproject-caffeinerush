import pygame
import sys
import random
import time
import subprocess
import sysconfig
import os

import Customer_Aron_is_silly
import my_character


def main():
    # turn on pygame
    pygame.init()
    screen_width = 1000 #defines the width
    screen_height = 600 #defines the height
    screen = pygame.display.set_mode((screen_width, screen_height))
    bg_color = ("white")

#hi
    # create a screen
    pygame.display.set_caption("Caffeine Rush")
    # TODO: Change the size of the screen as you see fit!
    screen = pygame.display.set_mode((screen_width, screen_height)) #sets the screen dimentions

    font = pygame.font.Font(None, 100)  # creates the font
    text_surface = font.render("Match Order To Customer", True, (250, 255, 20))  # creates text surface
    text_rect = text_surface.get_rect()  # get the rect of the play button
    text_rect.center = ( 500, 40)  # centers text




    clock = pygame.time.Clock()
    clock.tick(60)
    player = my_character.Character(screen, 10, 10)
    is_dragging = False
    customer = Customer_Aron_is_silly.Customer(screen, 250, 260)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                # for food in foods
                if player.get_rect().collidepoint(pos):
                    is_dragging = True

            if event.type == pygame.MOUSEBUTTONUP and is_dragging:
                is_dragging = False
                pos = event.pos
                if customer.get_rect().colliderect(player.get_rect()):
                    # remove customer here
                    print("RIP customer")



        pressed_keys = pygame.key.get_pressed()

        screen.fill((bg_color))
        screen.blit(text_surface, text_rect)  # "TEST"


        player_image = pygame.image.load("Apple-6.jpg")
        player_x, player_y = screen_width // 2, screen_height // 2

        if is_dragging:
            pos = pygame.mouse.get_pos()
            player.x = pos[0] - player.width / 2
            player.y = pos[1] - player.width / 2

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player.move(-10, 0)
        if keys[pygame.K_RIGHT]:
            player.move(10, 0)
        if keys[pygame.K_UP]:
            player_y -= 1
        if keys[pygame.K_DOWN]:
            player_y += 1
        customer.draw()
        player.draw()
        pygame.display.update()
main()