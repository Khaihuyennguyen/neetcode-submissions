class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        numberStack = []
        for token in tokens:
            if token == "+":
                res = numberStack.pop() + numberStack.pop()
                numberStack.append(res)
            elif token == "*":
                res = numberStack.pop() * numberStack.pop()
                numberStack.append(res)
            elif token == "-":
                a , b = numberStack.pop(), numberStack.pop()
                res = b - a
                numberStack.append(res)
            elif token == "/":
                a , b = numberStack.pop(), numberStack.pop()
                numberStack.append(int(float(b)/ a))
            else:
                
                numberStack.append(int(token))
        return numberStack[0]