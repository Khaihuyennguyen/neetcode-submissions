class Solution:
    def climbStairs(self, n: int) -> int:
        # are the top at the staris
        # current position will be either the n - 1 step
        # and n - 2 step

        step1, step2 = 1, 1

        for i in range(n - 1):
            step1, step2 = step1 + step2, step1
        return step1