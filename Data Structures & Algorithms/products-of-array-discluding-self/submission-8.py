class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 1 2 4 6
        # if we have  -> < -
        prefix = 1
        posfix  = 1
        res = [1] * len(nums)
        for i in range(len(nums)):
            res[i] *= prefix 
            prefix *= nums[i] 
        
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= posfix
            posfix *= nums[i]

        return res