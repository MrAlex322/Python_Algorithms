import unittest
from Modul_3.HW_2.Practice_2 import findDuplicate


class TestFindDuplicate(unittest.TestCase):
    def test_find_duplicate_example1(self):
        nums = [1, 3, 4, 2, 2]
        expected = 2
        result = findDuplicate(nums)
        self.assertEqual(result, expected)

    def test_find_duplicate_example2(self):
        nums = [3, 1, 3, 4, 2]
        expected = 3
        result = findDuplicate(nums)
        self.assertEqual(result, expected)

    def test_find_duplicate_custom(self):
        nums = [5, 3, 3, 4, 2]
        expected = 3
        result = findDuplicate(nums)
        self.assertEqual(result, expected)

    def test_find_duplicate_edge_case(self):
        nums = [1]
        expected = None
        result = findDuplicate(nums)
        self.assertEqual(result, expected)

    def test_find_duplicate_large_array(self):
        nums = [i for i in range(1, 10 ** 6)] + [10 ** 5]
        expected = 10 ** 5
        result = findDuplicate(nums)
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
