import pygame

tower4 = pygame.image.load('assets/images/medievalTile_023.png')

tower3 = pygame.image.load('assets/images/medievalTile_045.png')

tower2 = pygame.image.load('assets/images/medievalTile_069.png')

tower1 = pygame.image.load('assets/images/medievalTile_080.png')

class Tower1(pygame.sprite.Sprite):
    def __init__(self,screen):
        super().__init__()
        self.image = tower1
        self.rect = self.image.get_rect()
        self.rect.x = screen.get_width() / 2
        self.rect.y = screen.get_height()- self.image.get_height()
        self.velocity = 0
    def update(self):
        self.rect.x += self.velocity
    def draw(self, screen):
        screen.blit(self.image, self.rect)
class Tower2(pygame.sprite.Sprite):
    def __init__(self,screen):
        super().__init__()
        self.image = tower2
        self.rect = self.image.get_rect()
        self.rect.x = screen.get_width() / 2
        self.rect.y = screen.get_height()-2*self.image.get_height()
        self.velocity = 0
    def update(self):
        self.rect.x += self.velocity
    def draw(self, screen):
        screen.blit(self.image, self.rect)

class Tower3(pygame.sprite.Sprite):
    def __init__(self,screen):
        super().__init__()
        self.image = tower3
        self.rect = self.image.get_rect()
        self.rect.x = screen.get_width() / 2
        self.rect.y = screen.get_height()-3*self.image.get_height()
        self.velocity = 0
    def update(self):
        self.rect.x += self.velocity
    def draw(self, screen):
        screen.blit(self.image, self.rect)

class Tower4(pygame.sprite.Sprite):
    def __init__(self,screen):
        super().__init__()
        self.image = tower4
        self.rect = self.image.get_rect()
        self.rect.x = screen.get_width() / 2
        self.rect.y = screen.get_height()-4*self.image.get_height()
        self.velocity = 0
    def update(self):
        self.rect.x += self.velocity
    def draw(self, screen):
        screen.blit(self.image, self.rect)