import unittest
from solution import stack

class importIDTests(unittest.TestCase):
    def setUp(self):
        self.stack = stack()
        self.stack.push(1)
        self.stack.push(2)

    def test_1(self):
        self.assertEqual(1, self.stack.peek())

    def test_2(self):
        self.assertEqual(1, self.stack.pop())
    
    def test_3(self):
        self.assertEqual(False, self.stack.empty())

if __name__ == '__main__':
    unittest.main()