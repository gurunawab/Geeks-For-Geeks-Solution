class Solution:
    def isPossible(self, arr, s, x):
        P, cur = [s], s
        for a in arr:
            if cur + a > x: break
            P.append(cur + a)
            cur += P[-1]
        
        for v in reversed(P):
            if x >= v: x -= v
            
        return x == 0
        