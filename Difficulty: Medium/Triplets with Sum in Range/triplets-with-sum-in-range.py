class Solution:
    def countTriplets(self, arr: list[int], l: int, r: int) -> int:
        arr.sort()
    
        def count_le(val):
            cnt = 0
            for i in range(len(arr) - 2):
                j, k = i + 1, len(arr) - 1
                while j < k:
                    if arr[i] + arr[j] + arr[k] <= val:
                        cnt += k - j
                        j += 1
                    else:
                        k -= 1
            return cnt
    
        return count_le(r) - count_le(l - 1) 