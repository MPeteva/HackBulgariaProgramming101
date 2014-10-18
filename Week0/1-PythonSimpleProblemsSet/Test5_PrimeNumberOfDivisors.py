import unittest

from T5_PrimeNumberOfDivisors import number_of_divisors
from T5_PrimeNumberOfDivisors import prime_number_of_divisors


class PrimeNumberOfDivisorsTest(unittest.TestCase):
    def test_number_of_divisors_of_zero(self):
        self.assertEqual(0, number_of_divisors(0))

    def test_number_of_divisors_of_one(self):
        self.assertEqual(1, number_of_divisors(1))

    def test_number_of_divisors(self):
        self.assertEqual(8, number_of_divisors(24))

    def test_is_number_of_divisors_of_zero_prime(self):
        self.assertFalse(prime_number_of_divisors(0))

    def test_is_number_of_divisors_of_one_prime(self):
        self.assertFalse(prime_number_of_divisors(1))

    def test_is_number_of_divisors_prime_if_number_is_prime(self):
        self.assertTrue(prime_number_of_divisors(31))

    def test_is_number_of_divisors_prime_True(self):
        self.assertTrue(prime_number_of_divisors(16))

    def test_is_number_of_divisors_prime_False(self):
        self.assertFalse(prime_number_of_divisors(24))


if __name__ == '__main__':
    unittest.main()
