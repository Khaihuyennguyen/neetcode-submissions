class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        remaining = {} # where key is the remaining and value is the index

        for i in range(len(nums)):
            num = nums[i]
            if num in remaining:
                return [remaining[num], i]
            remaining[target - num] = i

        return []