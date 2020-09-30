import numpy as np 

class Cell():
    
    def __init__(self, pos, height):
        self.pos = pos
        self.height = height
        
    def is_valid_cell(self):
        if self.height != 4:
            return True

class Position(Cell):
    def __init__(self, x, y, height):
        self.x = pos[0]
        self.y = pos[1]
        self.height = height
        
    def distance_to(self, x_2, y_2):
        return np.sqrt((self.x - x_2)^2 + (self.y - y_2)^2) 
    
class Units():
    def __init__(self, player, pos):
        self.player = player
        self.pos = pos 
        
    def get_accessible_cells(self):
        for i in range(-1,1):
            for j in range(-1,1):
                if i != 0 and j != 0:
                    if Cell(pos + (i,j)).is_valid_cell() == True:
                        return ('This is an accessible cell position' , pos + (i,j))
                        #maybe put it in an array? I'm asking myself how to store the information 