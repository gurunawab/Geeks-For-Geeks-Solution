class Solution:

    def minEdgesReq(self, n: int, edges: list[list[int]]) -> int:
        if len(edges) < n - 1:
            return -1

        parent = list(range(n))

        def find(i):
            if parent[i] == i:
                return i
            parent[i] = find(parent[i])
            return parent[i]

        components = n
        for u, v in edges:
            root_u, root_v = find(u), find(v)
            if root_u != root_v:
                parent[root_u] = root_v
                components -= 1

        return components - 1