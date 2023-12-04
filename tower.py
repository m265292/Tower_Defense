import pygame


class Tower(pygame.sprite.Sprite):
    def __init__(self, screen, health):
        super().__init__()
        self.health = 280
        self.image = pygame.Surface((70, self.health))
        self.rect = self.image.get_rect()
        self.rect.midbottom = (screen.get_width() / 2, screen.get_height())
        self.health = health
        self.create()
        self.screen = screen

    def create(self):
        tower4 = pygame.image.load('assets/images/medievalTile_023.png')
        tower3 = pygame.image.load('assets/images/medievalTile_045.png')
        tower2 = pygame.image.load('assets/images/medievalTile_069.png')
        tower1 = pygame.image.load('assets/images/medievalTile_080.png')
        self.image.blit(tower1, (0, 3 * tower1.get_height()))
        self.image.blit(tower2, (0, 2 * tower1.get_height()))
        self.image.blit(tower3, (0, tower1.get_height()))
        self.image.blit(tower4, (0, 0))

    def damage(self):
        self.health -= 70
        self.rect.height = self.health


    def update(self):
        self.damage()

    def draw(self, screen):
        screen.blit(self.image, self.rect)
