class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = defaultdict(list)
        for s in strs:
            key = [0] * 26
            for w in s:
                key[ord(w) - ord('a')] += 1
            
            hashMap[tuple(key)].append(s)
        return list(hashMap.values())


