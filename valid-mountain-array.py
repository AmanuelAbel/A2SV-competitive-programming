class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        counter = 0
        for i in range(1,len(arr)):
            if arr[i-1] >= arr[i]:
                break
            counter += 1
        print(counter)
        if counter == 0 or counter+1 == len(arr):
            return False
        else:
            for i in range(counter+1,len(arr)):
                if arr[i-1] <= arr[i]:
                    return False
        return True