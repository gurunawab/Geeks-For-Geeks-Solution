class Solution:
    def findMinCost(self, s1: str, s2: str, costS1: int, costS2: int) -> int:
        n, m = len(s1), len(s2)
        dp = [0] * (m + 1)

        for c1 in s1:
            prev = 0
            for j, c2 in enumerate(s2, 1):
                temp = dp[j]
                dp[j] = prev + 1 if c1 == c2 else max(dp[j], dp[j - 1])
                prev = temp

        lcs = dp[m]
        return (n - lcs) * costS1 + (m - lcs) * costS2