import unittest
from solution import unscramble

class importTests(unittest.TestCase):
    def setUp(self):
        self.unscramble = unscramble()

    def test_1(self):
        self.assertEqual("This is a message", self.unscramble.get_word("ehTsii  s aemssga"))

    def test_2(self):
        self.assertEqual("HARRY POTTER AND THE GOBLET OF FIRE", self.unscramble.get_word("EAHRR YOPTTREA DNT EHG BOEL TFOF RI"))
    
    def test_3(self):
        self.assertEqual("abcde", self.unscramble.get_word("ebadc"))
    
    def test_4(self):
        self.assertEqual("abcd", self.unscramble.get_word("badc"))

if __name__ == '__main__':
    unittest.main()