class Solution:
    def largestArea(self, n, m, arr):
    
        blocked_rows = [0, n + 1]
        blocked_cols = [0, m + 1]
        
      
        for r, c in arr:
            blocked_rows.append(r)
            blocked_cols.append(c)
            
       
        blocked_rows.sort()
        blocked_cols.sort()
        
       
        max_row_gap = 0
        for i in range(len(blocked_rows) - 1):
            max_row_gap = max(max_row_gap, blocked_rows[i+1] - blocked_rows[i] - 1)
            
       
        max_col_gap = 0
        for i in range(len(blocked_cols) - 1):
            max_col_gap = max(max_col_gap, blocked_cols[i+1] - blocked_cols[i] - 1)
            
      
        return max_row_gap * max_col_gap
        