import unittest
from solution import Sum

class importTests(unittest.TestCase):
    def setUp(self):
        self.sum = Sum()

    def test_1(self):
        self.assertEqual([[2,2,2,2],[2,3,3],[3,5]], self.sum.combinationSum([2,3,5],8))

    def test_2(self):
        self.assertEqual([[2,2,3],[7]], self.sum.combinationSum([2,3,6,7],7))

    def test_3(self):
        self.assertEqual([], self.sum.combinationSum([2],1))

    def test_4(self):
        self.assertEqual([[1]], self.sum.combinationSum([1],1))

    def test_5(self):
        self.assertEqual([[1,1]], self.sum.combinationSum([1],2))

if __name__ == '__main__':
    unittest.main()