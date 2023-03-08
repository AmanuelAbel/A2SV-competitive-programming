class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arr = []
        res = 1
        counter = 0
        for i in nums:
            if i == 0:
                counter += 1
            else:
                res *= i
        for i in nums:
            if counter > 1  :
                arr.append(0)
            elif counter == 1 and i == 0:
                arr.append(int(res))
            elif counter == 1 and i != 0:
                arr.append(0)
            elif counter == 0 :
                arr.append(int(res/i))
        return arr