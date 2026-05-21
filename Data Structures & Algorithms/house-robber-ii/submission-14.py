class Solution:
    def rob(self, nums: List[int]) -> int:
        # 1 2 3 4
        #     x
        # max(3 + 1, 2)
        # update the prev = curr
        # and the curr = max
        
        return max(nums[0], self.helper(nums[1:]),
                            self.helper(nums[:-1]))

    def helper(self, nums):
        prevRob = currRob = 0

        for i in range(len(nums)):
            currRob, prevRob = max(currRob, nums[i] + prevRob), currRob
        return currRob
            