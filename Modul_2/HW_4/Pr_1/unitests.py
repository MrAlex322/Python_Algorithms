import unittest
from HW_1 import HarmonicSubsequence


class TestHarmonicSubsequence(unittest.TestCase):
    def setUp(self):
        self.hs = HarmonicSubsequence()

    def test_findLHS(self):
        nums1 = [1, 3, 2, 2, 5, 2, 3, 7]
        expected1 = 5
        self.assertEqual(self.hs.findLHS(nums1), expected1)

        nums2 = [1, 2, 3, 4]
        expected2 = 2
        self.assertEqual(self.hs.findLHS(nums2), expected2)

        nums3 = [1, 1, 1, 1]
        expected3 = 0
        self.assertEqual(self.hs.findLHS(nums3), expected3)

        nums4 = []
        expected4 = 0
        self.assertEqual(self.hs.findLHS(nums4), expected4)

        nums5 = [1]
        expected5 = 0
        self.assertEqual(self.hs.findLHS(nums5), expected5)

        nums6 = [1, 2, 4, 5, 6, 8]
        expected6 = 0
        self.assertEqual(self.hs.findLHS(nums6), expected6)


if __name__ == '__main__':
    unittest.main()
