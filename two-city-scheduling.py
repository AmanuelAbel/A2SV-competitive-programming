class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        arr = []
        countA = 0
        countB = 0
        res = 0
        n = len(costs)
        for i in costs:
            arr.append([abs(i[0]-i[1]),i[0],i[1]])
        arr.sort()
        print(arr,n)
        for i in arr:
            if i[1] < i[2]:
                countA += 1
                res += i[1]
            else:
                countB += 1
                res += i[2]
        print(countA,countB,res)
        if countA == countB:
            return res
        elif countA > countB:
            i = 0
            while i < len(arr) and countA != n//2:
                if arr[i][2] > arr[i][1]:
                    res += arr[i][0]
                    countA -= 1
                i+=1
        else:
            i = 0
            while i < len(arr) and countB != n//2:
                if arr[i][1] >= arr[i][2]:
                    res += arr[i][0]
                    countB -= 1
                i += 1

        return res