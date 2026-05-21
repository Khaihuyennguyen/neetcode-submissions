class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        

        maxSub = nums[0]
        currentSum = 0
        for i in range(len(nums)):
            currentSum += nums[i]
            maxSub = max(maxSub, currentSum)
            if currentSum < 0: 
                currentSum = 0
            

        return maxSub
            