import unittest
from diagram_class import Cell, Position
import numpy as np


class MyTestCase(unittest.TestCase):
    def test_valid_cell(self):
        self.assertEqual(Cell((1,2),3).is_valid_cell(), True)
        self.assertEqual(Cell((3,2),4).is_valid_cell(), None)
        
    def test_distance(self):
        self.assertEqual(Position((2,2),3).distance_to((2,3)),1)
        self.assertEqual(Position((2,2),3).distance_to((2,4)),2)
        self.assertEqual(Position((2,2),3).distance_to((1,1)),1)
        

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)