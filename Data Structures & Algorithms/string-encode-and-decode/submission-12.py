class Solution:
    # 6#string
    def encode(self, strs: List[str]) -> str:
        string = ''

        for s in strs:
            length = len(s)
            string += str(length) + '#' + s
        return string

    def decode(self, s: str) -> List[str]:
        res = []
        
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length

            res.append(s[i:j])
            i = j
        return res


