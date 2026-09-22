class Solution:
    def findLongestWord(self, s: str, d: list) -> str:
        for w in sorted(d, key=lambda x: (-len(x), x)):
            it = iter(s)
            if all(c in it for c in w):
                return w
        return ""