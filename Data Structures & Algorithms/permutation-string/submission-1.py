class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        
        s1Count = [0] * 26
        s2Count = [0] * 26

        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord("a")] += 1
            s2Count[ord(s2[i]) - ord("a")] += 1

        matches = sum ( 1 for i in range(26) if s1Count[i] == s2Count[i])

        l = 0

        def update(index, change):
            nonlocal matches

            # was this character matching before 
            before = s1Count[index] == s2Count[index]

            s2Count[index] += change

            after = s1Count[index] == s2Count[index]

            if before and not after:
                matches -= 1
            elif not before and after:
                matches += 1
            

        for r in range(len(s1), len(s2)):
            if matches == 26: return True

            update(ord(s2[r]) - ord("a"), 1 )
            update(ord(s2[l]) - ord("a"), -1 )
            l += 1
        return matches == 26

       