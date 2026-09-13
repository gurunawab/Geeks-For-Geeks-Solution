from collections import deque

class Solution:
    def shortestPath(self, mat: list[list[int]]) -> int:
        n, m = len(mat), len(mat[0])
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

       
        safe = [[True] * m for _ in range(n)]
        for r in range(n):
            for c in range(m):
                if mat[r][c] == 0:
                    safe[r][c] = False
                    for dr, dc in dirs:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < n and 0 <= nc < m:
                            safe[nr][nc] = False

        
        queue = deque()
        visited = [[False] * m for _ in range(n)]

        for r in range(n):
            if safe[r][0]:
                queue.append((r, 0, 1))  
                visited[r][0] = True

        while queue:
            r, c, dist = queue.popleft()

            
            if c == m - 1:
                return dist

            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < m and safe[nr][nc] and not visited[nr][nc]:
                    visited[nr][nc] = True
                    queue.append((nr, nc, dist + 1))

        return -1