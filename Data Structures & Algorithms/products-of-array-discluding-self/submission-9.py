class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        results = [1] * len(nums)
        current = 1
        for i in range(len(nums)):
            results[i] *= current
            current *= nums[i]
        
        current = 1
        for i in range(len(nums) -1, -1, -1):
            results[i] *= current
            current *= nums[i]
        
        return results
            
