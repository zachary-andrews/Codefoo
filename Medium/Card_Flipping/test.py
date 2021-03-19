import unittest
from game import game

class importTests(unittest.TestCase):
    def setUp(self):
        self.game = game()

    def test_1(self):
        self.assertEqual("1 0 2 3 5 4 6", self.game.solve("0100110"))

    def test_2(self):
        self.assertEqual("no solution", self.game.solve("01001100111"))

    def test_3(self):
        self.assertEqual("0 1 2 3 4 6 5 7 8 11 10 9 12 13 14", self.game.solve("100001100101000"))

if __name__ == '__main__':
    unittest.main()
