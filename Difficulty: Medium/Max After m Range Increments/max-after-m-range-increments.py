class Solution:
    def findMax(self, n, a, b, k):
        
        diff = [0] * (n + 1)
        
        
        for i in range(len(a)):
            start = a[i]
            end = b[i]
            val = k[i]
            
            diff[start] += val
            diff[end + 1] -= val
        
        
        max_val = 0
        current_sum = 0
        
        for i in range(n):
            current_sum += diff[i]
            if current_sum > max_val:
                max_val = current_sum
                
        return max_val