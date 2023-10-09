class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        res = 0
        for i in range(len(houses)-1,-1,-1):
            pos = bisect_left(heaters,houses[i])
            if pos > 0 and pos < len(heaters):
                res = max(res,min(abs(houses[i] - heaters[pos]),abs(heaters[pos-1] - houses[i])))
            elif pos == 0:
                res = max(res,abs(heaters[pos] - houses[i]))
                print(res,"yee")
            elif pos == len(heaters):
                print(res,"yoo")
                res = max(res,abs(heaters[pos-1] - houses[i]))
        return res