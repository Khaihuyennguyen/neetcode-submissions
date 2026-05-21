class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # { }}
        # key: leeter
        # value is the index:
        # z z y z x y z
        # t m m z u x t     
        #     l   

        mp = {}
        res = 0
        l = 0
        for r in range(len(s)):
            if s[r] in mp:
                l = max(l, mp[s[r]] + 1)
            mp[s[r]] = r
            res = max(r - l + 1, res)

        return res       