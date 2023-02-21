import unittest

class importTests(unittest.TestCase):
    def setUp(self):
        self.factorial = Factorial()

    def test_1(self):
        self.assertEqual(6, self.factorial.solve(3))
    
    def test_2(self):
        self.assertEqual(40320, self.factorial.solve(8))
        
class Factorial:
    def solve(self, Number: int) -> int:
        return self.recurse(Number)

    def recurse(self, number: int) -> int:
        if number == 1:
            return number
        else:
            return number*self.recurse(number-1)
if __name__ == '__main__':
    unittest.main()

