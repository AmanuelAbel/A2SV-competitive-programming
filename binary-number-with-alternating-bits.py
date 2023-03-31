class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        i = 0
        while 1<<i+1 < n:
            z = 1<<i
            y = 1<<i+1
            if n&z ==0:
                if n&y== 0:
                    return False
            else:
                if n&y != 0:
                    return False
            i+=1
        return True