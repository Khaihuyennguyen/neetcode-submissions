class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        f1, f2 = {}, {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            f1[s[i]] = 1 + f1.get(s[i], 0)
            f2[t[i]] = 1 + f2.get(t[i], 0)

        return f1 == f2