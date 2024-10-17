import calc
import unittest


class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calc.add(10, 20), 30)

    def test_sub(self):
        self.assertEqual(calc.sub(10, 20), 10)
