<<<<<<< HEAD
import unittest
from square import area, perimeter  

class TestSquareFunctions(unittest.TestCase):

    def test_area(self):
        self.assertEqual(area(2), 4)
        self.assertEqual(area(5), 25)
        self.assertEqual(area(0), 0)

    def test_perimeter(self):
        self.assertEqual(perimeter(2), 8)
        self.assertEqual(perimeter(5), 20)
        self.assertEqual(perimeter(0), 0)
=======
import unittest
from square import area, perimeter  

class TestSquareFunctions(unittest.TestCase):

    def test_area(self):
        self.assertEqual(area(2), 4)
        self.assertEqual(area(5), 25)
        self.assertEqual(area(0), 0)

    def test_perimeter(self):
        self.assertEqual(perimeter(2), 8)
        self.assertEqual(perimeter(5), 20)
        self.assertEqual(perimeter(0), 0)
>>>>>>> 72710a0ae29b6dd9ca7b036fe4ff547203360184
