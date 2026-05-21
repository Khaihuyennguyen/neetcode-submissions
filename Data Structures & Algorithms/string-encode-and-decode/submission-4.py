class Solution:

    def encode(self, strs: List[str]) -> str:
        dataString = ""

        for s in strs:
            dataString += str(len(s)) + "~" + s
        return dataString

    def decode(self, s: str) -> List[str]:
        index = 0
        # 10~khainguyen
        # i r
        rightIndex = 0
        res = []
        while index < len(s):
            rightIndex = index
            while s[rightIndex] != "~":
                rightIndex += 1
            length = int(s[index:rightIndex])
            index = rightIndex + 1
            rightIndex = index + length
            res.append(s[index: rightIndex])
            index = rightIndex
        return res
        

