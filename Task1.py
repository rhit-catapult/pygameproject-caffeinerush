import pygame
import sys
import random
import time
import subprocess
import sysconfig
import os
import Task2


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
    screen = pygame.display.set_mode((screen_width, screen_height)) # sets the screen dimension

    font = pygame.font.Font("calibri-italic.ttf", 70)  # creates the font
    text_surface = font.render("Match Order To Customer", True, (25, 150, 20))  # creates text surface
    text_rect = text_surface.get_rect()  # get the rect of the play button
    text_rect.center = (500, 40)  # centers text
    # dimension




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
    #
    #ASFGAFDH
    food_images = []
    food_images.append(pygame.image.load("ChocoStrawNoBackground.png"))
    food_images.append(pygame.image.load("CoffeeNoBackground.png"))
    food_images.append(pygame.image.load("CrossaintNoBackground.png"))
    food_images.append(pygame.image.load("CupcakeNoBackground.png"))
    food_deleted = 0
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
                            food_deleted += 1
                        print("RIP customer")



            pressed_keys = pygame.key.get_pressed()

        if len(customers) <= 5:
            customers.append(Customer_Aron_is_silly.Customer(screen, random.randint(0, 900), random.randint(0, 500)))
        if len(foods) <= 5:
            img = random.choice(food_images)
            foods.append(my_character.Character(screen, random.randint(0, 900), random.randint(0, 500), img))

        #why is curbies dick out


        screen.fill((bg_color))
        screen.blit(text_surface, text_rect)  # "TEST"


        player_image = pygame.image.load("Coffee.jpg")
        player_x, player_y = screen_width // 2, screen_height // 2

        if is_dragging:
            pos = pygame.mouse.get_pos()
            dragging_food.x = pos[0] - dragging_food.width / 2
            dragging_food.y = pos[1] - dragging_food.width / 2

        if food_deleted > 5:
            font = pygame.font.Font("calibri-italic.ttf", 100)
            text_surface = font.render("!YOU WIN!", True, (25, 150, 20))  # creates text surface

            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()
                clock.tick(60)
                screen.fill("Green")
                text_rect = text_surface.get_rect()  # get the rect of the play button
                text_rect.center = (300, 40)  # centers text
                screen.blit(text_surface, text_rect.center)
                task_text2 = "NEXT!"
                task_text_surface2 = font.render(task_text2, True, (0, 0, 0))
                task_text_rect2 = task_text_surface2.get_rect(center=(500, 300))
                screen.blit(task_text_surface2, task_text_rect2)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if task_text_rect2.collidepoint(event.pos):
                        pygame.quit()
                        Task2.main()


                pygame.display.update()

        # customer.draw()
        # player.draw()

        for customer in customers:
            customer.draw()

        for food in foods:
            food.draw()

        pygame.display.update()

print("Hello")
if __name__ == "__main__":
    main()