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
        for i in range(self.position.x - 1, self.position.x + 2):
            for j in range(self.position.y - 1, self.position.y + 2):
                if 0 <= i < size and 0 <= j < size and (i != self.position.x and j != self.position.y):
                    self.neighbours.append(board[i][j])

    def get_accessible_neighbours(self):
        if isinstance(self.state, DeadCell):
            return []
        else:
            accessible_neighbours = []
            for neigh_cell in self.neighbours:
                if isinstance(neigh_cell.state, ValidCell):
                    if neigh_cell.state.height - self.state.height <= 1:
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
            y_temp -= 1
        if "E" in direction:
            x_temp += 1
        if "W" in direction:
            x_temp -= 1
        if "S" in direction:
            y_temp += 1
        return Position(x_temp, y_temp)


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


class Action:
    def __init__(self, unit, name, dir_1):
        self.name = name
        self.unit = unit
        self.dir_1 = dir_1
        self.dir_2 = dir_2
        self.pos_1 = unit.cell.position.convert_direction(dir_1)
        self.pos_2 = None


class Referee:

    game_version = 0
    got_pushed = 2
    did_push = 1
    no_push = 0
    final_height = 4
    generated_map_size = 6
    win_on_max_height = True
    can_push = False
    unit_per_player = 1
    fog_of_war = False
    view_distance = 1


    def compute_move(game,unit,dir1,dir2):

        ''' Compute the decision when move and build '''

        # target cell
        target_position = unit.position.convert_direction(dir1)
        target_height = game.get_cell(target_position).state.height

        # target cell is dead ?
        if isinstance(game.get_cell(target_position).state,DeadCell):
            print("Bad move"+" "+str(target.x)+" "+str(target.y),file = sys.stderr)
            return False

        # build cell
        place_target_position = target.convert_direction(dir2)
        place_target_height = game.get_cell(place_target_position).state.height

        # build cell is dead
        if isinstance(game.get_cell(place_target_position).state,DeadCell):
            print("Bad place"+" "+str(target.x)+" "+str(target.y),file = sys.stderr)
            return False

        # update
        unit.position = target_position
        game.get_cell(place_target_position).state.height += 1

        #if target_height == final_height - 1:
        #    player.score += 1



    def compute_push(game,unit,dir1,dir2) :

        ''' Compute the decision when moveandpush '''

        # target cell
        target_position = unit.position.convert_direction(dir1)

        # target cell is dead ?
        if isinstance(game.get_cell(target_position).state, DeadCell):
            print("Bad move" + " " + str(target.x) + " " + str(target.y), file=sys.stderr)
            return False

        # Finding the pushed unit
        for unit in game.other_units:
            if unit.position == target_position:
                unit_pushed = unit

        # push cell
        push_to_position = unit_pushed.position.convert_direction(dir2)
        to_height = game.get_cell(push_to_position).state.height
        from_height = game.get_cell(target_position).state.height

        # target cell is dead ?
        if isinstance(game.get_cell(push_to_position).state, DeadCell):
            print("Bad push" + " " + str(target.x) + " " + str(target.y), file=sys.stderr)
            return False

        # Update
        unit.position = target_position
        unit_pushed.position = push_to_position

        #if from_height == final_height - 1:
         #   player.score += 1

        #if to_height == final_height - 1:
        #    player_other.score += 1




class MoveAndBuild(Action):
    def __init__(self, unit, dir_1, dir_2):
        super().__init__(unit, dir_1, dir_2)
        self.pos_2 = self.pos_1.convert_direction(dir_2)


class PushAndBuild(Action):
    def __init__(self, unit, dir_1, dir_2):
        super().__init__(unit, dir_1, dir_2)
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
