import unittest
from solution import rentals

class importTests(unittest.TestCase):
    def setUp(self):
        self.cr = rentals()

    def test_1(self):
        self.assertEqual(5, self.cr.get_number_cars("10",  
                                                    "1 5 12 13 40 30 22 70 19",  
                                                    "23 10 29 25 66 35 33 100 65"))


if __name__ == '__main__':
    unittest.main()