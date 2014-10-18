import unittest

from T10_IsNumberBalanced import is_number_balanced


class IsNumberBalancedTest(unittest.TestCase):
    def test_is_one_digit_number_balanced(self):
        self.assertTrue(is_number_balanced(1))

    def test_is_odd_dugit_number_balanced_true(self):
        self.assertTrue(is_number_balanced(1238033))

    def test_is_odd_dugit_number_balanced_false(self):
        self.assertFalse(is_number_balanced(28471))

    def test_is_even_dugit_number_balanced_true(self):
        self.assertTrue(is_number_balanced(134161))

    def test_is_even_dugit_number_balanced_false(self):
        self.assertFalse(is_number_balanced(3516))


if __name__ == '__main__':
    unittest.main()
