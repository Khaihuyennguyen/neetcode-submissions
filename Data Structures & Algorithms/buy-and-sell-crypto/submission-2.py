class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # we keep track of current Max value and ith value
        l = 0
        currentMax = 0
        for r in range(1,len(prices)):
            if prices[r] < prices[l]:
                l = r
            currentMax = max(currentMax, prices[r] - prices[l])
        


        return currentMax