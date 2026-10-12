class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = defaultdict(int)
        res = 0
        for num in nums:
            if not seen[num]:
                seen[num] = seen[num - 1] + 1 + seen[num + 1]
                seen[num - seen[num - 1]] = seen[num]
                seen[num + seen[num + 1]] = seen[num]
                res = max(res, seen[num])
        return res

