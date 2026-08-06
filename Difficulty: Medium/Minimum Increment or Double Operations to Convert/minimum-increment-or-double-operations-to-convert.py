class Solution:
    def countMinOperations(self, arr: list[int]) -> int:
        total_increments = 0
        max_doubles = 0
        
        for x in arr:
            if x > 0:
                
                total_increments += bin(x).count('1')
               
                max_doubles = max(max_doubles, x.bit_length() - 1)
                
        return total_increments + max_doubles