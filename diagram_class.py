class Cell():

    def __init__(self, x, y, height=0):
        self.pos = Position(x,y)
        self.height = height

    def __iter__(self):
        yield (self.pos)

    def is_valid_cell(self):
        if self.height != 4:
            return True
        else:
            return ('Dead')

    def get_accessible_cells(self):
        """
        Determine ,for a fix cell, all the accessible cells around it 
        """
        accessible_dir = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                if (i != 0 or j != 0):
                    cell = Cell(self.pos.x + i, self.pos.y + j)
                    if cell.is_valid_cell() == True:
                        accessible_dir.append(cell)
        return accessible_dir


class Position(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_to(self, other):
        return max(abs(self.x - other.x), abs(self.y - other.y))


class Units():
    def __init__(self, pos, player, index):
        self.player = player
        self.pos = pos
        self.index = index
