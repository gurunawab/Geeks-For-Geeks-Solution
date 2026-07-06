class Solution:
    def maxPathSum(self, a, b):
        i, j = 0, 0
        sumA, sumB = 0, 0
        total_sum = 0
        
        while i < len(a) and j < len(b):
            if a[i] < b[j]:
                sumA += a[i]
                i += 1
            elif a[i] > b[j]:
                sumB += b[j]
                j += 1
            else: 
                total_sum += max(sumA, sumB) + a[i]
                sumA, sumB = 0, 0
                i += 1
                j += 1
        
       
        while i < len(a):
            sumA += a[i]
            i += 1
        while j < len(b):
            sumB += b[j]
            j += 1
            
        total_sum += max(sumA, sumB)
        return total_sum
        