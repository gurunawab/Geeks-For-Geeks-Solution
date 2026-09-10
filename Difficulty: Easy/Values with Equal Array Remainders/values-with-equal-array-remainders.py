import math

class Solution:
    def sameMod(self, arr):
       
        g = 0
        for x in arr:
            g = math.gcd(g, abs(x - arr[0]))

       
        if g == 0:
            return -1

        
        divisors = sum(2 for i in range(1, int(math.isqrt(g)) + 1) if g % i == 0)
        return divisors - (1 if math.isqrt(g) ** 2 == g else 0)