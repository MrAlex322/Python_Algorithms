import unittest
from HW_1 import EmailAnalyzer


# Тесты

class TestEmailAnalyzer(unittest.TestCase):
    def setUp(self):
        self.arr = [
            {"email": "vas@gmail.com", "max_amount": 1},
            {"email": "gg@gmail.com", "max_amount": 123},
            {"email": "test@gmail.com", "max_amount": 10},
            {"email": "vas@gmailg.com", "max_amount": 5},
            {"email": "xyz@gmail.com", "max_amount": 45},
            {"email": "gg@gmail.com", "max_amount": 12},
        ]
        self.analyzer = EmailAnalyzer(self.arr)

    def test_find_most_frequent_email(self):
        self.assertEqual(self.analyzer.find_most_frequent_email(), "vas@gmail.com")

    def test_find_sum_values(self):
        self.assertEqual(self.analyzer.find_sum_values(), (1, 123))

    def test_sort_by_max_amount(self):
        expected_arr = [
            {"email": "gg@gmail.com", "max_amount": 123},
            {"email": "xyz@gmail.com", "max_amount": 45},
            {"email": "test@gmail.com", "max_amount": 10},
            {"email": "vas@gmail.com", "max_amount": 5},
        ]
        self.assertEqual(self.analyzer.sort_by_max_amount(), expected_arr)

    def test_negative_max_amount(self):
        self.assertEqual(self.analyzer.find_sum_values(), (-10, 123))


if __name__ == '__main__':
    unittest.main()
