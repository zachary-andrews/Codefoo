import unittest
from solution import LRUCache

class importTests(unittest.TestCase):
    def setUp(self):
        self.cache = LRUCache(2)

    def test_1(self):
        self.cache.put(2,2)
        self.assertEqual(2, self.cache.get(2))
    
    def test_2(self):
        self.cache.put(1, 1)
        self.cache.put(2, 2)   
        self.assertEqual(1, self.cache.get(1))

    def test_3(self):
        self.cache.put(1, 1)
        self.cache.put(2, 2)
        self.cache.get(1);   
        self.cache.put(3, 3)    
        self.assertEqual(-1, self.cache.get(2))
    
    def test_4(self):
        self.cache.put(1, 1)
        self.cache.put(2, 2)
        self.cache.get(1)
        self.cache.put(3, 3)
        self.cache.get(2)
        self.cache.put(4, 4)
        self.assertEqual(-1, self.cache.get(1))

    def test_5(self):
        self.cache.put(1, 1)
        self.cache.put(2, 2)
        self.cache.get(1)
        self.cache.put(3, 3)
        self.cache.get(2)
        self.cache.put(4, 4)
        self.assertEqual(3, self.cache.get(3))

    def test_6(self):
        self.cache.put(1, 1)
        self.cache.put(2, 2)
        self.cache.get(1)
        self.cache.put(3, 3)
        self.cache.get(2)
        self.cache.put(4, 4)
        self.cache.get(1)
        self.cache.get(3)
        self.assertEqual(4,self.cache.get(4))

if __name__ == '__main__':
    unittest.main()