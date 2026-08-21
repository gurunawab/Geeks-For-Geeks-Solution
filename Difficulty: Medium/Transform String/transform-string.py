from collections import Counter


class Solution:

    def transform(self, s1: str, s2: str) -> int:
        if Counter(s1) != Counter(s2):
            return -1
        i, j = len(s1) - 1, len(s2) - 1
        while i >= 0:
            if s1[i] == s2[j]:
                j -= 1
            i -= 1
        return j + 1 