import calc
import unittest


class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calc.add(10, 20), 30)

    def test_sub(self):
        self.assertEqual(calc.sub(10, 20), 10)

    def test_mul(self):
        self.assertEqual(calc.mul(10, 10), 100)

    def test_div(self):
        self.assertEqual(calc.div(10, 2), 5)
        with self.assertRaises(Exception):
            self.assertEqual(calc.div(10, 0), 0)
