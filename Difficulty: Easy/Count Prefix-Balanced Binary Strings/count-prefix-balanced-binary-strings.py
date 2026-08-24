import math


class Solution:

    def prefixStrings(self, n: int) -> int:
        # The number of valid strings is the n-th Catalan number: C(2n, n) // (n + 1)
        return (math.comb(2 * n, n) // (n + 1)) % (10**9 + 7) 