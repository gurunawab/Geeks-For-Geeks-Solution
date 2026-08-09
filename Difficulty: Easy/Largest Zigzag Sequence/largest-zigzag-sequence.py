class Solution:
    def zigzagSequence(self, mat):
        dp = mat[0]
        for row in mat[1:]:
            dp = [val + max(dp[:j] + dp[j+1:]) for j, val in enumerate(row)]
        return max(dp)