import pygame

__author__ = 'TriD'


class Monster(object):
    def __init__(self):
        self.x = 7
        self.y = 4
        self.image = pygame.image.load('res/images/monster.png')

    def draw(self, screen):
        screen.blit(self.image, (self.x * 32, self.y * 32))