class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        l = 0
        totalSum = 0
        maxSum = nums[0]
        for r in range(len(nums)):
            totalSum += nums[r]
            maxSum = max(maxSum,  totalSum)
            if totalSum < 0:
                totalSum = 0
        return maxSum