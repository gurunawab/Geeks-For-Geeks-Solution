class Solution:

    def maxFruits(self, arr: list[int], m: int) -> int:
      curr = max_val = sum(arr[:m])
      for i in range(len(arr) - 1):
        curr += arr[(i + m) % len(arr)] - arr[i]
        max_val = max(max_val, curr)
      return max_val 