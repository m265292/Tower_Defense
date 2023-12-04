from tower import *


class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.image.load('assets/images/knight.png')
        self.image = pygame.transform.scale_by(self.image, 2.5)
        self.pos = pos
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.pos

    def draw(self, screen):
        screen.blit(self.image, self.rect)
