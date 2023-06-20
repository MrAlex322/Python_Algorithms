import unittest
from Practice_1 import BinarySearch

class BinarySearchTests(unittest.TestCase):
    def setUp(self):
        self.bs = BinarySearch()

    def test_search_insert_found(self):
        arr = [1, 3, 5, 6]
        target = 5
        expected = 2
        result = self.bs.search_insert(arr, target)
        self.assertEqual(result, expected)

    def test_search_insert_not_found(self):
        arr = [1, 3, 5, 6]
        target = 4
        expected = 2
        result = self.bs.search_insert(arr, target)
        self.assertEqual(result, expected)

    def test_search_insert_duplicate(self):
        arr = [1, 3, 4, 4, 5, 6]
        target = 4
        expected = 2
        result = self.bs.search_insert(arr, target)
        self.assertEqual(result, expected)

    def test_search_insert_empty_array(self):
        arr = []
        target = 5
        expected = 0
        result = self.bs.search_insert(arr, target)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
