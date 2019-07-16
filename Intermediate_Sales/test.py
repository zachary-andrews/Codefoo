import unittest
from solution import intermediate_sales

class importTests(unittest.TestCase):
    def setUp(self):
        self.sales = intermediate_sales()

    def test_1(self):
        Commission = [
                    ['Frank',6.20],
                    ["Jane",9.49]
                ]
        Revenue = [
                    ['drinks','tea','coffee'],
                    ['Frank',120,243],
                    ["Jane",145,265]
                ]
        Expenses = [
                    ['drinks','tea','coffee'],
                    ['Frank',130,143],
                    ["Jane",59,198]
                ]
        

        
        self.assertEqual(Commission,self.sales.get_sales(Revenue,Expenses))

        
    def test_2(self):
        Commission = [
                    ['Johnver',92.32],
                    ["Vanston",5.21],
                    ['Danbree',113.21],
                    ['Vansey',45.45],
                    ['Mundyke',32.55]
                ]   
        Revenue = [
                    ['drinks','tea','coffee','milk','water'],
                    ['Johnver',190,325,682,829],
                    ["Vanston",140,19,14,140],
                    ['Danbree',1926,293,852,609],
                    ["Vansey",14,1491,56,120],
                    ['Mundyke',143,162,659,87]
                ]
        Expenses = [
                    ['drinks','tea','coffee','milk','water'],
                    ['Johnver',120,300,50,67],
                    ["Vanston",65,10,299,254],
                    ['Danbree',890,23,1290,89],
                    ["Vansey",54,802,12,129],
                    ['Mundyke',430,235,145,76]
                ]

        self.assertEqual(Commission,self.sales.get_sales(Revenue,Expenses))
if __name__ == '__main__':
    unittest.main()