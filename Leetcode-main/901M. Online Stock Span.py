class StockSpanner: #fre-50, Amazon

    def __init__(self):
        self.stack = []

    #题目的consecutive days of price drop to the past的条件 
    #每次运算，stack只保留过去价格比现在大的[price, res] 和 当前计算出来的[price_cur, res_cur]
    def next(self, price: int) -> int:
        res = 1
        while self.stack and self.stack[-1][0] <= price:
            res += self.stack[-1][1]
            self.stack.pop()
        self.stack.append([price, res])
        return res


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
