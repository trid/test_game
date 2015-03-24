import pygame

__author__ = 'TriD'


class GameMap(object):
    def __init__(self):
        self.map_data = []

        self.wall_sprite = pygame.image.load('res/images/wall.png')
        self.floor_sprite = pygame.image.load('res/images/floor.png')
        self.chest_sprite = pygame.image.load('res/images/chest.png')

    def draw(self, screen):
        for i in xrange(len(self.map_data)):
            for k in xrange(len(self.map_data[i])):
                if self.map_data[i][k] == '1':
                    screen.blit(self.wall_sprite, (k * 32, i * 32))
                elif self.map_data[i][k] == '2':
                    screen.blit(self.floor_sprite, (k * 32, i * 32))
                elif self.map_data[i][k] == '3':
                    screen.blit(self.chest_sprite, (k * 32, i * 32))
