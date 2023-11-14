import pygame
from helpers import *
from tower import *


# pygame setup
pygame.init()

# make a clock
clock = pygame.time.Clock()
# set the resolution of our game window
WIDTH = 1000
HEIGHT = 650
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Make my background once!
background = make_background(screen)

# declare a Font
game_font = pygame.font.SysFont('impact', 120)
score_font = pygame.font.SysFont('impact', 20)

# create a score variable (it is a list so we can pass with reference)
score = [0]


my_tower1 = Tower1(screen)
tower_group = pygame.sprite.Group()
tower_group.add(my_tower1)

my_tower2 = Tower2(screen)
tower_group = pygame.sprite.Group()
tower_group.add(my_tower2)

my_tower3 = Tower3(screen)
tower_group = pygame.sprite.Group()
tower_group.add(my_tower3)

my_tower4 = Tower4(screen)
tower_group = pygame.sprite.Group()
tower_group.add(my_tower4)




running = True
while running:
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # draw the background on the screen
        screen.blit(background, (0, 0))




    tower_group.update()





    tower_group.draw(screen)

    pygame.display.flip()














pygame.quit()