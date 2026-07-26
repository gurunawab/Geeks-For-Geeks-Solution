class Solution:
    def levelSort(self, arr):
        ans = []
        i = 0
        level_size = 1
        n = len(arr)
        
        while i < n:
           
            current_level = arr[i : i + level_size]
            
            
            current_level.sort()
            ans.append(current_level)
            
           
            i += level_size
            level_size *= 2
            
        return ans