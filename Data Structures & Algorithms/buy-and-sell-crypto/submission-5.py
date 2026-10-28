class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        l = 0
        r = l+1

        while l < r and r < len(prices):
            profit = prices[r] - prices[l]
            if profit < 0:
                l = r
                r = l+1
                continue

            max_profit = max(max_profit, profit)
            r += 1
        return max_profit
