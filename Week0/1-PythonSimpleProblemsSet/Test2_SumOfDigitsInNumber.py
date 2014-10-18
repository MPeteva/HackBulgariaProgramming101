import unittest

from T2_SumOfDigitsInNumber import sum_of_digits


class SumOfDigitsNumberTest(unittest.TestCase):
    def test_if_number_is_negative(self):
        self.assertEqual(7, sum_of_digits(-1123))

    def test_second_place_in_Fibonaccis_Row(self):
        self.assertEqual(43, sum_of_digits(1325132435356))


if __name__ == '__main__':
    unittest.main()
