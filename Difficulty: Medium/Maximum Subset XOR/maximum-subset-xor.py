class Solution:
    def maxSubsetXOR(self, arr):
        basis = [0] * 32
        
        for num in arr:
            for i in range(31, -1, -1):
                if not (num & (1 << i)):
                    continue
                if not basis[i]:
                    basis[i] = num
                    break
                num ^= basis[i]
                
        res = 0
        for i in range(31, -1, -1):
            if (res ^ basis[i]) > res:
                res ^= basis[i]
                
        return res