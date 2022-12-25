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
    
    def test_substract_numbers(self):
        '''Test subtracting numbers.'''
        res = calc.subtract(10, 15)
        
        self.assertEqual(res, 5)
