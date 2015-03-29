__author__ = 'TriD'


class Tile(object):
    def __init__(self, ground, item=None, trigger=None):
        self.ground = ground
        self.item = item
        self.trigger = trigger
        self.monster = None

    def draw(self, screen):
        pass