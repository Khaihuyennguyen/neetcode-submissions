class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # if we know the most repeating string in that sub
        # len - most if == k: we satisfy the condition 1
        # if we keep expanding the substring with the condtion
        # keep tract of what is the most repeating 
        # then take the max if it is\
        # if not, increate the lft bpundary and decreaste the count

        hashMap = {}
        maxf = 0
        res = 0
        l = 0
        for r in range(len(s)):
            hashMap[s[r]] = 1 + hashMap.get(s[r], 0)
            maxf = max(maxf, hashMap[s[r]])

            while r - l + 1 - maxf > k:
                hashMap[s[l]] -= 1
                l += 1
 
            res = max(res, r - l + 1)

        return res