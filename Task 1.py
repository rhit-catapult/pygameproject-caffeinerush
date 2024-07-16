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
    # player = my_character.Character(screen, 10, 10)
    is_dragging = False
    customer = Customer_Aron_is_silly.Customer(screen, 250, 260)
    customers = []
    customers.append(customer)
    foods = []
    # foods.append(my_character.Character(screen, 20, 30))
    # foods.append(my_character.Character(screen, 90, 400))
    dragging_food = None

    food_images = []
    food_images.append(pygame.image.load("ChocoStraw.jpg"))
    food_images.append(pygame.image.load("Coffee.jpg"))
    food_images.append(pygame.image.load("Crossaint.jpg"))
    food_images.append(pygame.image.load("Cupcake.jpg"))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                # for food in foods
                for food in foods:
                    if food.get_rect().collidepoint(pos):
                        is_dragging = True
                        dragging_food = food

            if event.type == pygame.MOUSEBUTTONUP and is_dragging:
                is_dragging = False
                for customer in customers:
                    if customer.get_rect().colliderect(dragging_food.get_rect()):
                        # remove customer here
                        customers.remove(customer)
                        if dragging_food in foods:
                            foods.remove(dragging_food)
                        print("RIP customer")



            pressed_keys = pygame.key.get_pressed()

        if len(customers) <= 5:
            customers.append(Customer_Aron_is_silly.Customer(screen, random.randint(0, 900), random.randint(0, 500)))
        if len(foods) <= 5:
            img = random.choice(food_images)
            foods.append(my_character.Character(screen, random.randint(0, 900), random.randint(0, 500), img))




        screen.fill((bg_color))
        screen.blit(text_surface, text_rect)  # "TEST"


        player_image = pygame.image.load("Coffee.jpg")
        player_x, player_y = screen_width // 2, screen_height // 2

        if is_dragging:
            pos = pygame.mouse.get_pos()
            dragging_food.x = pos[0] - dragging_food.width / 2
            dragging_food.y = pos[1] - dragging_food.width / 2


        # customer.draw()
        # player.draw()

        for customer in customers:
            customer.draw()

        for food in foods:
            food.draw()

        pygame.display.update()
main()