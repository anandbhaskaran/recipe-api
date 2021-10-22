from django.test import TestCase

from app.calc import add


class CalcTests(TestCase):

    def test_Add_numbers(self):
        """Test that two numbers are added togather"""
        self.assertEqual(add(3, 8), 11)
