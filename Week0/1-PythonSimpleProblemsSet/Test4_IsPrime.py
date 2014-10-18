import unittest

from T4_IsPrime import is_prime


class IsPrimeTest(unittest.TestCase):
    def test_is_negative_number_prime(self):
        self.assertFalse(is_prime(-102))

    def test_is_zero_prime(self):
        self.assertFalse(is_prime(0))

    def test_is_one_prime(self):
        self.assertFalse(is_prime(1))

    def test_is_two_prime(self):
        self.assertTrue(is_prime(2))

    def test_is_three_prime(self):
        self.assertTrue(is_prime(3))

    def test_is_even_number_prime(self):
        self.assertFalse(is_prime(2452))

    def test_is_odd_number_prime_true(self):
        self.assertTrue(is_prime(587))

    def test_is_odd_number_prime_false(self):
        self.assertFalse(is_prime(377))

if __name__ == '__main__':
    unittest.main()
