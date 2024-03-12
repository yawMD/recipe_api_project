"""
Sample tests
"""

from django.test import SimpleTestCase
from app import calc

class CalcTests(SimpleTestCase):
    """Test the calc module"""

    def test_add_numbers(self):
        """Test adding numbers together"""
        a = 2 
        b = 3
        res = calc.add(a, b)
        self.assertEqual(res, 5)
    
    def test_subtract_numbers(self):
        """Test subtracting numbers together"""
        a = 10 
        b = 3
        res = calc.subtract(a, b)
        self.assertEqual(res, 7)

    def test_divide_numbers(self):
        # divides numbers
        res = calc.divide(6, 2)
        self.assertEqual(res, 3)