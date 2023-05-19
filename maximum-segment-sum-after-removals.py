class Solution:
    def maximumSegmentSum(self, nums: List[int], removeQueries: List[int]) -> List[int]:
        parent = [i for i in range(len(nums))]
        arr = [0]*len(nums)
        summ = []
        for i in nums:
            summ.append(i)
        def isvalid(n):
            if n >= len(nums) or n < 0 or arr[n] == 0:
                return False
            return True 
        def find(n):
            if parent[n] != n:
                parent[n] = find(parent[n])
            return parent[n]
        def union(a,b):
            x = find(a)
            y = find(b)
            parent[x] = y
            summ[y] += summ[x]
        maximum = 0
        ans = [0]
        for z in range(len(nums)-1,0,-1):
            i = removeQueries[z]
            if isvalid(i+1):
                union(i,i+1)
                arr[i+1] = 1
            if isvalid(i-1):
                union(i,i-1)
                arr[i-1] = 1
            arr[i] = 1
            maximum = max(maximum,summ[find(i)])
            ans.append(maximum)
        return reversed(ans)