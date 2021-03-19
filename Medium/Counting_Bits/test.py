import unittest
from solution import counting_bits

class importTests(unittest.TestCase):
    def setUp(self):
        self.counting_bits = counting_bits()

    def test_1(self):
        self.assertEqual([0,1,1], self.counting_bits.get_bits(2))

    def test_2(self):
        self.assertEqual([0,1,1,2,1,2], self.counting_bits.get_bits(5))

if __name__ == '__main__':
    unittest.main()