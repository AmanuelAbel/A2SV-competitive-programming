class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        arr1 = [0]*32
        arr2 = [0]*32
        i = 0
        j = 0
        res = 0
        while x > 0 or y > 0:
            arr1[i] = x%2
            x = x//2
            arr2[i] = y%2
            y = y//2
            i+=1
        for i in range(32):
            z = arr1[i] ^ arr2[i]
            if z == 1:
                res += 1
        return res