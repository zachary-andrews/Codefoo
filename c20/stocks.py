def buyPrice(stocks):
    return min(stocks)

def sellPrice(stocks):
    if stocks:
        return max(stocks)
    else:
        return 0

if __name__  == "__main__":
    stocks = [2,10,3,6,4,8,3,2,1]

    buy_price = buyPrice(stocks)
    sell_price = sellPrice(stocks[stocks.index(buy_price)+1:])

    if sell_price - buy_price < 0:
        profit = 0
    else:
        profit = sell_price - buy_price

    print profit
    