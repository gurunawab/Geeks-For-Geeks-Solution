class Solution:
    def isNegativeWeightCycle(self, V: int, edges: list[list[int]]) -> bool:
        dist = [0] * V
        for _ in range(V - 1):
            for u, v, w in edges:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
    
        return any(dist[u] + w < dist[v] for u, v, w in edges) 