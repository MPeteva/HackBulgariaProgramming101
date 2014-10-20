import unittest

from T16_BiggestDifference import biggest_difference


class BiggestDifferenceTest(unittest.TestCase):
    def test_if_there_is_no_number_in_hte_list(self):
        self.assertFalse(biggest_difference([]))

    def test_biggest_difference(self):
        self.assertEqual(-4, biggest_difference([1, 2, 3, 4, 5]))

    def test_biggest_difference_if_there_are_negative_number(self):
        self.assertEqual(-9, biggest_difference([-10, -9, -1]))


if __name__ == '__main__':
    unittest.main()
