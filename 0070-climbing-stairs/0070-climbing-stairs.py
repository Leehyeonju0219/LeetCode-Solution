from collections import defaultdict

class Solution:
    dp = defaultdict(int)

    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        
        if n == 2:
            return 2
        
        if n not in self.dp:
            self.dp[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        
        return self.dp[n]