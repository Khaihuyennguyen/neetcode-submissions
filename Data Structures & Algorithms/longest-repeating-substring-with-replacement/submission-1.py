class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        countS = {} # we counts the freq of the current letter
        # if we take the currentLength - max(currenters)  > k not good
        # so, we have to update the currentLengt => 2 pointers

        # 
        left = 0
        maxCount = 0
        maxChars = 0
        for right in range(len(s)):
            countS[s[right]] = 1 + countS.get(s[right], 0)
            maxChars = max(maxChars, countS[s[right]])
            while right - left + 1 - maxChars > k:
                countS[s[left]] -= 1
                left += 1
            maxCount = max(maxCount, right - left + 1)
        return maxCount
