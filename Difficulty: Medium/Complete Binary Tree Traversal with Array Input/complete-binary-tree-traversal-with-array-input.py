class Solution:
    def levelSort(self, arr):
        ans = []
        i = 0
        level_size = 1
        n = len(arr)
        
        while i < n:
            # Slice elements for the current level
            current_level = arr[i : i + level_size]
            
            # Sort the current level in ascending order
            current_level.sort()
            ans.append(current_level)
            
            # Move index forward and double the level capacity for next level
            i += level_size
            level_size *= 2
            
        return ans