""" Tests
"""

import unittest
from leap_year import days_in_month

class MyTest(unittest.TestCase):

    def test_1(self):
        self.assertEqual(days_in_month(2018, 2), 28)

    def test_2(self):
        self.assertEqual(days_in_month(2020, 2), 29)

    def test_3(self):
        self.assertEqual(days_in_month(2019, 4), 30)

    def test_4(self):
        self.assertEqual(days_in_month(1045, 5), 31)

print("\n")
print('Running some tests on your code:')
print(".\n.\n.\n.")
unittest.main(verbosity=1, exit=False)
