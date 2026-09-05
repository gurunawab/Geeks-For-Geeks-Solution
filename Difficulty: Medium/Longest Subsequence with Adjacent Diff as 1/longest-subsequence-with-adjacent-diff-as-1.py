class Solution:
    def longestSubseq(self, arr):
        dp = {}
        for x in arr:
            dp[x] = 1 + max(dp.get(x - 1, 0), dp.get(x + 1, 0))
        return max(dp.values(), default=0) 