class Solution:
    def isValid(self, s: str) -> bool:
        hashMap = {'(': ')', '{': '}', '[' : ']'}
        heap = []


        for c in s:
            if c in hashMap:
                heap.append(hashMap[c])
            else:
                if  heap and heap[-1] == c:
                    heap.pop()
                else:
                    return False
        return True if not heap else False

