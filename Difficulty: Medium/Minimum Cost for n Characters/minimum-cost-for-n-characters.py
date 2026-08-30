class Solution:
    def minCost(self, n: int, i: int, d: int, c: int) -> int:
        if n <= 0:
            return 0
        dp = [0] * (n + 2)
        dp[1] = i
        for k in range(2, n + 1):
            if k % 2 == 0:
                dp[k] = min(dp[k - 1] + i, dp[k // 2] + c)
            else:
                dp[k] = min(dp[k - 1] + i, dp[(k + 1) // 2] + c + d)
            dp[k - 1] = min(dp[k - 1], dp[k] + d)
        return dp[n] 