class Solution:
    def find(self, arr):
       
        x = 0
        
        
        for a in reversed(arr):
           
            x = (x + a + 1) // 2
            
        return x