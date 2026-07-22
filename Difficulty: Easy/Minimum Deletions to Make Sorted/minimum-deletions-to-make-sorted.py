import bisect

class Solution:
    def minDeletions(self, arr):
        tails = []
        
        for x in arr:
            # Find the insertion index to maintain strictly increasing order
            idx = bisect.bisect_left(tails, x)
            
            # If x is larger than all elements in tails, append it
            if idx == len(tails):
                tails.append(x)
            else:
                # Replace the existing element at idx with x
                tails[idx] = x
                
        lis_length = len(tails)
        return len(arr) - lis_length