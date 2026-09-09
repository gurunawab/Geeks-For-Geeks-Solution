class Solution:
    def pairCount(self, x, y):
        if y % x != 0:
            return 0
        n, p = y // x, 2
        k = 0
        while p * p <= n:
            if n % p == 0:
                k += 1
                while n % p == 0:
                    n //= p
            p += 1
        if n > 1:
            k += 1
        return 1 << k