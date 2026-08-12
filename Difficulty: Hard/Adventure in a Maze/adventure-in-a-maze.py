class Solution:

    def findWays(self, grid):
        n, MOD = len(grid), 10**9 + 7
        paths = [[0] * n for _ in range(n)]
        adv = [[0] * n for _ in range(n)]
        paths[0][0], adv[0][0] = 1, grid[0][0]

        for i in range(n):
            for j in range(n):
                if not paths[i][j]:
                    continue
                # Move Right (1 or 3)
                if j + 1 < n and grid[i][j] in (1, 3):
                    paths[i][j + 1] = (paths[i][j + 1] + paths[i][j]) % MOD
                    adv[i][j + 1] = max(
                        adv[i][j + 1], adv[i][j] + grid[i][j + 1]
                    )
                # Move Down (2 or 3)
                if i + 1 < n and grid[i][j] in (2, 3):
                    paths[i + 1][j] = (paths[i + 1][j] + paths[i][j]) % MOD
                    adv[i + 1][j] = max(
                        adv[i + 1][j], adv[i][j] + grid[i + 1][j]
                    )

        return [paths[-1][-1], adv[-1][-1] if paths[-1][-1] else 0]