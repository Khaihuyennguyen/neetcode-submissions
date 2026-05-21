class Solution:
    def rob(self, nums: List[int]) -> int:
        # sum of all the amount that meet the condition
        # two house could not be rob at the same time 
        # 1   2   3      4
        # max max curr  
        previousRob, currentRob = 0, 0

        for num in nums:
            currentRob, previousRob = max(currentRob, previousRob + num)   , currentRob
        return currentRob