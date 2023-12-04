import random
import pygame


class Horde(pygame.sprite.Sprite):
    def __init__(self, screen, score):
        super().__init__()
        self.image = pygame.image.load('assets/images/horde.png')
        self.image = pygame.transform.scale_by(self.image, 2)
        self.x_speed = -(random.random() * .05)
        self.y_speed = 0
        self.rect = self.image.get_rect()
        self.x = screen.get_width()
        self.y = random.randint(screen.get_height() - 50, screen.get_height() - self.image.get_height())
        self.rect.y = self.y
        self.screen = screen
        self.dead_timer = 0
        self.score = score  # SCORE IS A LIST WITH ONE ITEM!
        self.has_scored = 0

    def update(self):
        self.x_speed = self.x_speed
        self.x = self.x + self.x_speed
        self.rect.x = self.x
        if self.screen.get_width()/2 - 35 < self.rect.x < self.screen.get_width()/2 + 35:
            self.y_speed = -(random.random() * .05)
            self.y = self.y + self.y_speed
            self.rect.y = self.y
            self.x_speed = 0
            self.x = self.x + self.x_speed
            self.rect.x = self.x
        if self.screen.get_height()/2 > int(self.y):
            self.y_speed = 0
            self.y = self.y + self.y_speed
            self.rect.y = self.y
            self.x_speed = -(random.random() * .05)
            self.x = self.x + self.x_speed
            self.rect.x = self.x
        if not self.dead_timer or self.dead_timer <= 1000:
            pass
        else:
            self.kill()

    def ghost(self):
        self.image = pygame.image.load('assets/images/ghost.png')
        self.dead_timer = pygame.time.get_ticks()
        # update the score only if you haven't already added to the score

