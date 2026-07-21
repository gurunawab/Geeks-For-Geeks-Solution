class Solution:
    def maxIndexDifference(self, s: str) -> int:
        first_a = s.find('a')
        if first_a == -1:
            return -1
        
        # 1. Compute min_reach: earliest index where each character can be reached
        min_reach = {'a': first_a}
        for i in range(1, 26):
            ch = chr(ord('a') + i)
            prev_ch = chr(ord('a') + i - 1)
            
            if prev_ch not in min_reach:
                break
            
            # Find first occurrence of `ch` after the earliest reachable `prev_ch`
            idx = s.find(ch, min_reach[prev_ch] + 1)
            if idx != -1:
                min_reach[ch] = idx
            else:
                break

        # 2. Compute last occurrence of each character in the string
        last_occ = {}
        for idx, ch in enumerate(s):
            last_occ[ch] = idx
            
        max_diff = 0  # Default max diff is 0 (if no jumps can be made from 'a')
        
        # 3. Check all valid terminal characters ('b' through 'z')
        for i in range(1, 26):
            ch = chr(ord('a') + i)
            prev_ch = chr(ord('a') + i - 1)
            next_ch = chr(ord('a') + i + 1) if i < 25 else None
            
            # Character must be reachable from 'a'
            if prev_ch in min_reach and ch in last_occ:
                if last_occ[ch] > min_reach[prev_ch]:
                    # A character is terminal if no `next_ch` exists after its last occurrence
                    if next_ch is None or next_ch not in last_occ or last_occ[ch] > last_occ[next_ch]:
                        max_diff = max(max_diff, last_occ[ch] - first_a)
                    
        return max_diff