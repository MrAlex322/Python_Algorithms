import unittest
from HW_2 import Solution
class SolutionTests(unittest.TestCase):
    def test_findMinIndexSum(self):
        solution = Solution()

        # Тест 1
        list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
        list2 = ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
        expected = ["Shogun"]
        result = solution.findMinIndexSum(list1, list2)
        self.assertEqual(result, expected)

        # Тест 2
        list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
        list2 = ["KFC", "Shogun", "Burger King"]
        expected = ["Shogun"]
        result = solution.findMinIndexSum(list1, list2)
        self.assertEqual(result, expected)

        # Тест 3
        list1 = ["happy", "sad", "good"]
        list2 = ["sad", "happy", "good"]
        expected = ["sad", "happy"]
        result = solution.findMinIndexSum(list1, list2)
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()
