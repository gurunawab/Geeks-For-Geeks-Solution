class Solution:
    def count(self, n: int, m: int) -> int:
        neighbors = {i : [] for i in range(1, m + 1)}
        for i in range(1, m + 1):
            for j in range(1, m + 1):
                if i % j == 0 or j % i == 0:
                    neighbors[i].append(j)
                    
        dp = [1] * (m + 1)
        
        for _ in range(2, n + 1):
            next_dp = [0] * (m + 1)
            for curr in range(1, m + 1):
                next_dp[curr] = sum(dp[prev] for prev in neighbors[curr])
            dp = next_dp
            
        return sum(dp[1:])    
        