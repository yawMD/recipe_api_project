from django.test import SimpleTestCase
from app import calc


class CalcTests(SimpleTestCase):
    """Test the calc module"""

    def test_add_numbers(self):
        """Test adding numbers together"""
        res = calc.add(2, 3)
        self.assertEqual(res, 5)

    def test_subtract_numbers(self):
        """Test subtracting numbers"""
        res = calc.subtract(10, 3)
        self.assertEqual(res, 7)

    def test_divide_numbers(self):
        """Divides numbers"""
        res = calc.divide(6, 2)
        self.assertEqual(res, 3)
