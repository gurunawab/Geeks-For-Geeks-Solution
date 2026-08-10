class Solution:

    def largestSquare(
        self, mat: list[list[int]], queries: list[list[int]], k: int
    ) -> list[int]:
        n, m = len(mat), len(mat[0])

   
        P = [[0] * (m + 1) for _ in range(n + 1)]
        for r in range(n):
            for c in range(m):
                P[r + 1][c + 1] = (
                    mat[r][c] + P[r][c + 1] + P[r + 1][c] - P[r][c]
                )

        ans = []
        for r, c in queries:
         
            lo, hi, best = 0, min(r, n - 1 - r, c, m - 1 - c), -1
            while lo <= hi:
                d = (lo + hi) // 2
                ones = (
                    P[r + d + 1][c + d + 1]
                    - P[r - d][c + d + 1]
                    - P[r + d + 1][c - d]
                    + P[r - d][c - d]
                )

                if ones <= k:
                    best = d
                    lo = d + 1
                else:
                    hi = d - 1

            ans.append(2 * best + 1 if best != -1 else -1)

        return ans