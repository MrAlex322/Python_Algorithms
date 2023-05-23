import unittest
from HW_2 import Discount


class TestDiscount(unittest.TestCase):

    def setUp(self):
        self.discount = Discount()

    def test_initial_price(self):
        self.assertEqual(self.discount.price, [1, 1, 1, 1])

    def test_fees(self):
        self.assertEqual(self.discount.fees(), [1, 0, 0, 0])


if __name__ == '__main__':
    unittest.main()
