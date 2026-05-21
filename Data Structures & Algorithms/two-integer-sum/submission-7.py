class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # we nend to return indices
        res = {}
        for i in range(len(nums)):
            if nums[i] not in res:
                rem = target - nums[i]
                res[rem] = i
            else:
                return [res[nums[i]], i]
        return []