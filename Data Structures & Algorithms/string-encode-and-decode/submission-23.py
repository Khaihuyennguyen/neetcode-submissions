class Solution:

    def encode(self, strs: List[str]) -> str:
        result = []

        for i in range(len(strs)):
            result.append(str(len(strs[i])))
            result.append("#")
            result.append(strs[i])
        return "".join(result)

    def decode(self, s: str) -> List[str]:
        result = []

        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            # 0 1 2 3 4 
            # 3 # h h e 
            length = int(s[i:j])
            i = j+1
            j = i + length
            c = s[i:j]
            result.append(c)

            i = j
        return result
