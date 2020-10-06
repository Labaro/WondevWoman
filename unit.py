from utils import *


class Unit(object):
    def __init__(self, x, y, player):
        self.x = x
        self.y = y
        self.player = player

    def get_accessible_positions(self, grid):
        for x, y in get_valid_neighbours(grid, self.x, self.y):
            if grid[y][x] - grid[self.y][self.x] <= 1:
                yield x, y
