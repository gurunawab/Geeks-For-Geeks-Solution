class Solution:
    def minCost(self, mat: list[list[int]]) -> int:
        a, b, c = 0, 0, 0
        for x, y, z in mat:
            a, b, c = x + min(b, c), y + min(a, c), z + min(a, b)
        return min(a, b, c) 