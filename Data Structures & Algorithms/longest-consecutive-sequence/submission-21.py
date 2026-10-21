class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = defaultdict(int)

        # 2 3 4 5  10 20 
        # 3 3 3 0  1  1
        longest = 0
        for num in nums:
            if  not seen[num]:
                seen[num] = 1 + seen[num-1] + seen[num+1]
                seen[num - seen[num-1]] = seen[num]
                seen[num + seen[num+1]] = seen[num]

            longest = max(longest, seen[num])

        return longest