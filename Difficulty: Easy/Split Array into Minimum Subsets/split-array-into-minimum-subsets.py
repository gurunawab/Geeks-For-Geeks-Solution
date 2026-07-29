class Solution:
    def minSubsets(self, arr):
        # Handle empty array edge case
        if not arr:
            return 0
        
        # Step 1: Sort the array in ascending order
        arr.sort()
        
        # Step 2: Initialize subset count to 1 (at least one subset exists if arr is non-empty)
        subsets = 1
        
        # Step 3: Count gaps between adjacent elements
        for i in range(1, len(arr)):
           
            if arr[i] != arr[i - 1] + 1:
                subsets += 1
                
        return subsets