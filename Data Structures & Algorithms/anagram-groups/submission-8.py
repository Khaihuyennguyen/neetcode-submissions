class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for word in strs:
            series = [0] * 26
            for l in word:
                series[ord(l) - ord('a')] += 1
            res[tuple(series)].append(word)
        return list(res.values())
                