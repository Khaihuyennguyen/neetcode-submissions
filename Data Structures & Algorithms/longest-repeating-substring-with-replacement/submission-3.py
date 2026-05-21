class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # l = maxC <= 5, then keep expanding
        # if not, we have to move the left too
        # think about it, the new longer strange must have even s
        count = {}
        l = 0
        maxf = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get( s[r], 0)
            maxf = max(maxf, count[s[r]])
            if r - l + 1 - maxf > k:
                count[s[l]] -= 1
                l += 1
        return r - l + 1