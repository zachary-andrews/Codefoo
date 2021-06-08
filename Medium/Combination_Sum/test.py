import unittest
from solution import Sum

class importTests(unittest.TestCase):
    def setUp(self):
        self.sum = Sum()

    def test_all(self):
        self.assertEqual([[2,2,2,2],[2,3,3],[3,5]], self.sum.combinationSum([2,3,5],8))
        self.assertEqual([[2,2,3],[7]], self.sum.combinationSum([2,3,6,7],7))
        self.assertEqual([], self.sum.combinationSum([2],1))
        self.assertEqual([[1]], self.sum.combinationSum([1],1))
        self.assertEqual([[1,1]], self.sum.combinationSum([1],2))

if __name__ == '__main__':
    unittest.main()