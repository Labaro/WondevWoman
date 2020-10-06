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
        self.score = 0
        self.has_been_evaluated = False

    def evaluate(self):
        if self.has_been_evaluated:
            return self.score
        else:
            if self.is_terminal():
                self.score -= 1000
            for unit in self.units:
                if unit.player == self.player:
                    self.score += self.grid[unit.y][unit.x] * 5
                else:
                    self.score -= self.grid[unit.y][unit.x] * 2
            self.has_been_evaluated = True
            return self.score

    def get_legal_actions(self):
        if self.legal_actions:
            return self.legal_actions
        for unit in self.units:
            others_positions = [(u.x, u.y) for u in self.units if u != unit]
            if unit.player == self.player:
                for move_x, move_y in unit.get_accessible_positions(self.grid):
                    for build_x, build_y in get_valid_neighbours(self.grid, move_x, move_y):
                        if (move_x, move_y) not in others_positions and (build_x, build_y) not in others_positions:
                            dir_1 = position_to_direction(unit.x, unit.y, move_x, move_y)
                            dir_2 = position_to_direction(move_x, move_y, build_x, build_y)
                            self.legal_actions.append(MoveAction(unit.index, dir_1, dir_2))
                for push_x, push_y in get_valid_neighbours(self.grid, unit.x, unit.y):
                    dir_1 = position_to_direction(unit.x, unit.y, push_x, push_y)
                    idx = DIRECTIONS.index(dir_1)
                    for i in range(-1, 2):
                        dir_2 = DIRECTIONS[(idx + i) % 8]
                        push_to_x, push_to_y = direction_to_position(push_x, push_y, dir_2)
                        if (push_x >= 0 and push_x < len(self.grid) and push_y >= 0 and push_y < len(self.grid) and
                                self.grid[push_to_y][push_to_x] - self.grid[push_y][push_x] <= 1):
                            self.legal_actions.append(PushAction(unit.index, dir_1, dir_2))
        return self.legal_actions

    def is_terminal(self):
        return bool(self.get_legal_actions())

    def simulate(self, action):
        """We suppose that every actions that can be simulate are already legal actions"""
        if isinstance(action, MoveAction):
            for unit in self.units:
                if unit.player == self.player and unit.index == action.index:
                    unit.x, unit.y = direction_to_position(unit.x, unit.y, action.dir_1)
                    build_x, build_y = direction_to_position(unit.x, unit.y, action.dir_2)
                    self.grid[build_y][build_x] += 1
                    if self.grid[build_y][build_x] == 4:
                        self.grid[build_y][build_x] = -1
                    break
        else:
            for unit in self.units:
                if unit.player == self.player and unit.index == action.index:
                    push_x, push_y = direction_to_position(unit.x, unit.y, action.dir_1)
                    for u in self.units:
                        if u.x == push_x and u.y == push_y:
                            u.x, u.y = direction_to_position(u.x, u.y, action.dir_2)
                            break
                    build_x, build_y = push_x, push_y
                    self.grid[build_y][build_x] += 1
                    if self.grid[build_y][build_x] == 4:
                        self.grid[build_y][build_x] = -1
                    break
        return State(self.grid[:][:], self.units, - self.player, self.turn + 1)
