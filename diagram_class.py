from scipy.spatial import distance

class Cell():
    
    def __init__(self, pos, height):
        self.pos = pos
        self.height = height
        
    def is_valid_cell(self):
        if self.height != 4:
            return True
    
class Position(Cell):
    def __init__(self, pos, height):
        self.pos = pos
        self.height = height
        
    def distance_to(self, pos2):
        return distance.chebyshev(self.pos,pos2)
    
class Units():
    def __init__(self, player, pos):
        self.player = player
        self.pos = pos 
        
    def get_accessible_cells(self):
        """
        Determine ,for an unit, all the accessible cells around it 
        """
        accessible_pos = []
        for i in range(-1,1):
            for j in range(-1,1):
                if i != 0 and j != 0:
                    if Cell(self.pos + (i,j)).is_valid_cell() == True:
                        accessible_pos.append(self.pos + (i,j))
        return accessible_pos
