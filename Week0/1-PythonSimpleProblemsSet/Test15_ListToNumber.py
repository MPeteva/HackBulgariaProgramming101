import unittest

from T15_ListToNumber import list_to_number


class ListToNumberTest(unittest.TestCase):
    def test_if_there_is_no_number_in_hte_list(self):
        self.assertFalse(0, list_to_number([]))

    def test_list_to_number(self):
        self.assertEqual(123023, list_to_number([1, 2, 3, 0, 2, 3]))

    def test_list_to_number_if_there_are_similar_numbers(self):
        self.assertEqual(99999, list_to_number([9, 9, 9, 9, 9]))


if __name__ == '__main__':
    unittest.main()
