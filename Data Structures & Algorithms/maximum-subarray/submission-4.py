class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Let's see the first example
        # []
        maxSum = nums[0]
        currentSum = 0
        for n in nums:
            if n > currentSum + n:
                currentSum = 0
            currentSum += n

            maxSum = max(maxSum, currentSum)
        return maxSum