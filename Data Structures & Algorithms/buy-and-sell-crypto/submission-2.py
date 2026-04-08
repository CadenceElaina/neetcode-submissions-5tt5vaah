class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        min_v = float("inf")
        l = 0
        max_p = float("-inf")

        for i, p in enumerate(prices):
            #profit = sell - buy
            if p < min_v:
                min_v = p
            profit = p - min_v
            if profit > 0:
                max_p = max(max_p, profit)
        if max_p <= 0:
            return 0        
        return max_p