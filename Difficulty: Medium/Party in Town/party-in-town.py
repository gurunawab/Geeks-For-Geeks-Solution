class Solution:

    def partyHouse(self, adj: list[list[int]]) -> int:
        n = len(adj)
        if n <= 1:
            return 0

        def bfs(src):
            dist = [-1] * (n + 1)
            dist[src] = 0
            q = [src]
            for u in q:
                d = dist[u] + 1
                for v in adj[u - 1]:
                    if dist[v] == -1:
                        dist[v] = d
                        q.append(v)
            farthest = max(range(1, n + 1), key=lambda x: dist[x])
            return farthest, dist[farthest]

        u, _ = bfs(1)
        _, diameter = bfs(u)
        return (diameter + 1) // 2