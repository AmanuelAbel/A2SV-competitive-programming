class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        myset = set(arr)
        n = 0
        for i in range(1,arr[-1]+1):
            if i not in myset:
                n += 1
            if n == k:
                return i
        return arr[-1] + k - n
