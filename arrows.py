from math import cos, sin, atan2, sqrt

import pygame
import pygame.mouse


class Arrow(pygame.sprite.Sprite):
    def __init__(self, screen, horde_group):
        super().__init__()
        self.image = pygame.image.load('assets/images/spear.png')
        self.image = pygame.transform.flip(self.image, 1, 1)
        # self.x_speed = random.random() * 5
        # self.y_speed = random.random() * 3
        self.speed = 2.5
        # arrow just has an angle of travel, theta
        self.rect = self.image.get_rect()
        # change these values
        self.x = screen.get_width() / 2
        self.y = screen.get_height() / 2
        self.rect.y = self.y
        self.screen = screen
        self.dead_timer = 0
        self.horde_group = horde_group
        self.collision_radius = 30

    def update(self):
        m1, m2, m3 = pygame.mouse.get_pressed()

        # only update theta IF button pressed
        if m1:
            # get the position of them mouse!
            mouse_x, mouse_y = pygame.mouse.get_pos()
            # get the delta x, delt y
            delta_x = mouse_x - self.x
            delta_y = mouse_y - self.y
            # change the angle (theta) of the arrow!
            self.theta = atan2(delta_y, delta_x)
            self.gravity = 0.3
        new_theta = self.theta
        # move the arrow with its speed
        self.y_vel = self.speed * sin(new_theta)
        self.y_acc = self.y_vel + self.gravity
        self.y_vel += self.y_acc
        self.x = self.x + self.speed * cos(new_theta)
        self.y += self.y_vel

            # update the rectangle
        self.rect.x = self.x
        self.rect.y = self.y
        if self.x < 0 or self.x > self.screen.get_width() or self.y < 0 or self.y > self.screen.get_height():
            self.kill()

    def get_distance(self, coord1, coord2):
        x1, y1 = coord1
        x2, y2 = coord2
        return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    def get_sprite_distance(self, sprite1, sprite2):
        coord1 = sprite1.rect.center
        coord2 = sprite2.rect.center
        return self.get_distance(coord1, coord2) < self.collision_radius

    def check_hit(self):
        # check for collisions with the horde group use sprite collide
        hit_list = pygame.sprite.spritecollide(self, self.horde_group, 0, collided=self.get_sprite_distance)
        # if we find a collision, call horde.group()
        for h in hit_list:
            h.ghost()
