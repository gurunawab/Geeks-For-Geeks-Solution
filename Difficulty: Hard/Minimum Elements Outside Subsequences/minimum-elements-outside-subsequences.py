class Solution:

    def minCount(self, arr: list[int]) -> int:
        n = len(arr)
       
        dp = {(-1, float("inf")): 0}

        for x in arr:
            next_dp = dict(dp)
            for (inc, dec), count in dp.items():
                # Option 1: Append to strictly increasing subsequence
                if x > inc:
                    key = (x, dec)
                    next_dp[key] = max(next_dp.get(key, 0), count + 1)
                # Option 2: Append to strictly decreasing subsequence
                if x < dec:
                    key = (inc, x)
                    next_dp[key] = max(next_dp.get(key, 0), count + 1)
            dp = next_dp

        return n - max(dp.values())