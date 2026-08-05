class Solution:
    def countSubarray(self, arr: list[int], l: int, r: int) -> int:
        def countAtMost(target: int) -> int:
            ans = left = curr = 0
            for right in range(len(arr)):
                curr += arr[right]
                while curr > target and left <= right:
                    curr -= arr[left]
                    left += 1
                ans += right - left + 1
            return ans

        return countAtMost(r) - countAtMost(l - 1)