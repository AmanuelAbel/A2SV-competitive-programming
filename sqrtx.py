class Solution:
    def mySqrt(self, x: int) -> int:
        l,r = 1 , x//2
        mid = 0
        if x == 0 or x == 1:
            return x
            print(x)
        while l <= r:
            mid = (r + l) // 2
            res = mid*mid
            
            if res > x:
                r = mid - 1
            else:
                ans = mid
                l = mid + 1
        return ans