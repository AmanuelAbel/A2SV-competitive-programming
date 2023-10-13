class Solution:
    def knightDialer(self, n: int) -> int:
        dialer ={0 : [4,6] , 1:[6,8] , 2:[7,9] , 3:[4,8] , 4:[9,0,3] , 5:[] , 6:[1,7,0] , 7:[6,2] , 8:[3,1] , 9:[4,2]}
        dp = [1] * 10
        for i in range(n-1):
            temp = []
            for j in range(10):

                res = 0
                for k in dialer[j]:
                    res += dp[k]
                temp.append(res)
            dp = temp[:]
        return sum(dp) % (10**9+7)