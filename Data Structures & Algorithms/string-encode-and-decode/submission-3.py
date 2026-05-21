class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            result += str(len(s)) + "#" + s
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        index = 0

        while index < len(s):
            right_index = index
            while s[right_index] != "#":
                right_index += 1
            length = int(s[index:right_index])
            # update to get real string
            index = right_index + 1
            right_index = index + length
            result.append(s[index:right_index])
            index = right_index
        return result

