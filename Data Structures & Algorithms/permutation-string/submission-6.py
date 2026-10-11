class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        countS1 = [0] * 26
        countS2 = [0] * 26
        if len(s2) < len(s1): return False
        for i in range(len(s1)):
            countS1[ord(s1[i]) - ord("a")] += 1
            countS2[ord(s2[i]) - ord("a")] += 1
        l = 0
        for i in range(len(s1), len(s2)):
            if countS1 == countS2: return True

            countS2[ord(s2[l]) - ord("a")] -= 1
            countS2[ord(s2[i]) - ord("a")] += 1
            l += 1


        return countS1 == countS2