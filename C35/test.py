import unittest
from solution import bowling

class importIDTests(unittest.TestCase):
    def setUp(self):
        self.bowling = bowling()

    def test_1(self):
        self.assertEqual(300, self.bowling.get_score("X X X X X X X X X X X X"))

    def test_2(self):
        self.assertEqual(90, self.bowling.get_score("9- 9- 9- 9- 9- 9- 9- 9- 9- 9-"))

    def test_3(self):
        self.assertEqual(150,self.bowling.get_score("5/ 5/ 5/ 5/ 5/ 5/ 5/ 5/ 5/ 5/ 5"))

    def test_4(self):
        self.assertEqual(149,self.bowling.get_score("8/ 54 9- X X 5/ 53 63 9/ 9/ X"))

if __name__ == '__main__':
    unittest.main()