class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        l = 0
        r = int(sqrt(c))
        while l<=r:
            z = (l*l) + (r*r)
            if z > c:
                r -= 1
            elif z < c:
                l += 1
            else:
                return True