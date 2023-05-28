class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        z = len(cost)-1
        counter = 0
        cache = [0]*(z+1)
        cache[z] = cost[z]
        cache[z-1] = cost[z-1]
        for i in range(len(cost)-3,-1,-1):
            cache[i] = min(cost[i]+cache[i+2],cache[i+1]+cost[i])
        return min(cache[0],cache[1])