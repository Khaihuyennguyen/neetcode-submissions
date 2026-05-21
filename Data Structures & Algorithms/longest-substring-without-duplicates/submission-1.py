class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # we use a set to store the characters 
        # we go through the lenght of the string: find if 

        mp = {}
        l = 0
        res = 0

        for r in range(len(s)):
            if s[r] in mp:
                l = max(mp[s[r]] + 1, l)
            mp[s[r]] = r
            res = max(res, r - l + 1)
        return res