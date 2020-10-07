import random as rd

from action import MoveAction, PushAction
from node import Node
from state import State
from unit import Unit
from utils import *


class Agent(object):
    def __init__(self, player):
        self.player = player
        self.my_units = []
        self.adv_units = []
        self.map_size = 0
        self.units_per_player = 0
        self.grid = []
        self.turn = -1
        self.current_state = None
        self.nb_legal_actions = 0
        self.legal_actions = []
        self.best_action = None

    def track_units(self):
        """Not visible units are simply randomly placed on the map."""
        visible_position = []
        for unit in self.my_units:
            visible_position.append((unit.x, unit.y))
            visible_position += [(x, y) for x, y in get_valid_neighbours(self.grid, unit.x, unit.y)]
        valid_positions = [(x, y) for x in range(len(self.grid)) for y in range(len(self.grid)) if self.grid[y][x] >= 0]
        not_visible_positions = set(valid_positions) - set(visible_position)
        while len(self.adv_units) < 2:
            self.adv_units.append(Unit(*rd.choice(not_visible_positions), len(self.adv_units), - self.player))
        return self.adv_units

    def read_init(self, *args):
        self.map_size = int(input())
        self.units_per_player = int(input())

    def read_state(self, *args):
        self.turn += 1
        for i in range(self.map_size):
            row = [j for j in input()]
            self.grid.append(row[:])
        for i in range(self.units_per_player):
            x, y = [int(j) for j in input().split()]
            self.my_units.append(Unit(x, y, i, self.player))
        for i in range(self.units_per_player):
            x, y = [int(j) for j in input().split()]
            self.adv_units.append(Unit(x, y, i, -self.player))
        self.nb_legal_actions = int(input())
        for i in range(self.nb_legal_actions):
            atype, index, dir_1, dir_2 = input().split()
            if atype == "MOVE&BUILD":
                action = MoveAction(index, dir_1, dir_2)
            else:
                action = PushAction(index, dir_1, dir_2)
            self.legal_actions.append(action)
        self.adv_units = self.track_units()
        self.current_state = State(self.grid, self.my_units + self.adv_units, self.player, self.turn)

    def choose_best_action(self, depth):
        if self.current_state is None:
            self.read_state()

        root = Node(self.current_state)
        root.negamax_alpha_beta_pruning(depth, -1e17, 1e17)
        children = root.get_children()
        for i in range(len(children)):
            if children[i].value == -root.value:
                self.best_action = self.legal_actions[i]
                break
        return self.best_action

    def commit(self, depth):
        best_action = self.choose_best_action(depth)
        print(best_action)


class LocalAgent(Agent):
    def __init__(self, player):
        super().__init__(player)
        self.score = 0

    def read_init(self, map_size, units_per_player):
        self.map_size = map_size
        self.units_per_player = units_per_player

    def read_state(self, current_state):
        self.turn += 1
        self.current_state = current_state
        self.grid = self.current_state.grid[:][:]
        self.my_units = [u for u in self.current_state.units if u.player == self.player]
        self.adv_units = [u for u in self.current_state.units if u.player != self.player]
        self.legal_actions = self.current_state.get_actions()

    def commit(self, depth):
        if self.current_state.is_terminal():
            return
        best_action = self.choose_best_action(depth)
        return best_action
