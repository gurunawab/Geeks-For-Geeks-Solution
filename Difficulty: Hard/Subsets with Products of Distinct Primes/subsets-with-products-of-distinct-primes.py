from collections import Counter

class Solution:
    def countSubsets(self, arr):
        MOD = 10**9 + 7
        
       
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        num_primes = len(primes)
        
        
        prime_mask = {}
        for num in range(2, 31):
            temp = num
            mask = 0
            is_square_free = True
            
            for i, p in enumerate(primes):
                if temp % p == 0:
                    count = 0
                    while temp % p == 0:
                        count += 1
                        temp //= p
                    if count > 1:
                        is_square_free = False
                        break
                    mask |= (1 << i)
                    
            if is_square_free:
                prime_mask[num] = mask

        freq = Counter(arr)
        
        
        dp = [0] * (1 << num_primes)
        dp[0] = 1  
        
     
        for num, count in freq.items():
            if num in prime_mask:
                mask = prime_mask[num]
                
                for i in range((1 << num_primes) - 1, -1, -1):
                    if (i & mask) == 0:
                        dp[i | mask] = (dp[i | mask] + dp[i] * count) % MOD
                        
        
        valid_non_ones = sum(dp[1:]) % MOD
        
       
        num_ones = freq[1]
        pow_ones = pow(2, num_ones, MOD)
        
        return (valid_non_ones * pow_ones) % MOD