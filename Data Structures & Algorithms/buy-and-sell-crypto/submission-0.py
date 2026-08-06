class Solution:
    def maxProfit(self, prices: List[int]) -> int:


        max_profit = 0
        lp = 0
        for rp in range(1,len(prices)):
            if prices[rp] < prices[lp]:
                lp = rp
            else:
                max_profit = max(max_profit, prices[rp]- prices[lp])
    
        return max_profit