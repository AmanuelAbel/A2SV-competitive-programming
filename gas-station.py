class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        res = []
        for i in range(len(gas)):
            res.append(gas[i]-cost[i])
        if sum(res) < 0:
            return -1
        start = 0
        ans = 0
        for i,s in enumerate(res):
            ans += s
            if (ans) < 0:
                start = i+1
                ans = 0
        return start