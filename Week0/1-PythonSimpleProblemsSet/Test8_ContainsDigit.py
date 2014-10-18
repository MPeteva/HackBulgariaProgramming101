import unittest

from T8_ContainsDigit import contains_digit


class ContainsDigitTest(unittest.TestCase):
    def test_if_number_contains_a_digit_true(self):
        self.assertTrue(contains_digit(123456789, 5))

    def test_if_number_contains_a_digit_false(self):
        self.assertFalse(contains_digit(123, 4))


if __name__ == '__main__':
    unittest.main()
