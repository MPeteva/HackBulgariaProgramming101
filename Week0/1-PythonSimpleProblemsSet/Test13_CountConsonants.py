import unittest

from T13_CountConsonants import count_consonants


class CountConsonantsTest(unittest.TestCase):
    def test_none_consonants(self):
        self.assertEqual(0, count_consonants("Aaaa!"))

    def test_count_of_consonants(self):
        self.assertEqual(44, count_consonants("Github is the second best thing that happend to programmers, after the keyboard!"))


if __name__ == '__main__':
    unittest.main()
