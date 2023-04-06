import unittest
from HW_2 import AnagramGrouper

class TestAnagramGroups(unittest.TestCase):
    def test_empty_list(self):
        anagram_groups = AnagramGrouper()
        input_data = []
        expected_output = []
        self.assertEqual(anagram_groups.group_anagrams(input_data), expected_output)

    def test_single_word(self):
        anagram_groups = AnagramGrouper()
        input_data = ["abc"]
        expected_output = [["abc"]]
        self.assertEqual(anagram_groups.group_anagrams(input_data), expected_output)

    def test_no_anagrams(self):
        anagram_groups = AnagramGrouper()
        input_data = ["abc", "def", "xyz"]
        expected_output = [["abc"], ["def"], ["xyz"]]
        self.assertEqual(anagram_groups.group_anagrams(input_data), expected_output)

if __name__ == '__main__':
    unittest.main()