class Solution:
    def arraySortedOrNot(self, arr, n):
        # code here
        for left in range(len(arr)-1):
            right = left + 1
            if arr[left] > arr[right]:
                return 0
        return 1