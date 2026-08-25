class Solution:
    def minMoves(self, arr):
        pos = {val: i for i, val in enumerate(arr)}
        curr = max_len = 0
        for i in range(1, len(arr) + 1):
            curr = curr + 1 if i == 1 or pos[i] > pos[i - 1] else 1
            max_len = max(max_len, curr)
        return len(arr) - max_len 