class Solution:
    def getCount(self, n):
        count = 0
        k = 2
        
       
        while (k * (k + 1)) // 2 <= n:
           
            if (2 * n) % k == 0:
                val = (2 * n) // k - k + 1
                if val > 0 and val % 2 == 0:
                    count += 1
            k += 1
            
        return count