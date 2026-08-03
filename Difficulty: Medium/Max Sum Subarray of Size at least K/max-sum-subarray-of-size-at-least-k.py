class Solution:
    def maxSumWithK(self, arr: list[int], k: int) -> int:
        n = len(arr)
        
        max_ending_at = [0] * n
        max_ending_at[0] = arr[0]
        
        for i in range(1, n):
            max_ending_at[i] = max(arr[i], max_ending_at[i - 1] + arr[i])
            
        current_k_sum = sum(arr[:k])
        max_sum = current_k_sum
        
        for i in range(k, n):
            current_k_sum += arr[i] - arr[i - k]
            
            sum_with_prefix = current_k_sum + max(0, max_ending_at[i - k])
            
            max_sum = max(max_sum, sum_with_prefix)
            
        return max_sum