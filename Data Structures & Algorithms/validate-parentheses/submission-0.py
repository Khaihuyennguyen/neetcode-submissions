class Solution:
    def isValid(self, s: str) -> bool:
        pars = {'(': ')', '{': '}', '[' : ']'}
        stack = []
        for c in s:
            if c in pars:
                stack.append(pars[c])
            elif not stack or stack[-1] != c:
                return False
            else:
                stack.pop()
        return len(stack) == 0

