class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        fre_s, fre_t = {}, {}

        for i in range(len(s)):
            fre_s[s[i]] = 1 + fre_s.get(s[i], 0)
            fre_t[t[i]] = 1 + fre_t.get(t[i], 0)
        
        return fre_t == fre_s
