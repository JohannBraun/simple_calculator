# test_calculator.py
import unittest
from simple_calculator.calculator import subtract, add

class TestCalculator(unittest.TestCase):
    def test_subtract(self):
        """
         Test subtraction of two numbers. This should give the same result as subtracting two numbers but with different sign
        """
        self.assertEqual(subtract(5, 3), 2)

    def test_add(self):
        """
         Test adding two numbers to a number. This should give the same result as the previous call to __add__
        """
        self.assertEqual(add(2, 3), 5)

# Unittest. main. This is a convenience method for unittest. main.
if __name__ == '__main__':
    unittest.main()