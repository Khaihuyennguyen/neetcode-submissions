class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq = defaultdict(list)

        # 
        count = [0] * 27

        for s in strs:
            count = [0] * 27
            for c in s:
                count[ord(c) - ord('a')] += 1
           

            freq[tuple(count)].append(s)
        
        return list(freq.values())


