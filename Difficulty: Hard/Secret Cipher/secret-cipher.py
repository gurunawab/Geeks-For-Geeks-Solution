class Solution:
    def compress(self, s: str) -> str:
        n = len(s)
        lps = [0] * n
    
        # Build KMP LPS array
        for i in range(1, n):
            j = lps[i - 1]
            while j > 0 and s[i] != s[j]:
                j = lps[j - 1]
            lps[i] = j + (s[i] == s[j])
    
        res, i = [], n
        while i > 0:
            if i % 2 == 0:
                j = lps[i - 1]
                while j > i // 2:
                    j = lps[j - 1]
                if j == i // 2:
                    res.append('*')
                    i //= 2
                    continue
            res.append(s[i - 1])
            i -= 1
    
        return ''.join(reversed(res)) 