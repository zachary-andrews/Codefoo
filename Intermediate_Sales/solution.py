class intermediate_sales:
    def get_profit(self,Revenue,Expenses):
        Profit = Expenses
        for i in range(len(Revenue)):
            for j in range(len(Revenue[0])):
                if isinstance(Revenue[i][j], int):
                    Profit[i][j] = max(0, Revenue[i][j] - Expenses[i][j])
                    
        return Profit

    def run_the_numbys(self,Profit):
        Commission = []
        for i in range(len(Profit)):
            count = 0
            for j in range(len(Profit[0])):
                if isinstance(Profit[i][j], int):
                    count += Profit[i][j]
            if i > 0:   
                Commission.append([Profit[i][0],round(count*.062,2)])
        return Commission

    def get_sales(self,sales_array,expenses_array):
        Revenue = sales_array
        Expenses = expenses_array
        Profit = self.get_profit(Revenue,Expenses)
        Commission = self.run_the_numbys(Profit)
        return Commission