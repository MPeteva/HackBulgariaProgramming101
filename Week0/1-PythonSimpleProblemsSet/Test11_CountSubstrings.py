import unittest

from T11_CountSubstrings import count_substrings


class CountSubstringsTest(unittest.TestCase):
    def test_number_of_occurrences_of_singal_char(self):
        self.assertEqual(4, count_substrings("Python is an awesome language to program in!", "o"))

    def test_number_of_occurrences(self):
        self.assertEqual(2, count_substrings("This is a test string", "is"))

    def test_number_of_occurrences_when_they_can_be_count_twice(self):
        self.assertEqual(2, count_substrings("babababa", "baba"))

    def test_number_of_occurrences_if_doesnt_occurred(self):
        self.assertEqual(0, count_substrings("We have nothing in common!", "really?"))


if __name__ == '__main__':
    unittest.main()
