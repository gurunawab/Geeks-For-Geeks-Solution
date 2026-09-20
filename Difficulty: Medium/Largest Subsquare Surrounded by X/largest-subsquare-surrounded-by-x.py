class Solution:
    def largestSubsquare(self, mat: list[list[str]]) -> int:
        n, ans = len(mat), 0
        h = [[0] * (n + 1) for _ in range(n + 1)]
        v = [[0] * (n + 1) for _ in range(n + 1)]

        for r in range(n):
            for c in range(n):
                if mat[r][c] == 'X':
                    h[r + 1][c + 1] = h[r + 1][c] + 1
                    v[r + 1][c + 1] = v[r][c + 1] + 1

                    for k in range(min(h[r + 1][c + 1], v[r + 1][c + 1]), ans, -1):
                        if h[r - k + 2][c + 1] >= k and v[r + 1][c - k + 2] >= k:
                            ans = k
                            break
        return ans