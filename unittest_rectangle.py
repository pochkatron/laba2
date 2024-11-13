import unittest
from rectangle import area, perimeter  

class TestRectangleFunctions(unittest.TestCase):

    def test_area(self):
        self.assertEqual(area(2, 3), 6)
        self.assertEqual(area(5, 5), 25)
        self.assertEqual(area(0, 4), 0)
        self.assertEqual(area(4, 0), 0)
        self.assertEqual(area(0, 0), 0)

    def test_perimeter(self):
        self.assertEqual(perimeter(2, 3), 10)
        self.assertEqual(perimeter(5, 5), 20)
        self.assertEqual(perimeter(0, 4), 8)
        self.assertEqual(perimeter(4, 0), 8)
        self.assertEqual(perimeter(0, 0), 0)
