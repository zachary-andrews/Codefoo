import unittest
from solution import two_city

class importIDTests(unittest.TestCase):
    def setUp(self):
        self.two_city = two_city()

    def test_1(self):
        self.assertEqual(110, self.two_city.get_cost([[10,20],[30,200],[400,50],[30,20]]))

    def test_2(self):
        self.assertEqual(34, self.two_city.get_cost([[1,100],[10,11],[2,99],[10,20]]))
    
    def test_3(self):
        self.assertEqual(1004, self.two_city.get_cost([[700,500],[2,1],[500,1000],[4,2]]))

if __name__ == '__main__':
    unittest.main()