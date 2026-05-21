class Solution:
    def isHappy(self, n: int) -> bool:
        def squareSum(n):
            output = 0

            while n :
                output += (n%10) ** 2
                n = n // 10
            return output
        
        slow = n
        fast = squareSum(n)

        while fast!= slow:
            fast = squareSum(fast)
            fast = squareSum(fast)
            slow = squareSum(slow)
        

        return True if fast == 1 else False
        

