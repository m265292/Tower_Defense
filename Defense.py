from arrows import Arrow
from helpers import *
from horde import *
from player import *
from tower import *

# pygame setup
pygame.init()

# make a clock
clock = pygame.time.Clock()
# set the resolution of our game window
WIDTH = 1200
HEIGHT = 650
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Make my background once!
background = make_background(screen)

# declare a Font
game_font = pygame.font.SysFont('impact', 120)
score_font = pygame.font.SysFont('impact', 20)
game_over_font = pygame.font.SysFont('impact', 120)
# create a score variable (it is a list, so we can pass with reference)
score = [0]
my_tower = Tower(screen, health=280)
tower_group = pygame.sprite.Group()
tower_group.add(my_tower)

my_player = Player(my_tower.rect.midtop)
player_group = pygame.sprite.Group()
player_group.add(my_player)

arrow_group = pygame.sprite.Group()
horde_group = pygame.sprite.Group()

num_horde = 10
[horde_group.add(Horde(screen, score)) for n in range(num_horde)]
horde_rect = Horde(screen, score).rect
running = True
while running:
    game_over = False
    if not game_over:
        if int(pygame.time.get_ticks() / 1000) % 10 == 0 and len(horde_group) < 8:
            [horde_group.add(Horde(screen, score)) for n in range(1)]
        if int(pygame.time.get_ticks() / 1000) % 50 == 0 and len(horde_group) < 15:
            [horde_group.add(Horde(screen, score)) for n in range(2)]
        if int(pygame.time.get_ticks() / 1000) % 100 == 0 and len(horde_group) < 20:
            [horde_group.add(Horde(screen, score)) for n in range(5)]
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if len(arrow_group) < 3:
                    arrow_group.add(Arrow(screen, horde_group))

            hit = pygame.sprite.groupcollide(arrow_group, horde_group, True, True)
            if hit:
                score[0] += 1
            if pygame.sprite.groupcollide(horde_group, tower_group, True, False):
                my_tower.damage()
            for h in horde_group:
                if h.rect.x < screen.get_width() / 2:
                    game_over = True
            # draw the background on the screen
        screen.blit(background, (0, 0))

        tower_group.update()
        arrow_group.update()
        horde_group.update()

        if pygame.time.get_ticks() < 3000:
            # draw text
            font_surface = game_font.render('DEFEND', 1, (199, 23, 4))
            screen.blit(font_surface, (screen.get_width() / 2 - 150, 40))
            # draw the score to the screen
        score_surface = score_font.render(f"Score: {score[0]}", 1, (199, 23, 4))
        screen.blit(score_surface, (10, 10))
        clock_surface = score_font.render(f"Time Elapsed: {int(pygame.time.get_ticks() / 1000)}", 1, (199, 23, 4))
        screen.blit(clock_surface, (10, 40))
        game_over_surface = game_over_font.render(f'Game Over', 1, (199, 23, 4))

        tower_group.draw(screen)
        player_group.draw(screen)
        arrow_group.draw(screen)
        horde_group.draw(screen)

        pygame.display.flip()

    else:
        screen.fill((0, 0, 0))
        screen.blit(game_over_surface, (screen.get_width() // 2 - 250, screen.get_height() // 2 - 50))
        screen.blit(score_surface, (screen.get_width() // 2 - 200, screen.get_height() // 2 + 150))
        screen.blit(clock_surface, (screen.get_width() // 2 - 200, screen.get_height() // 2 + 250))

        # Allow the player to restart the game by pressing 'R'
        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            game_over = False
            score = 0
    pygame.display.flip()

pygame.quit()
