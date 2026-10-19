class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        fre = defaultdict(list)

        for s in strs:
            count = 29 * [0]

            for i in range(len(s)):
                count[ord(s[i]) - ord("a")] += 1
            fre[tuple(count)].append(s)

        return list(fre.values())