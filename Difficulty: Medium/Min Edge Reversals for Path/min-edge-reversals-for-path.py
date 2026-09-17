from collections import defaultdict
import heapq


class Solution:

    def minimumEdgeReversal(
        self, edges: list[list[int]], n: int, src: int, dst: int
    ) -> int:
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append((v, 0))  # Original edge costs 0 reversals
            adj[v].append((u, 1))  # Reversed edge costs 1 reversal

        pq, dist = [(0, src)], {src: 0}
        while pq:
            d, u = heapq.heappop(pq)
            if u == dst:
                return d
            if d > dist[u]:
                continue
            for v, w in adj[u]:
                if d + w < dist.get(v, float("inf")):
                    dist[v] = d + w
                    heapq.heappush(pq, (d + w, v))
        return -1