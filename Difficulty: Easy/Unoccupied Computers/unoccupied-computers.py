class Solution:
    def solve(self, n: int, s: str) -> int:
        seen, allocated, unassigned = set(), set(), 0
        for c in s:
            if c not in seen:
                seen.add(c)
                if len(allocated) < n:
                    allocated.add(c)
                else:
                    unassigned += 1
            elif c in allocated:
                allocated.remove(c)
        return unassigned  