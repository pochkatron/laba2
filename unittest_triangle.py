import unittest
from triangle import area, perimeter  

class TestTriangleFunctions(unittest.TestCase):

    def test_area(self):
       
        self.assertEqual(area(2, 3), 3)
        self.assertEqual(area(5, 4), 10)
        self.assertEqual(area(0, 4), 0)
        self.assertEqual(area(4, 0), 0)
        self.assertEqual(area(0, 0), 0)

    def test_perimeter(self):
        self.assertEqual(perimeter(2, 3, 4), 9)
        self.assertEqual(perimeter(5, 5, 5), 15)
        self.assertEqual(perimeter(0, 4, 4), 8)
        self.assertEqual(perimeter(4, 0, 4), 8)
        self.assertEqual(perimeter(4, 4, 0), 8)
        self.assertEqual(perimeter(0, 0, 0), 0)
