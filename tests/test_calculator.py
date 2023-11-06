# test_calculator.py
import unittest
from simple_calculator.calculator import subtract, add

class TestCalculator(unittest.TestCase):
    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)

    def test_add(self):
        self.assertEqual(add(2, 3), 5)

if __name__ == '__main__':
    unittest.main()