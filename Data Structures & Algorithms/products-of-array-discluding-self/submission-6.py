class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        preFix = 1
        postFix = 1
        product = [1] * (len(nums))

        for i in range(len(nums)):
            product[i] *= preFix
            preFix *= nums[i]
        
        for i in range(len(nums) - 1, -1, -1):
            product[i] *= postFix
            postFix *= nums[i]

        return product
        