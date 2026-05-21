class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}

        for i, num in enumerate(nums):
            remaining = target - num
            if remaining not in hashMap:
                hashMap[num] = i
            else:
                return [hashMap[remaining], i]
        return []