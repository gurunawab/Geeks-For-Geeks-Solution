class Solution:
    def maxCharGap(self, s: str) -> int:
        first_occurrence = {}
        max_gap = -1
        
        for i, char in enumerate(s):
            if char in first_occurrence:
                
                current_gap = i - first_occurrence[char] - 1
                if current_gap > max_gap:
                    max_gap = current_gap
            else:
               
                first_occurrence[char] = i
                
        return max_gap
