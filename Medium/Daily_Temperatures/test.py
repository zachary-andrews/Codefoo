import unittest
from solution import Temps

class importTests(unittest.TestCase):
    def setUp(self):
        self.temps = Temps()

    def test_1(self):
        self.assertEqual([1,1,4,2,1,1,0,0], self.temps.dailyTemperatures([73,74,75,71,69,72,76,73]))

    def test_2(self):
        self.assertEqual([1,1,1,0], self.temps.dailyTemperatures([30,40,50,60]))

    def test_3(self):
        self.assertEqual([1,1,0], self.temps.dailyTemperatures([30,60,90]))
if __name__ == '__main__':
    unittest.main()