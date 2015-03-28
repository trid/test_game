__author__ = 'TriD'


class World(object):
    def __init__(self, game_map):
        self.map = game_map

    def can_move(self, creature, position_x, position_y):
        if self.map.get_tile(position_x, position_y) == '1':
            return False
        x_dist = abs(creature.x - position_x)
        y_dist = abs(creature.y - position_y)
        if x_dist > 1 or y_dist > 1:
            return False
        if x_dist == 1 and y_dist == 1:
            return False
        return True

    def move(self, creature, position_x, position_y):
        if self.can_move(creature, position_x, position_y):
            creature.x = position_x
            creature.y = position_y
            return True
        return False