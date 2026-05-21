class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))

    def helper(self, nums: List[int]) -> int:
        # 1 2 3 4 

        rob1, rob2 = 0 , 0
        res = 0

        for i in nums:
            rob1, rob2 = rob2, max(rob1 + i, rob2)

        return rob2
