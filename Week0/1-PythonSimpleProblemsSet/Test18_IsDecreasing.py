import unittest

from T18_IsDecreasing import is_decreasing


class IsDecreasingTest(unittest.TestCase):
    def test_if_there_is_no_number_in_the_list(self):
        self.assertFalse(is_decreasing([]))

    def test_if_there_is_one_number_in_the_list(self):
        self.assertTrue(is_decreasing([1]))

    def test_is_decreasing_true(self):
        self.assertTrue(is_decreasing([5, 4, 3, 2, 1]))

    def test_is_decreasing_false(self):
        self.assertFalse(is_decreasing([-10, 10, 5, 2]))

    def test_when_there_are_equal_numbers(self):
        self.assertFalse(is_decreasing([1, 1, 1, 1]))


if __name__ == '__main__':
    unittest.main()
