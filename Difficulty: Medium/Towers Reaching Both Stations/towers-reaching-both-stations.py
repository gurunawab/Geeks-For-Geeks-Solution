from collections import deque

class Solution:
    def countCoordinates(self, mat):
        n = len(mat)
        m = len(mat[0])
        
        def bfs(sources):
            visited = [[False for _ in range(m)] for _ in range(n)]
            queue = deque(sources)
            for r, c in sources:
                visited[r][c] = True
            
            while queue:
                r, c = queue.popleft()
                for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < n and 0 <= nc < m and not visited[nr][nc]:
                        if mat[nr][nc] >= mat[r][c]:
                            visited[nr][nc] = True
                            queue.append((nr, nc))
            return visited

       
        p_sources = []
        for i in range(n): p_sources.append((i, 0))
        for j in range(1, m): p_sources.append((0, j))
        reach_P = bfs(p_sources)
        
        
        q_sources = []
        for i in range(n): q_sources.append((i, m - 1))
        for j in range(m - 1): q_sources.append((n - 1, j))
        reach_Q = bfs(q_sources)
        
        count = 0
        for i in range(n):
            for j in range(m):
                if reach_P[i][j] and reach_Q[i][j]:
                    count += 1
        return count
        