class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)

        dp[0] = 0

        for currentAmount in range(1, amount + 1):
            for coinValue in coins:
                if currentAmount >= coinValue:
                    dp[currentAmount] = min(1 + dp[currentAmount - coinValue], dp[currentAmount])
        return dp[amount] if dp[amount] != amount + 1 else -1