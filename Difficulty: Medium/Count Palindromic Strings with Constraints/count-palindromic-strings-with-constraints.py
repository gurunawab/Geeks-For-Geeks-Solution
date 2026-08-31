import math

class Solution:
    def palindromicStrings(self, n: int, k: int) -> int:
        MOD = 10**9 + 7
        return sum(math.perm(k, (L + 1) // 2) for L in range(1, n + 1)) % MOD 