class Solution:
    def countFriendsPairings(self, n: int) -> int:
        a, b = 1, 1
        for i in range(1, n):
            a, b = b, b + i * a
        return b
        