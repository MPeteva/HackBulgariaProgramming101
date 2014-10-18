import unittest

from T3_SumOfDivisors import sum_of_divisors


class SumOfDivisorsTest(unittest.TestCase):
    def test_if_number_is_zero(self):
        self.assertEqual(0, sum_of_divisors(0))

    def test_if_number_is_one(self):
        self.assertEqual(1, sum_of_divisors(1))

    def test_if_number_is_two(self):
        self.assertEqual(3, sum_of_divisors(2))

    def test_if_number_is_even(self):
        self.assertEqual(60, sum_of_divisors(24))

    def test_if_number_is_odd(self):
        self.assertEqual(40, sum_of_divisors(27))


if __name__ == '__main__':
    unittest.main()
