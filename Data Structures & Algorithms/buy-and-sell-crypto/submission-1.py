class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        lowest_price = sys.maxsize
        for i, price in enumerate(prices):
            if i <1:
                lowest_price = min(lowest_price, price)
                continue
            lowest_price = min(lowest_price, price)
            profit = price - lowest_price
            max_profit = max(max_profit, profit)


        return max_profit 
