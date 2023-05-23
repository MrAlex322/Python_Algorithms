import unittest
from HW_1 import MyQueue

class TestMyQueue(unittest.TestCase):
    def test_push_and_peek(self):
        q = MyQueue()
        q.push(1)
        self.assertEqual(q.peek(), 1)
        q.push(2)
        self.assertEqual(q.peek(), 1)
        q.push(3)
        self.assertEqual(q.peek(), 1)

    def test_pop(self):
        q = MyQueue()
        q.push(1)
        q.push(2)
        q.push(3)
        self.assertEqual(q.pop(), 1)
        self.assertEqual(q.pop(), 2)
        self.assertEqual(q.pop(), 3)
        self.assertIsNone(q.pop())

    def test_empty(self):
        q = MyQueue()
        self.assertTrue(q.empty())
        q.push(1)
        self.assertFalse(q.empty())
        q.pop()
        self.assertTrue(q.empty())

    def test_print_queue(self):
        q = MyQueue()
        q.print_queue()
        q.push(1)
        q.push(2)
        q.push(3)
        q.print_queue()
        q.pop()
        q.print_queue()
        self.assertEqual(q.pop(), 2)
        q.print_queue()

    if __name__ == '__main__':
        unittest.main()