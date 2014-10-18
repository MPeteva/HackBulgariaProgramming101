import unittest

from T13_CountConsonants import count_consonants


class CountConsonantsTest(unittest.TestCase):
    def test_none_consonants(self):
        self.assertEqual(0, count_consonants("Aaaa!"))

    def test_count_of_consonants_if_there_is_consonant_in_the_end(self):
        self.assertEqual(44, count_consonants("Github is the second best thing that happend to programmers, after the keyboard!"))

    def test_count_of_consonants(self):
        self.assertEqual(11, count_consonants("Theistareykjarbunga"))


if __name__ == '__main__':
    unittest.main()
