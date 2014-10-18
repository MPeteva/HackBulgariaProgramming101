import unittest

from T7_IsIntPalindrome import is_int_palindrome


class IsIntPalindromeTest(unittest.TestCase):
    def test_sevens_in_an_empty_row_true(self):
        self.assertTrue(is_int_palindrome([], 0))

    def test_sevens_in_an_empty_row_false(self):
        self.assertFalse(is_int_palindrome([], 5))


if __name__ == '__main__':
    unittest.main()
