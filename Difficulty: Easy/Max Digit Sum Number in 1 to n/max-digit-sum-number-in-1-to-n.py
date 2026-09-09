class Solution:
    def findMax(self, n: int) -> int:
        s = str(n)
        cand = [n] + [int(s[:i] + str(int(s[i]) - 1) + '9' * (len(s) - 1 - i)) 
                      for i in range(len(s)) if s[i] > '0']
        return max(cand, key=lambda x: (sum(map(int, str(x))), x))