import unittest
from solution import ID

class importIDTests(unittest.TestCase):
    def setUp(self):
        self.number_id = ID()

    def test_1(self):
        self.assertEqual(50, len(self.number_id.create_ids(50)))

    def test_2(self):
        id_list = self.number_id.create_ids(1000)
        self.assertEqual(len(id_list),len(set(id_list)))

    def test_3(self):
        self.assertEqual(-1,self.number_id.create_ids(1001))

    
if __name__ == '__main__':
    unittest.main()