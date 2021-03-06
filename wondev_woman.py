import sys
import math
from copy import deepcopy


# directions = ["N", "NE", "E", "SE", "S", "SW", "W", "NW"]


class Cell:

    def __init__(self, position):
        self.position = position
        self.neighbours = []
        self.state = ValidCell(0)

    def set_neighbours(self, board):
        for i in range(self.position[0] - 1, self.position[0] + 2):
            for j in range(self.position[1] - 1, self.position[1] + 2):
                if (i != self.position[0] or j != self.position[1]):
                    self.neighbours.append(board[i][j])
        #return self.neighbours

    def get_accessible_neighbours(self):
        if isinstance(self.state, DeadCell):
            return []
        else:
            accessible_neighbours = []
            for neigh_cell in self.neighbours:
                if isinstance(neigh_cell.state, ValidCell):
                    if (neigh_cell.state.height - self.state.height <= 1):
                        accessible_neighbours.append(neigh_cell)
            return accessible_neighbours


# State classes
class ValidCell:

    def __init__(self, height):
        self.height = height


class DeadCell:
    pass


class Position:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def convert_direction(self, direction):
        x_temp, y_temp = self.x, self.y
        if "N" in direction:
            x_temp -= 1
        if "E" in direction:
            y_temp += 1
        if "W" in direction:
            y_temp -= 1
        if "S" in direction:
            x_temp += 1
        return Position(x_temp, y_temp)

    def direction_to(self, position):
        diff_x = self.x - position.x
        diff_y = self.y - position.y
        dir = ''
        if diff_x == 1:
            dir += 'N'
        elif diff_x == -1:
            dir += 'S'
        if diff_y == 1:
            dir += 'W'
        elif diff_y == -1:
            dir += 'E'

    def distance_to(self, other):
        return max(abs(self.x - other[0]), abs(self.y - other[1]))


class Unit:

    def __init__(self, index, player):
        self.index = index
        self.player = player
        self.cell = None


class Game:

    def __init__(self):
        self.board = [[Cell(Position(x, y)) for y in range(size)] for x in range(size)]
        self.set_cells_neighbours()
        # !! Change player number according to starting player ? !!
        self.my_units = [Unit(i, 0) for i in range(units_per_player)]
        self.other_units = [Unit(i, 1) for i in range(units_per_player)]
        self.played_action = None

    def get_cell(self, position):
        return self.board[position.x][position.y]

    def set_cells_neighbours(self):
        for x in range(size):
            for y in range(size):
                self.board[x][y].set_neighbours(self.board)

    def update_board_row(self, row_index, row):
        for i in range(size):
            elem = row[i]
            if elem == '4' or elem == '.':
                current_cell = self.board[row_index][i]
                if isinstance(current_cell.state, ValidCell):
                    for neighbour in current_cell.neighbours:
                        neighbour.neighbours.remove(current_cell)
                    current_cell.state = DeadCell()
            else:
                self.board[row_index][i].state.height = int(elem)

    def get_actions(self, my_turn):
        actions = []
        if my_turn:
            units_player = self.my_units
            units_other_player = self.other_units
        else:
            units_player = self.other_units
            units_other_player = self.my_units
        for unit in units_player:
            # Check possible move and build
            for move_cell in unit.cell.get_accessible_neighbours():
                for build_cell in move_cell.neighbours:
                    dir_1 = unit.cell.position.direction_to(move_cell.position)
                    dir_2 = dir_1.direction_to(build_cell.position)
                    actions.append(['MOVE&BUILD', unit.index, dir_1, dir_2])
            # Check possible push and build
            for push_cell in units_player[i].cell.get_pushable_neighbours():
                for build_cell in push_cell.neighbours:
                    for adv_unit in units_other_player:
                        if push_cell.position == adv_unit.cell.position:
                            dir_1 = unit.cell.position.direction_to(push_cell.position)
                            dir_2 = unit.cell.position.direction_to(build_cell.position)
                            actions.append(['PUSH&BUILD', unit.index, dir_1, dir_2])

    def simulate(self, action):
        new_game = deepcopy(self)
        new_game.played_action = Action(*action)
        new_game.played_action.play_action()
        self.played_action.play_action()


class Action:
    def __init__(self, unit, name, dir_1, dir_2):
        self.name = name
        self.unit = unit
        self.dir_1 = dir_1
        self.dir_2 = dir_2
        self.pos_1 = unit.cell.position.convert_direction(dir_1)
        self.pos_2 = None


class MoveAndBuild(Action):
    def __init__(self, unit, name, dir_1, dir_2):
        super().__init__(unit, name, dir_1, dir_2)
        self.pos_2 = self.pos_1.convert_direction(dir_2)


class PushAndBuild(Action):
    def __init__(self, unit, name, dir_1, dir_2):
        super().__init__(unit, name, dir_1, dir_2)
        self.pos_2 = unit.cell.position.convert_direction(dir_2)


global size
global units_per_player
size = int(input())
units_per_player = int(input())
game = Game()
# node = Node()

# game loop
while True:
    for row_index in range(size):
        board_new_row = input()
        game.update_board_row(row_index, board_new_row)
    for unit_index in range(units_per_player):
        my_x, my_y = int(input.split())
        game.my_units[unit_index].cell = game.board[my_x, my_y]
    for unit_index in range(units_per_player):
        other_x, other_y = int(input().split())
        game.other_units[unit_index].cell = game.board[other_x][other_y]

    legal_actions = int(input())
    max_score = 0
    best_action = []
    for i in range(legal_actions):
        atype, index, dir_1, dir_2 = input().split()
        if atype == 'MOVE&BUILD':
            game.played_action = MoveAndBuild(atype, game.my_units[index], dir_1, dir_2)
        elif atype == 'PUSH&BUILD':
            game.played_action = PushAndBuild(atype, game.my_units[index], dir_1, dir_2)
        # if score(action) >= max_score:
        #     best_action = action
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)
    print("{} {} {} {}".format(*best_action))
