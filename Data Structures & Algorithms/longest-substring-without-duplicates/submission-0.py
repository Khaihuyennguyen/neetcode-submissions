class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        showWords = set()

        l = 0
        maxLength = 0
        for r in range(len(s)):
            while s[r] in showWords:
                showWords.remove(s[l])
                l += 1
            maxLength = max(maxLength, r - l + 1)
            showWords.add(s[r])
        return maxLength