import unittest
from solution import light

class importTests(unittest.TestCase):
    def setUp(self):
        self.light = light()

    def test_1(self):
        self.assertEqual(3, self.light.get([
                                            ('1','3'),
                                            ('2','3'),
                                            ('4','5')
                                        ]))

    def test_2(self):
        self.assertEqual(7, self.light.get([
                                            ('2','4'),
                                            ('3','6'),
                                            ('1','3'),
                                            ('6','8')
                                        ]))
    
    def test_3(self):
        self.assertEqual(5, self.light.get([
                                            ('6','8'),
                                            ('5','8'),
                                            ('8','9'),
                                            ('5','7'),
                                            ('4','7')
                                        ]))

    
if __name__ == '__main__':
    unittest.main()