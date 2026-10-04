class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # we  count the frequencies of each letter
        # convert that into some kind of key so we can group them later
        fre = defaultdict(list)
        for s in strs:
            count = [0] * 29
            for c in s:
                count[ord(c) - ord('a')] += 1
            k = tuple(count)
            fre[k].append(s)

        return list(fre.values())
