from scipy.spatial import distance
from numpy import array

class Cell():
    
    def __init__(self, pos=(0,0), height=0):
        self.pos = pos
        self.height = height
        
    def __iter__(self):
        yield (self.pos)
        
    def is_valid_cell(self):
        if self.height != 4:
            return True
        else:
            return('Dead')
        
    def get_accessible_cells(self):
        """
        Determine ,for a fix cell, all the accessible cells around it 
        """
        accessible_dir = []
        for i in range(-1,2):
            for j in range(-1,2):
                if (i != 0 or j != 0):
                    if Cell(tuple(array(tuple(self.pos)+ array((i,j))))).is_valid_cell() == True:
                        accessible_dir.append(tuple(array(tuple(self.pos)+ array((i,j)))))
        return accessible_dir
    
class Position(Cell):
    def __init__(self, pos, height):
        self.pos = pos
        self.height = height
        
    def distance_to(self, pos2):
        return distance.chebyshev(self.pos,pos2)
    
class Units():
    def __init__(self, pos, player, index):
        self.player = player
        self.pos = pos
        self.index = index
               
