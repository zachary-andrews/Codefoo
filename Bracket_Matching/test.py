import unittest
from solution import brackets

class importTests(unittest.TestCase):
    def setUp(self):
        self.brackets = brackets()

    def test_1(self):
        self.assertEqual("Yes", self.brackets.check("(){}[]"))

    def test_2(self):
        self.assertEqual("No",self.brackets.check("[{]}"))

    def test_3(self):
        self.assertEqual("Yes",self.brackets.check("[{}([])]"))

    def test_4(self):
        self.assertEqual("No",self.brackets.check("({[])}"))


if __name__ == '__main__':
    unittest.main()
