import unittest
from solution import Lights

class importIDTests(unittest.TestCase):
    def setUp(self):
        self.lights = Lights()

    def test_1(self):
        self.assertEqual(1, self.lights.solve_lights(3))

if __name__ == '__main__':
    unittest.main()