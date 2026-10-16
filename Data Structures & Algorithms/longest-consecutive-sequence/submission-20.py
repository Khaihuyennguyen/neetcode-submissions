class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = defaultdict(int)

        # 1 2 3 
        # 0 1 0
        maxLength = 0
        for num in nums:
            if not seen[num]:
                seen[num] = 1 + seen[num - 1] + seen[num + 1]
                seen[num - seen[num - 1]] = seen[num]
                seen[num + seen[num + 1]] = seen[num]
                maxLength = max(maxLength, seen[num])

        return maxLength 

