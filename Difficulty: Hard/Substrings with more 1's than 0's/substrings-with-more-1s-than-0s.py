class Solution:
    def countSubstring(self, s: str) -> int:
        n = len(s)
       
        offset = n + 1
     
        bit = [0] * (2 * n + 2)
        
        def update(i, delta):
            i += offset
            while i < len(bit):
                bit[i] += delta
                i += i & (-i)
                
        def query(i):
            i += offset
            s = 0
            while i > 0:
                s += bit[i]
                i -= i & (-i)
            return s
        
        count = 0
        current_sum = 0
       
        update(0, 1)
        
        for char in s:
            if char == '1':
                current_sum += 1
            else:
                current_sum -= 1
            
           
            count += query(current_sum - 1)
           
            update(current_sum, 1)
            
        return count