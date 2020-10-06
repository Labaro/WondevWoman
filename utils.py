def get_valid_neighbours(grid, x, y):
    size = len(grid)
    for i in range(-1, 2):
        for j in range(-1, 2):
            if x + i >= 0 & x + i < size & y + j >= 0 & y + j < size & grid[y + j][x + i] >= 0:
                yield x + i, y + j


def apply_direction(x, y, dir):
    if "N" in dir:
        y -= 1
    if "E" in dir:
        x -= 1
    if "W" in dir:
        x += 1
    if "S" in dir:
        y += 1
    return x, y