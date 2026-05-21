class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answers = [1] * len(nums)
        sufix = 1
        for i in range(1, len(nums)):
            answers[i] = answers[i-1] * nums[i-1]

        for i in range(len(nums) - 1, -1, -1):
            answers[i] *= sufix
            sufix *= nums[i]

        return answers