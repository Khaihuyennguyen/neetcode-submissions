class Solution:
    def longestPalindrome(self, s: str) -> str:
        # find the substring that is palindrome first
        # we keep track of the length


        # abbd
        #  ij i    3
        if len(s) == 1:
            return s
        resLength = 0
        longestSubString = ""
        def validPalindrome(i,j):
            l, r = i, j

            while l >= 0 and r < len(s) and s[l] == s[r]:
                nonlocal resLength
                nonlocal longestSubString
                if r - l + 1 >= resLength:
                    resLength = r - l + 1
                    longestSubString = s[l:r+1]
                l -= 1
                r += 1

        for i in range(len(s)):
            validPalindrome(i, i)
            validPalindrome(i, i + 1)

        return longestSubString