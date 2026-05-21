class Solution:
    def isValid(self, s: str) -> bool:
        # so rule 1: they have to come in and out as in order 
        # so   if go with ) or } ... are invalid unless there is an open 
        # we should have a stack, to record the 

        # if we see the open, we store the } inside the stack
        # if we see the end, we check if the stack is not empy and it must be match with the open of its

        # we return true if the stack is empty

        hashString = {")": "(", "]": "[", "}": "{"}
        stack = []
        for string in s:
            if string in hashString:
                if stack and stack[-1] == hashString[string]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(string)
        return  not stack 
