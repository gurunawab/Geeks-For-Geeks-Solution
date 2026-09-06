class Solution:
    def pairAndSum(self, arr):
        ans = 0
        for b in range(30):
            cnt = sum((x >> b) & 1 for x in arr)
            ans += (cnt * (cnt - 1) // 2) << b
        return ans