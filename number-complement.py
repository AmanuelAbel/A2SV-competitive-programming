class Solution:
    def findComplement(self, num: int) -> int:
        string = ""
        res = 0
        while num > 0:
            string+=str(num%2^1)
            num = num//2
        length = len(string)-1
        for i in range(len(string)):
            res += int(string[length-i]) *int(2**(length-i))
        return res