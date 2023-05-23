import unittest

class TestMyQueue(unittest.TestCase):
    def test_push_and_peek(self):
        queue = MyQueue()
        queue.push(1)
        self.assertEqual(queue.peek(), 1)
        queue.push(2)
        self.assertEqual(queue.peek(), 1)
        queue.push(3)
        self.assertEqual(queue.peek(), 1)

    def test_pop(self):
        queue = MyQueue()
        queue.push(1)
        queue.push(2)
        queue.push(3)
        self.assertEqual(queue.pop(), 1)
        self.assertEqual(queue.pop(), 2)
        self.assertEqual(queue.pop(), 3)
        self.assertIsNone(queue.pop())

    def test_empty(self):
        queue = MyQueue()
        self.assertTrue(queue.empty())
        queue.push(1)
        self.assertFalse(queue.empty())
        queue.pop()
        self.assertTrue(queue.empty())

    def test_print_queue(self):
        queue = MyQueue()
        queue.print_queue()
        queue.push(1)
        queue.push(2)
        queue.push(3)
        queue.print_queue()
        queue.pop()
        queue.print_queue()
        self.assertEqual(queue.pop(), 2)
        queue.print_queue()

    if __name__ == '__main__':
        unittest.main()
