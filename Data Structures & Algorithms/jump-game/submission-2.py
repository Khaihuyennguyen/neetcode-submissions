class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # we set the goal is the index
        # if index - 1 + nums[index - 1] == goal we set the new goal is the current index - 1


        # in the end if the index is not 0 we return false

        goal = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        
        return goal == 0