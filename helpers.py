import pygame
from random import randint, randrange


# this function will take 2 surface and center the 2nd surface on the first one
def center_surfaces(bg, fg):
    # get the bg width and height
    bg_width = bg.get_width()
    bg_height = bg.get_height()
    # get the front surface width and height
    fg_width = fg.get_width()
    fg_height = fg.get_height()
    # blit the text on the surface
    bg.blit(fg, (bg_width / 2 - fg_width / 2, bg_height / 2 - fg_height / 2))


def make_background(screen):
    WIDTH = screen.get_width()
    HEIGHT = screen.get_height()
    sky_tile = pygame.image.load('assets/images/sky_tile.png')
    grass_tile = pygame.image.load('assets/images/grass_tile.png')
    grass_top = pygame.image.load('assets/images/grass5.png')
    grass_top = pygame.transform.scale(grass_top, (10, 10))
    cloud_tile = pygame.image.load('assets/images/cloud6.png')
    tree_tile = pygame.image.load('assets/images/tree02.png')
    tree_tile = pygame.transform.scale(tree_tile, (60, 80))
    # get tile size info
    tile_width = sky_tile.get_width()
    tile_height = sky_tile.get_height()
    # make a background
    background = pygame.Surface((WIDTH, HEIGHT))
    # draw sky tiles
    for x in range(0, WIDTH, tile_width):
        for y in range(0, HEIGHT, tile_height):
            background.blit(sky_tile, (x, y))
        # draw grass tile
    for x in range(0, WIDTH, tile_width):
        background.blit(grass_tile, (x, HEIGHT - tile_height))
    for x in range(0, WIDTH, tile_width):
        background.blit(grass_top, (x, randrange(HEIGHT - 1.5 * tile_height, HEIGHT)))
    num_clouds = 4
    for c in range(num_clouds):
        background.blit(cloud_tile, (randint(0, WIDTH), randint(0, 50)))
    num_trees = 4
    for t in range(num_trees):
        background.blit(tree_tile, (randint(0, WIDTH), HEIGHT - 4 * tile_height))
    return background
