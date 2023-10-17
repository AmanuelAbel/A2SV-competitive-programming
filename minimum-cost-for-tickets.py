class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = max(days)
        dp = [-1]*n
        for i in days:
            dp[i-1] = 0
        dp[-1] = min(costs)
        for i in range(n-2,-1,-1):
            if dp[i] == 0:
                if i + 7 > n - 1:
                    week = 0
                else:
                    week = dp[i+7]
                if i + 30 > n - 1:
                    month = 0
                else:
                    month = dp[i+30]
                
                dp[i] = min(costs[2]+month,costs[1]+week,costs[0]+dp[i+1])
            else:
                dp[i] = dp[i+1]
        return dp[0]