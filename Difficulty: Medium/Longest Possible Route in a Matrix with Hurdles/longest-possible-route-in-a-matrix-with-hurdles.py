class Solution:
    def longestPath(self, mat, xs, ys, xd, yd):
        n = len(mat)
        m = len(mat[0])
        self.max_len = -1
        
        def solve(r, c, current_dist):
           
            if r < 0 or r >= n or c < 0 or c >= m or mat[r][c] == 0:
                return
            
          
            if r == xd and c == yd:
                self.max_len = max(self.max_len, current_dist)
                return
            
            
            temp = mat[r][c]
            mat[r][c] = 0
            
          
            solve(r + 1, c, current_dist + 1)
            solve(r - 1, c, current_dist + 1)
            solve(r, c + 1, current_dist + 1)
            solve(r, c - 1, current_dist + 1)
            
            
            mat[r][c] = temp
            
        
        if mat[xs][ys] == 1:
            solve(xs, ys, 0)
            
        return self.max_len
        