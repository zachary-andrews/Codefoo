import unittest
from simple_solution import Flowers

class importTests(unittest.TestCase):
    def setUp(self):
        self.flowerbed = Flowers()

    def test1(self):
        self.assertTrue(self.flowerbed.check([1,0,0,0,1], 1))
    
    def test2(self):
        self.assertFalse(self.flowerbed.check([1,0,0,0,1], 2))
    
    def test3(self):
        self.assertFalse(self.flowerbed.check([1,0,0,0,0,0,1], 3))

if __name__ == '__main__':
    unittest.main()