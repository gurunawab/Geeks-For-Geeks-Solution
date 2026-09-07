class Solution:
    def searchWord(self, mat, word):
        n, m, L = len(mat), len(mat[0]), len(word)
        dirs = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
        ans = []

        for r in range(n):
            for c in range(m):
                if mat[r][c] != word[0]:
                    continue
                for dr, dc in dirs:
                    if 0 <= r + (L - 1) * dr < n and 0 <= c + (L - 1) * dc < m:
                        if all(mat[r + k * dr][c + k * dc] == word[k] for k in range(1, L)):
                            ans.append([r, c])
                            break

        return ans