import unittest
from solution import Palindrom

class importTests(unittest.TestCase):
    def setUp(self):
        self.palindrom = palindrom()

    def test_1(self):
        self.assertEqual("racecar", self.palindrom.get_palindrom_substring("racecar"))

if __name__ == '__main__':
    unittest.main()