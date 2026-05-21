class Solution:
    def isValid(self, s: str) -> bool:
        heap = []
        mp = {'(': ')', '{' : '}', '[' : ']'}

        for l in s:
            if l in mp:
                heap.append(mp[l])
            else:
                if heap and heap[-1] == l:
                    heap.pop()
                else:
                    return False
        return len(heap) == 0