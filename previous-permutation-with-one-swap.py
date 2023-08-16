class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
            n = len(arr)
            left, right = n - 2, n - 1
            while left >= 0 and arr[left] <= arr[left + 1]:
                left -= 1
            if left == -1:
                return arr  
            
            while arr[right] >= arr[left] or arr[right] == arr[right - 1]:
                right -= 1
            
            arr[left], arr[right] = arr[right], arr[left]
            return arr