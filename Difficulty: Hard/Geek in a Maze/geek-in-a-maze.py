from collections import deque

class Solution:
    def numberOfCells(self, r: int, c: int, u: int, d: int, mat: list[list[str]]) -> int:
        if mat[r][c] == '#': 
            return 0

        n, m = len(mat), len(mat[0])
        # Track maximum remaining up moves for visited cells: visited[row][col] = max_u
        visited = [[-1] * m for _ in range(n)]

        # 0-1 BFS: left/right (cost 0 in up/down), up/down (cost 1)
        q = deque([(r, c, u, d)])
        visited[r][c] = u
        ans = 0

        while q:
            cr, cc, cu, cd = q.popleft()
            ans += 1

            # Horizontal moves (free in terms of u/d budget) -> push to left
            for nc in (cc - 1, cc + 1):
                if 0 <= nc < m and mat[cr][nc] != '#' and cu > visited[cr][nc]:
                    visited[cr][nc] = cu
                    q.appendleft((cr, nc, cu, cd))

            # Up move -> cost 1 u
            if cu > 0 and cr > 0 and mat[cr - 1][cc] != '#' and cu - 1 > visited[cr - 1][cc]:
                visited[cr - 1][cc] = cu - 1
                q.append((cr - 1, cc, cu - 1, cd))

            # Down move -> cost 1 d
            if cd > 0 and cr + 1 < n and mat[cr + 1][cc] != '#' and cu > visited[cr + 1][cc]:
                visited[cr + 1][cc] = cu
                q.append((cr + 1, cc, cu, cd - 1))

        return ans 