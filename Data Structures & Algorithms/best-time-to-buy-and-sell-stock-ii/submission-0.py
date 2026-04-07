class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        profit = 0
        for i in range(len(prices)-1):
            profit = prices[i+1] - prices[i]
            if profit < 0:
                profit = 0
            res += profit
        return res

