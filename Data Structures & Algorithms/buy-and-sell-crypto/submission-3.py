class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        l = 0
        r = 1
        while r < len(prices):
            cur_profit = prices[r] - prices[l]
            if cur_profit <= 0:
                l = r
            else:
                max_profit = max(max_profit, cur_profit)          
            
            r += 1
            
        return max_profit