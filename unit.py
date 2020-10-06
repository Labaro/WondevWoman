from utils import *


class Unit(object):
    def __init__(self, x, y, player, index):
        self.x = x
        self.y = y
        self.player = player
        self.index = index

    def get_accessible_positions(self, grid):
        for x, y in get_valid_neighbours(grid, self.x, self.y):
            if grid[y][x] - grid[self.y][self.x] <= 1:
                yield x, y
