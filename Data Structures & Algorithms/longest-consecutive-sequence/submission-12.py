class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #    1 2 3 4 5 6   10
        #    0 4 3 3 4 0

        mp = defaultdict(int)
        res = 0

        for num in nums:
            if not mp[num]:
                mp[num] = 1 + mp[num - 1] + mp[num + 1]
                mp[num - mp[num - 1]] = mp[num]
                mp[num + mp[num + 1]] = mp[num]
        
            res = max(res, mp[num])
        return res