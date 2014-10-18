import unittest

from T7_IsIntPalindrome import is_int_palindrome


class IsIntPalindromeTest(unittest.TestCase):
    def test_is_one_digit_number_palindrome(self):
        self.assertTrue(is_int_palindrome(1))

    def test_is_odd_dugit_number_palindrome_true(self):
        self.assertTrue(is_int_palindrome(1234321))

    def test_is_odd_dugit_number_palindrome_false(self):
        self.assertFalse(is_int_palindrome(12345))

    def test_is_even_dugit_number_palindrome_true(self):
        self.assertTrue(is_int_palindrome(123321))

    def test_is_even_dugit_number_palindrome_false(self):
        self.assertFalse(is_int_palindrome(123456))


if __name__ == '__main__':
    unittest.main()
