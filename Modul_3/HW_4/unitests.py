import unittest
from Practice_1 import most_frequent


class TestKMostFrequent(unittest.TestCase):

    def test_example_1(self):
        nums = [1, 1, 1, 2, 2, 3]
        k = 2
        result = most_frequent(nums, k)
        self.assertCountEqual(result, [1, 2])

    def test_example_2(self):
        nums = [1]
        k = 1
        result = most_frequent(nums, k)
        self.assertEqual(result, [1])

    def test_repeated_elements(self):
        nums = [5, 5, 5, 5, 3, 3, 2, 2, 2, 1, 1]
        k = 2
        result = most_frequent(nums, k)
        self.assertCountEqual(result, [5, 2])  #


if __name__ == '__main__':
    unittest.main()
