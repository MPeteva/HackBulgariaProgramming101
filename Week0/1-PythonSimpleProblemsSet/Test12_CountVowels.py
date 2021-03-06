import unittest

from T12_CountVowels import count_vowels


class CountVowelsTest(unittest.TestCase):
    def test_none_vowels(self):
        self.assertEqual(0, count_vowels("grrrrgh!"))

    def test_count_of_vowels_if_there_is_vowel_in_the_end(self):
        self.assertEqual(8, count_vowels("Theistareykjarbunga"))

    def test_count_of_vowels(self):
        self.assertEqual(22, count_vowels("Github is the second best thing that happend to programmers, after the keyboard!"))


if __name__ == '__main__':
    unittest.main()
