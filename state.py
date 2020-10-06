from unit import Unit
from action import MoveAction, PushAction
from utils import *


class State(object):
    def __init__(self, grid, units, player, turn=0):
        self.grid = grid
        self.units = units  # list of the 4 units, invisible units should already have been tracked
        self.player = player
        self.turn = turn
        self.legal_actions = []

    def evaluate(self):
        pass

    def get_legal_actions(self):
        if self.legal_actions:
            return self.legal_actions
        occupied_positions = [(u.x, u.y) for u in self.units]
        for unit in self.units:
            if unit.player == self.player:
                for move_x, move_y in unit.get_accessible_positions(self.grid):
                    for build_x, build_y in get_valid_neighbours(self.grid, move_x, move_y):
                        if (move_x, move_y) not in occupied_positions and (build_x, build_y) not in occupied_positions:
                            dir_1 = position_to_direction(unit.x, unit.y, move_x, move_y)
                            dir_2 = position_to_direction(move_x, move_y, build_x, build_y)
                            self.legal_actions.append(MoveAction(unit.index, dir_1, dir_2))

                for push_x, push_y in get_valid_neighbours(self.grid, unit.x, unit.y):
                    dir_1 = position_to_direction(unit.x, unit.y, push_x, push_y)
                    idx = DIRECTIONS.index(dir_1)
                    for i in range(-1, 2):
                        dir_2 = DIRECTIONS[idx + i]
                        push_to_x, push_to_y = direction_to_position(push_x, push_y, dir_2)
                        if (push_x >= 0 and push_x < len(self.grid) and push_y >= 0 and push_y < len(self.grid) and
                                self.grid[push_to_y][push_to_x] - self.grid[push_y][push_x] <= 1):
                            self.legal_actions.append(PushAction(unit.index, dir_1, dir_2))
        return self.legal_actions

    def is_terminal(self):
        pass

    def simulate(self, action):
        """We suppose that every actions that can be simulate are already legal actions"""
