from bisect import bisect_left
from itertools import accumulate

class Solution:
    def getMarks(self, l, r, rank):
        pref = list(accumulate(b - a + 1 for a, b in zip(l, r)))
        return [l[i] + k - 1 - (pref[i - 1] if i else 0) for k in rank for i in [bisect_left(pref, k)]] 