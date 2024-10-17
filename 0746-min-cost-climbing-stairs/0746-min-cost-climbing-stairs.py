from collections import defaultdict

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost_len = len(cost)
        
        v = defaultdict(int)
        def dp(n):
            if n == 0:
                v[n] = cost[0]
            if n == 1:
                v[n] = cost[1]
            
            if n not in v:
                if n < cost_len:
                    v[n] = cost[n] + min(dp(n-1), dp(n-2))
                else:
                    v[n] = min(dp(n-1), dp(n-2))
            
            return v[n]
        
        return dp(cost_len)