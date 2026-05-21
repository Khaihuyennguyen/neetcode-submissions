class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # 12 = 10 + 1 + 1 (3)
        # 0: 0
        # 1: 1
        # 2: 1 + DP[2 - 1] = 2
        # 3: 1 + DP[3 - 1], = 3
        # 5: 1 + DP[5 - 5] 1
        # Means that: we have a for loop that go from 1 to amount + 1
        #  dp[i] = min(1 + dp[a - c], dp[i])    if a - c > 0

        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for i in range(1, amount + 1):
            for c in coins:
                if i - c >= 0:
                    dp[i] = min(dp[i], 1 + dp[i - c])
        return dp[amount] if dp[amount] != amount + 1 else -1

