import unittest

from T9_ContainsDigits import contains_digits


class ContainsDigitsTest(unittest.TestCase):
    def test_if_list_of_numbers_is_empty(self):
        self.assertTrue(contains_digits(456, []))

    def test_if_number_contains_all_digits(self):
        self.assertTrue(contains_digits(402123, [0, 3, 4]))

    def test_if_number_doesnt_contain_all_digits(self):
        self.assertFalse(contains_digits(123456789, [1, 2, 3, 0]))


if __name__ == '__main__':
    unittest.main()
