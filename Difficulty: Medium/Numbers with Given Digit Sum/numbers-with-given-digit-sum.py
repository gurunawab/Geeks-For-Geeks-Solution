class Solution:
    def countWays(self, n: int, sum: int) -> int:
    
        if sum < 0 or sum > 9 * n:
            return -1
        
       
        memo = {}
        
        def solve(digits_left, current_sum):
           
            if digits_left == 0:
                return 1 if current_sum == 0 else 0
            if current_sum < 0:
                return 0
                
          
            if (digits_left, current_sum) in memo:
                return memo[(digits_left, current_sum)]
            
           
            start_digit = 1 if digits_left == n else 0
            
            ways = 0
           
            for i in range(start_digit, 10):
                ways += solve(digits_left - 1, current_sum - i)
                
            memo[(digits_left, current_sum)] = ways
            return ways

        ans = solve(n, sum)
        
       
        return ans if ans > 0 else -1
        