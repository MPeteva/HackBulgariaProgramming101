import unittest

from T14_NumberToList import number_to_list


class NumberToList(unittest.TestCase):
    def test_if_there_is_no_number(self):
        self.assertEqual([], number_to_list()) # DAva mi bug tuka, che ne sum napisala chislo v skobite???

    def test_number_to_list(self):
        self.assertEqual([1, 2, 3, 0, 2, 3], number_to_list(123023))

    def test_number_to_list_if_there_are_similar_numbers(self):
        self.assertEqual([9, 9, 9, 9, 9], number_to_list(99999))


if __name__ == '__main__':
    unittest.main()
