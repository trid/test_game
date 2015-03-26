import pygame

__author__ = 'TriD'


class Video():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.drawing_objects = []
        self.game_state = 'running'
        self.font = pygame.font.SysFont('monospace', 48)
        self.label_win = self.font.render("You Win", 1, (255, 0, 0))
        self.label_lose = self.font.render("You Lose", 1, (255, 0, 0))


    def draw(self):
        self.screen.fill((0, 0, 0))
        for obj in self.drawing_objects:
            obj.draw(self.screen)
        if self.game_state == 'win':
            self.screen.blit(self.label_win, (0, 0))
        if self.game_state == 'lose':
            self.screen.blit(self.label_lose, (0, 0))
        pygame.display.flip()
