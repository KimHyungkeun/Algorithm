class Solution:
    def tribonacci(self, n: int) -> int:
        dp = [0,1,1]
        
        if n <= 2 :
            return dp[n]
        
        idx = 2
        
        while idx != n :
            total = sum(dp)
            dp[0] = dp[1]
            dp[1] = dp[2]
            dp[2] = total
            idx += 1
        
        return dp[2]