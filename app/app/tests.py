from django.test import TestCase
from app.calc import add, subtract

class CalcTestCase(TestCase):

    def test_add(self):
        '''test for add function'''
        self.assertEqual(add(2,6), 8)

    def test_subtract(self):
        '''test for subtract'''
        self.assertEqual(subtract(1,5), 4)
