import unittest

from T6_SevensInARow import sevens_in_a_row


class SevensInARowTest(unittest.TestCase):
    def test_sevens_in_an_empty_row_true(self):
        self.assertTrue(sevens_in_a_row([], 0))

    def test_sevens_in_an_empty_row_false(self):
        self.assertFalse(sevens_in_a_row([], 5))

    def test_sevens_in_row_if_there_are_more_in_a_serial(self):
        self.assertFalse(sevens_in_a_row([7, 7, 7, 1, 1, 1, 7, 7, 7, 7], 2))

    def test_sevens_in_row_if_serial_isnt_last(self):
        self.assertTrue(sevens_in_a_row([7, 7, 7, 1, 1, 1, 7, 7, 7, 7], 3))

    def test_sevens_in_row_if_they_are_not_in_a_serial(self):
        self.assertFalse(sevens_in_a_row([10, 8, 7, 6, 7, 7, 7, 20, 7], 5))

    def test_sevens_in_row_if_there_are_not_enough_sevens_in_a_serial(self):
        self.assertFalse(sevens_in_a_row([10, 8, 7, 6, 7, 7, 7, 20, -7], 4))



if __name__ == '__main__':
    unittest.main()
