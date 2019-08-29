import unittest
from solution import tax

class importTests(unittest.TestCase):
    def setUp(self):
        self.tax = tax()

    def test_1(self):
        self.assertEqual(0, self.tax.get(0))

    def test_2(self):
        self.assertEqual(0, self.tax.get(10000))
    
    def test_3(self):
        self.assertEqual(0, self.tax.get(10009))

    def test_4(self):
        self.assertEqual(1, self.tax.get(10010))

    def test_5(self):
        self.assertEqual(200, self.tax.get(12000))
    
    def test_6(self):
        self.assertEqual(8697, self.tax.get(56789))
    
    def test_7(self):
        self.assertEqual(473326, self.tax.get(1234567))
    
if __name__ == '__main__':
    unittest.main()