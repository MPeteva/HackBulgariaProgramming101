import unittest

from T19_ZeroInsert import zero_insert


class IsDecreasingTest(unittest.TestCase):
    def test_if_there_is_one_number(self):
        self.assertEqual(zero_insert(1), 1)

    def test_if_every_two_numbers_that_are_equal_are_separeted_by_zero(self):
        self.assertEqual(zero_insert(55555), 505050505)

    def test_if_there_is_no_zeroes_added(self):
        self.assertEqual(zero_insert(16357), 16357)


if __name__ == '__main__':
    unittest.main()
