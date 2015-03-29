import pygame

__author__ = 'TriD'


class PlayerCharacter(object):
    def __init__(self):
        self.x = 1
        self.y = 1
        self.attack = 10
        self.hp = 15
        self.image = pygame.image.load('res/images/character.png')

    def draw(self, screen):
        screen.blit(self.image, (self.x * 32, self.y * 32 - 16))