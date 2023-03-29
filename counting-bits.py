class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n+1):
            arr = []
            while i>0:
                arr.append(i%2)
                i = i//2
            res.append(arr.count(1))
        return res