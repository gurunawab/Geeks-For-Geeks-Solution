from collections import defaultdict, deque

class Solution:
    def maxDistance(self, V, src, edges):
        INF = -2147483648
        adj = defaultdict(list)
        indegree = [0] * V
        
        for u, v, w in edges:
            adj[u].append((v, w))
            indegree[v] += 1
            
        q = deque([i for i in range(V) if indegree[i] == 0])
        
        dist = [INF] * V
        dist[src] = 0
        
        while q:
            u = q.popleft()
            for v, w in adj[u]:
                if dist[u] != INF:
                    dist[v] = max(dist[v], dist[u] + w)
                indegree[v] -= 1
                if indegree[v] == 0:
                    q.append(v)
                    
        return dist            