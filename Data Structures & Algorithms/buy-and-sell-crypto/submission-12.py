class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        maxRevenue = 0
        for r in range(len(prices)):
            if prices[r] < prices[l]:
                l = r
            maxRevenue = max(maxRevenue, prices[r] - prices[l])
        return maxRevenue