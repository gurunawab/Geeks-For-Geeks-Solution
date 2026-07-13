import math

class Solution:
    def minOperations(self, b: list[int]) -> int:
        n = len(b)
        MOD = 10**9 + 7
        
        # 1. Find all cycle lengths
        visited = [False] * n
        cycle_lengths = []
        
        for i in range(n):
            if not visited[i]:
                length = 0
                curr = i
                while not visited[curr]:
                    visited[curr] = True
                    # b has 1-based indexing, convert to 0-based
                    curr = b[curr] - 1
                    length += 1
                cycle_lengths.append(length)
        
        # 2. Track the maximum power of each prime factor across all cycles
        max_prime_powers = {}
        
        for length in cycle_lengths:
            temp = length
            d = 2
            while d * d <= temp:
                if temp % d == 0:
                    count = 0
                    while temp % d == 0:
                        count += 1
                        temp //= d
                    max_prime_powers[d] = max(max_prime_powers.get(d, 0), count)
                d += 1
            if temp > 1:
                max_prime_powers[temp] = max(max_prime_powers.get(temp, 0), 1)
        
        # 3. Calculate the LCM modulo 10^9 + 7
        ans = 1
        for prime, power in max_prime_powers.items():
            ans = (ans * pow(prime, power, MOD)) % MOD
            
        return ans
        