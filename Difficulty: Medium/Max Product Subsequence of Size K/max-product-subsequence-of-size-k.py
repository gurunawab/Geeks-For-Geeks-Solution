class Solution:

    def maxProduct(self, arr: list[int], k: int) -> int:
        dp = {0: (1, 1)}  # count: (min_prod, max_prod)

        for x in arr:
            for count in range(min(k - 1, len(dp) - 1), -1, -1):
                if count in dp:
                    mn, mx = dp[count]
                    cands = [mn * x, mx * x]
                    if count + 1 in dp:
                        cands += list(dp[count + 1])
                    dp[count + 1] = (min(cands), max(cands))

        return dp[k][1]