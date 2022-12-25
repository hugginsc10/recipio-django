"""
SAMPLE TESTS
"""

from django.test import SimpleTestCase
from app import calc

class CalcTests(SimpleTestCase):
    '''
    Test the Calc Module.
    '''
    def test_add_numbers(self):
        '''
        Test that two numbers are added together.
        '''
        self.assertEqual(calc.add(3, 8), 11)
        