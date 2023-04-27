import unittest
from Modul_2.HW_2.HW_2_2 import Anagrams

class TestAnagram(unittest.TestCase):
    def setUp(self):
        self.finder = Anagrams()

    def test_find_longest_substring_empty_string(self):
        s = ""
        expected = ""
        result = self.finder.find_longest_substring(s)
        self.assertEqual(result, expected)

    def test_find_longest_substring_no_repeating_chars(self):
        s = "abcdefg"
        expected = "abcdefg"
        result = self.finder.find_longest_substring(s)
        self.assertEqual(result, expected)

    def test_find_longest_substring_repeating_chars(self):
        s = "abcabcbb"
        expected = "abc"
        result = self.finder.find_longest_substring(s)
        self.assertEqual(result, expected)

    def test_find_longest_substring_repeating_chars_at_end(self):
        s = "pwwkew"
        expected = "wke"
        result = self.finder.find_longest_substring(s)
        self.assertEqual(result, expected)

    def test_find_longest_substring_repeating_chars_same_char(self):
        s = "bbbbb"
        expected = "b"
        result = self.finder.find_longest_substring(s)
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()