import unittest
from solution import decode

class importTests(unittest.TestCase):
    def setUp(self):
        self.decode = decode()

    def test_1(self):
        self.assertEqual("aaabcbc", self.decode.get_word("3[a]2[bc]"))

    def test_2(self):
        self.assertEqual("accaccacc", self.decode.get_word("3[a2[c]]"))
    
    def test_3(self):
        self.assertEqual("abcabccdcdcdef", self.decode.get_word("2[abc]3[cd]ef"))

if __name__ == '__main__':
    unittest.main()