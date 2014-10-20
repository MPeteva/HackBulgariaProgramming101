import unittest

from T17_IsIncreasing import is_increasing


class IsIncreasingTest(unittest.TestCase):
    def test_if_there_is_no_number_in_the_list(self):
        self.assertFalse(is_increasing([]))

    def test_if_there_is_one_number_in_the_list(self):
        self.assertTrue(is_increasing([1]))

    def test_is_increasing_true(self):
        self.assertTrue(is_increasing([1, 2, 3, 4, 5]))

    def test_is_increasing_false(self):
        self.assertFalse(is_increasing([5, 6, -10]))

    def test_when_there_are_equal_numbers(self):
        self.assertFalse(is_increasing([1, 1, 1, 1]))


if __name__ == '__main__':
    unittest.main()
