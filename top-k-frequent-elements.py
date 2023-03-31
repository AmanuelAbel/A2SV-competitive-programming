class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        arr = [[] for i in range(len(nums) + 1)]
        for i in nums:
            count[i] = 1 + count.get(i,0)

        for i,n in count.items():
            arr[n].append(i)
        res = []
        for i in range(len(arr)-1 , 0,-1):
            for n in arr[i]:
                res.append(n)
            if len(res) == k:
                return res