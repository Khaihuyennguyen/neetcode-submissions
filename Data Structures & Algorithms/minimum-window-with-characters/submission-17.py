class Solution:
    def minWindow(self, s: str, t: str) -> str:
        fre_t = {}
        for i in range(len(t)):
            fre_t[t[i]] = fre_t.get(t[i], 0) + 1
        fre = {}
        need = len(fre_t)
        have = 0
        l = 0
        shortest = float("inf")
        results = [-1, -1]
        for r in range(len(s)):
            c = s[r]

            if c in fre_t:
                fre[c] = 1 + fre.get(c, 0)
                if fre[c] == fre_t[c]:
                    have += 1
            
            while need == have:
                if shortest > r - l + 1:
                    shortest = r - l + 1
                    results = [l, r]
                if s[l] in fre_t:
                    fre[s[l]] -= 1
                    if fre[s[l]] < fre_t[s[l]]:
                        have -= 1
                l += 1

        return s[results[0]: results[1] + 1] if shortest != float("inf") else ""


            