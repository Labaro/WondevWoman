import unittest
from diagram_class import Cell, Position, Units



class MyTestCase(unittest.TestCase):
    def test_valid_cell(self):
        self.assertEqual(Cell((1,2),3).is_valid_cell(), True)
        self.assertEqual(Cell((3,2),4).is_valid_cell(), None)
        
    def test_distance(self):
        self.assertEqual(Position((2,2),3).distance_to((2,3)),1)
        self.assertEqual(Position((2,2),3).distance_to((2,4)),2)
        self.assertEqual(Position((2,2),3).distance_to((1,1)),1)
        
    def test_accessible_cells(self):
        cell_center = Cell((1,1),3)
        cell1 = Cell((0,0), 2)
        cell2 = Cell((0,1), 3)
        cell3 = Cell((0,2), 4)
        cell4 = Cell((1,0),4)
        cell5 = Cell((1,2),1)
        cell6 = Cell((2,0),4)
        cell7 = Cell((2,1),0)
        cell8 = Cell((2,2),4)
        self.assertEqual(cell_center.get_accessible_cells(),[(0, 0), (0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1), (2, 2)])
        

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)