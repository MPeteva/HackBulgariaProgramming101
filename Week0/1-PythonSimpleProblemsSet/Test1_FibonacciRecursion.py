import unittest

from T1_FibonacciRecursion import nth_fibonacci


class FibonacciRecursionTest(unittest.TestCase):
    def test_first_place_in_Fibonaccis_Row(self):
        self.assertEqual(1, nth_fibonacci(1))

    def test_second_place_in_Fibonaccis_Row(self):
        self.assertEqual(1, nth_fibonacci(2))

    def test_third_place_in_Fibonaccis_Row(self):
        self.assertEqual(2, nth_fibonacci(3))

    def test_any_place_in_Fibonaccis_Row(self):
        self.assertEqual(987, nth_fibonacci(16))


if __name__ == '__main__':
    unittest.main()
