import random as rd

from unit import Unit

DIRECTIONS = ["N", "NE", "E", "SE", "S", "SW", "W", "NW"]


def get_valid_neighbours(grid, x, y):
    size = len(grid)
    for i in range(-1, 2):
        for j in range(-1, 2):
            if x + i >= 0 and x + i < size and y + j >= 0 and y + j < size and grid[y + j][x + i] >= 0 and (i or j):
                yield x + i, y + j


def direction_to_position(x, y, dir):
    if "N" in dir:
        y -= 1
    if "E" in dir:
        x += 1
    if "W" in dir:
        x -= 1
    if "S" in dir:
        y += 1
    return x, y


def position_to_direction(from_x, from_y, to_x, to_y):
    diff_x = to_x - from_x
    diff_y = to_y - from_y
    dir = ''
    if diff_y == 1:
        dir += 'S'
    elif diff_y == -1:
        dir += 'N'
    if diff_x == 1:
        dir += 'E'
    elif diff_x == -1:
        dir += 'W'
    return dir


def track_units(player, player_units, known_units, grid):
    """Not visible units are simply randomly placed on the map."""
    visible_position = []
    for unit in player_units:
        visible_position.append((unit.x, unit.y))
        visible_position += [(x, y) for x, y in get_valid_neighbours(grid, unit.x, unit.y)]
    valid_positions = [(x, y) for x in range(len(grid)) for y in range(len(grid)) if grid[y][x] >= 0]
    not_visible_positions = set(valid_positions) - set(visible_position)
    while len(known_units) < 2:
        known_units.append(Unit(*rd.choice(not_visible_positions), len(known_units), - player))
    return known_units
