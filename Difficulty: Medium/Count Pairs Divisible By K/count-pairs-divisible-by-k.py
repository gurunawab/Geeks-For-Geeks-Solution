class Solution:
    def countKdivPairs(self, arr, k):
      
        remainder_counts = [0] * k
        for num in arr:
            remainder_counts[num % k] += 1
        
        count = 0
        
        
        n = remainder_counts[0]
        count += (n * (n - 1)) // 2
        
        
        for r in range(1, (k // 2) + 1):
            if r == k - r: 
                n = remainder_counts[r]
                count += (n * (n - 1)) // 2
            else:
                count += remainder_counts[r] * remainder_counts[k - r]
                
        return count