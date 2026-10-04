class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        results = [1] * len(nums) 

        product = 1

        for i in range(len(nums)):
            results[i] *= product
            product *= nums[i]
        product = 1
        for i in range(len(nums) - 1, -1 , -1):
            results[i] *= product
            product *= nums[i]
        return results