class Solution:
    def maxDiffSubArrays(self, arr):
        n = len(arr)
        
       
        left_max = [0] * n
        left_min = [0] * n
        
        
        current_max = current_min = arr[0]
        left_max[0] = left_min[0] = arr[0]
        
        for i in range(1, n):
            current_max = max(arr[i], current_max + arr[i])
            left_max[i] = max(left_max[i - 1], current_max)
            
            current_min = min(arr[i], current_min + arr[i])
            left_min[i] = min(left_min[i - 1], current_min)
            
       
        right_max = [0] * n
        right_min = [0] * n
        
        
        current_max = current_min = arr[n - 1]
        right_max[n - 1] = right_min[n - 1] = arr[n - 1]
        
        for i in range(n - 2, -1, -1):
            current_max = max(arr[i], current_max + arr[i])
            right_max[i] = max(right_max[i + 1], current_max)
            
            current_min = min(arr[i], current_min + arr[i])
            right_min[i] = min(right_min[i + 1], current_min)
            
        
        max_diff = 0
        for i in range(n - 1):
            diff1 = abs(left_max[i] - right_min[i + 1])
            diff2 = abs(left_min[i] - right_max[i + 1])
            max_diff = max(max_diff, diff1, diff2)
            
        return max_diff