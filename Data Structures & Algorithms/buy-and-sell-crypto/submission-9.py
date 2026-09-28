class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxDiff = 0
        l = 0

        for r in range(len(prices)):
            while prices[r] < prices[l]:
                l += 1
            maxDiff = max(maxDiff, prices[r] - prices[l])


        return maxDiff