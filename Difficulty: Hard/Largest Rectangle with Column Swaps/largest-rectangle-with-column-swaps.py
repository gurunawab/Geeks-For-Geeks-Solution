class Solution:

    def maxArea(self, mat: list[list[int]]) -> int:
        n, m = len(mat), len(mat[0])
    
       
        for r in range(1, n):
            for c in range(m):
                if mat[r][c]:
                    mat[r][c] += mat[r - 1][c]
    
       
        ans = 0
        for row in mat:
            row.sort(reverse=True)
            for k, h in enumerate(row):
                ans = max(ans, h * (k + 1))
    
        return ans 