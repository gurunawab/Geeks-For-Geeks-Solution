class Solution:
    def countSubsequences(self, s: str, n: int) -> int:
        MOD = 10**9 + 7
        dp = [0] * n
        dp[0] = 1  
    
        for char in s:
            digit = int(char)
            next_dp = list(dp)
            for r in range(n):
                if dp[r]:
                    new_r = (r * 10 + digit) % n
                    next_dp[new_r] = (next_dp[new_r] + dp[r]) % MOD
            dp = next_dp
    
        
        return (dp[0] - 1) % MOD 