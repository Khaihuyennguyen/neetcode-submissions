class Solution:

    def encode(self, strs: List[str]) -> str:
        # at the front of each word we add the length of the wrod and special character # 
        newString = ""
        for word in strs:
            length = str(len(word))
            newword = length +"#"+word
            newString += newword
        return newString 

    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])

            i = j + 1
            j = i  + length

            res.append(s[i:j])
            i = j 
        return res
