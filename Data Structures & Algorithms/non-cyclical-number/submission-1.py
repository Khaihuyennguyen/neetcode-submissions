class Solution:
    def isHappy(self, n: int) -> bool:
        def squareSum(number):
            sumSquare = 0
            while number > 0:
                currentNum = number % 10
                sumSquare += currentNum * currentNum

                number = number // 10

            return sumSquare

        first = squareSum(n)
        second = squareSum(squareSum(n))
        if first == 1 or second == 1:
                return True
        while first != second:
            if first == 1 or second == 1:
                return True
            first = squareSum(first)
            second = squareSum(squareSum(second)) 
        return False