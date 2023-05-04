import unittest
from Modul_2.HW_2.Pr_1.HW_2 import AnagramGrouper

class TestAnagramGrouper(unittest.TestCase):

    def test_empty_input(self):
        ag = AnagramGrouper()
        self.assertEqual(ag.group_anagrams([]), [])

    def test_single_word(self):
        ag = AnagramGrouper()
        self.assertEqual(ag.group_anagrams(["hello"]), [["hello"]])

    def test_multiple_words(self):
        ag = AnagramGrouper()
        input = ["eat", "tea", "tan", "ate", "nat", "bat"]
        expected_output = [["eat","tea","ate"], ["tan","nat"], ["bat"]]
        self.assertEqual(ag.group_anagrams(input), expected_output)

    def test_duplicate_words(self):
        ag = AnagramGrouper()
        input = ["eat", "tea", "tan", "ate", "tan", "bat"]
        expected_output = [["eat","tea","ate"], ["tan","nat"], ["bat"]]
        self.assertEqual(ag.group_anagrams(input), expected_output)

if __name__ == '__main__':
    unittest.main()
