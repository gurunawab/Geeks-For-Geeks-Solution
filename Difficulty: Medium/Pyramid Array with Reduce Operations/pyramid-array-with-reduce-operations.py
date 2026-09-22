class Solution:
    def formPyramid(self, arr):
        n = len(arr)
        L = [0] * n
        R = [0] * n

        # Maximum increasing ramp from left
        for i in range(n):
            L[i] = min(arr[i], (L[i - 1] + 1) if i > 0 else 1)

        # Maximum decreasing ramp from right
        for i in range(n - 1, -1, -1):
            R[i] = min(arr[i], (R[i + 1] + 1) if i < n - 1 else 1)

        # Maximize peak height x
        max_x = max(min(L[i], R[i]) for i in range(n))
        return sum(arr) - max_x * max_x