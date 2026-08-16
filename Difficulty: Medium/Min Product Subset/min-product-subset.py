import math

class Solution:
    def minProd(self, arr):
        if len(arr) == 1:
            return arr[0]

        negs = [x for x in arr if x < 0]

       
        if not negs:
            return 0 if 0 in arr else min(arr)

       
        prod = math.prod(x for x in arr if x != 0)

       
        return prod // max(negs) if len(negs) % 2 == 0 else prod 