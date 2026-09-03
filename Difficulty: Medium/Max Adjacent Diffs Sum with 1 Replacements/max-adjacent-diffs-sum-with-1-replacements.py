class Solution:
    def maxDiffSum(self, arr):
        dp0, dp1 = 0, 0  # dp0: max sum ending at arr[i-1], dp1: max sum ending at 1
    
        for i in range(1, len(arr)):
            new_dp0 = max(dp0 + abs(arr[i] - arr[i-1]), dp1 + abs(arr[i] - 1))
            new_dp1 = max(dp0 + abs(1 - arr[i-1]), dp1)  # |1 - 1| = 0
            dp0, dp1 = new_dp0, new_dp1
    
        return max(dp0, dp1) 