import sys
import math
from copy import deepcopy


class Node:

    def __init__(self):
        self.board = [[Cell(Position(x, y)) for y in range(size)] for x in range(size)]
        self.my_units = [Unit(i, 0) for i in range(units_per_player)]
        self.other_units = [Unit(i, 1) for i in range(units_per_player)]
        self.played_action = None

    def set_cells_neighbours(self):
        for x in range(size):
            for y in range(size):
                self.board[x][y].set_neighbours(self.board)

    def update_board_row(self, index, row):
        for i in range(size):
            elem = row[i]
            if elem == '.' or elem == '4':
                self.board[index][i].state == DeadCell()
            else:
                self.board[index][i].state == ValidCell(int(elem))


class Unit:

    def __init__(self, index, player):
        self.index = index
        self.player = player
        self.position = None


class Position:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def equals(self, position):
        if self.x == position.x and self.y == position.y:
            return True
        else:
            return False


class Cell:

    def __init__(self, position):
        self.position = position
        self.neighbours = []
        self.state = None

    def set_neighbours(self, board):
        for i in range(self.position.x - 1, self.position.x + 1):
            for j in range(self.position.y - 1, self.position.y + 1):
                if 0 <= i < size and 0 <= j < size:
                    self.neighbours.append(board[i][j])


class ValidCell:

    def __init__(self, height):
        self.height = height


class DeadCell:
    pass


global size
global units_per_player
size = int(input())
units_per_player = int(input())
node = Node()

# game loop
while True:
    for row_index in range(size):
        board_row = input()
        node.update_board_row(row_index, board_row)
    for unit_index in range(units_per_player):
        # x, y = [int(j) for j in input().split()]
        x, y = int(input.split())
        node.my_units[unit_index].position = node.board[x, y].position
        # node.my_units[unit_index].update_position([unit_x, unit_y])
    for i in range(units_per_player):
        other_x, other_y = [int(j) for j in input().split()]
        node.other_units[i].update_position([other_x, other_y])

    legal_actions = int(input())
    max_score = 0
    best_action = []
    for i in range(legal_actions):
        # atype, index, dir_1, dir_2 = input().split()
        action = input().split()
        # if score(action) >= max_score:
        #     best_action = action
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)
    print("{} {} {} {}".format(*best_action))
