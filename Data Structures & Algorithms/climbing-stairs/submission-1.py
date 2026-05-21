class Solution:
    def climbStairs(self, n: int) -> int:
        # n = 2

        # 1 2 3 
        # x x X: 3
        #   x x: first
        #   x X: second stop

        curr, prev = 1, 1
        for i in range(n - 1): 
            prev, curr = curr, curr + prev

        return curr